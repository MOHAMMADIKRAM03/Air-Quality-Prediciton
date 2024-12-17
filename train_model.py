import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv(r'C:\Users\ASUS\PycharmProjects\Air-Quality-Prediction-Final\Real_Combine.csv')

# Drop rows where the target variable 'PM 2.5' has NaN values
data = data.dropna(subset=['PM 2.5'])

# Separate features and target variable
X = data[['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM']]
y = data['PM 2.5']  # Updated target column name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model (optional)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error on Test Set: {mse}")

# Save the trained model to a file using pickle
filename = 'random_forest_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print(f"Model trained and saved as {filename} successfully!")
