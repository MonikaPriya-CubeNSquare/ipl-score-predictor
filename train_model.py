import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load the data
df = pd.read_csv('data/ipl_data.csv')

# Drop or convert columns
df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
columns_to_drop = ['batsman', 'bowler', 'non_striker', 'striker']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['bat_team', 'bowl_team', 'venue'])

# Define features and target
X = df.drop('total', axis=1)
y = df['total']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")
