import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib  # To save the model
from sklearn.preprocessing import LabelEncoder  # For encoding categorical data

# Load your dataset (replace 'your_dataset.csv' with your actual dataset)
data = pd.read_csv('Training.csv')

# Display the first few rows of the dataset to understand its structure
print("Data Preview:")
print(data.head())

# Display dataset information
print("\nDataset Info:")
print(data.info())

# Drop the unnecessary column
data = data.drop(columns=['Unnamed: 133'], errors='ignore')  # Use errors='ignore' to avoid errors if the column doesn't exist

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Continue with the same process: splitting into X (features) and y (target)
X = data.iloc[:, :-1]  # Features (all columns except the last one)
y = data.iloc[:, -1]   # Target (last column)

# Encode categorical features
label_encoders = {}
for column in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    label_encoders[column] = le  # Save the encoder for later use

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)  # Set random_state for reproducibility
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Save the trained model as model.pkl
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")

# Optionally, save label encoders for future use
joblib.dump(label_encoders, 'label_encoders.pkl')
print("Label encoders saved as label_encoders.pkl")
