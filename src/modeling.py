import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

class InsuranceModeler:
    def __init__(self, df):
        self.df = df
        self.models = {}
        self.feature_names = None

    def preprocess(self):
        """
        Prepare features (X) and target (y).
        Using TotalClaims as target for Risk Model.
        """
        # Filter for relevant columns
        features = [
            'VehicleType', 'Make', 'Province', 'Gender', 'PostalCode',
            'SumInsured', 'CalculatedPremiumPerTerm', 'Cubiccapacity', 'Kilowatts'
        ]
        target = 'TotalClaims'
        
        # Drop rows where target is missing
        data = self.df.dropna(subset=[target] + features)
        
        X = data[features]
        y = data[target]

        # Define transformations
        numeric_features = ['SumInsured', 'CalculatedPremiumPerTerm', 'Cubiccapacity', 'Kilowatts']
        categorical_features = ['VehicleType', 'Make', 'Province', 'Gender', 'PostalCode']

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
            ])

        return train_test_split(X, y, test_size=0.2, random_state=42), preprocessor

    def train_linear_regression_per_zipcode(self):
        """
        Requirement: For each zipcode, fit a linear regression (TotalClaims).
        Note: Demonstrated on top 5 zipcodes to save time.
        """
        print("\n--- Linear Regression per ZipCode (Top 5) ---")
        top_zips = self.df['PostalCode'].value_counts().head(5).index
        
        for zipcode in top_zips:
            subset = self.df[self.df['PostalCode'] == zipcode]
            if len(subset) > 10: # Minimum data check
                X = subset[['TotalPremium', 'SumInsured']].fillna(0)
                y = subset['TotalClaims']
                
                model = LinearRegression()
                model.fit(X, y)
                print(f"ZipCode: {zipcode}, R2: {model.score(X, y):.4f}, Coeff: {model.coef_}")

    def train_xgboost(self, X_train, y_train, preprocessor):
        """
        Train XGBoost Regressor for Claim Prediction.
        """
        print("\n--- Training XGBoost Model ---")
        
        # Create pipeline
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1))
        ])
        
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performance -> RMSE: {rmse:.2f}, MAE: {mae:.2f}, R2: {r2:.4f}")

    def explain_with_shap(self, model, X_train, preprocessor):
        """
        SHAP Feature Importance Analysis.
        """
        print("\n--- Generating SHAP Explanations ---")
        
        # Extract the regressor and transformed data
        regressor = model.named_steps['regressor']
        
        # Transform X_train to get feature names
        X_transformed = preprocessor.transform(X_train)
        
        # Get feature names from OneHotEncoder
        cat_encoder = preprocessor.named_transformers_['cat']
        cat_features = cat_encoder.get_feature_names_out()
        num_features = ['SumInsured', 'CalculatedPremiumPerTerm', 'Cubiccapacity', 'Kilowatts']
        all_features = np.concatenate([num_features, cat_features])
        
        # SHAP Explainer
        explainer = shap.Explainer(regressor, X_transformed)
        shap_values = explainer(X_transformed)
        
        # Plot
        shap.summary_plot(shap_values, X_transformed, feature_names=all_features, show=False)
        plt.savefig("shap_summary.png")
        print("SHAP Summary plot saved as 'shap_summary.png'")

if __name__ == "__main__":
    from data_loader import load_data, clean_data
    
    # Load
    df = load_data('../data/insurance_claims.csv')
    df = clean_data(df)
    
    # Initialize Modeler
    modeler = InsuranceModeler(df)
    
    # 1. Linear Regression per Zip
    modeler.train_linear_regression_per_zipcode()
    
    # 2. Advanced ML (XGBoost)
    (X_train, X_test, y_train, y_test), preprocessor = modeler.preprocess()
    xgb_model = modeler.train_xgboost(X_train, y_train, preprocessor)
    
    # 3. Evaluate
    modeler.evaluate_model(xgb_model, X_test, y_test)
    
    # 4. Interpret
    # Note: SHAP can be slow on large datasets; sample if necessary
    modeler.explain_with_shap(xgb_model, X_train[:1000], preprocessor)