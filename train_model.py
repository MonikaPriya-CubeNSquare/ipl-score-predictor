import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
import os

# --- Load Data ---
df = pd.read_csv('data/ipl_data.csv')

# --- Clean & Prepare ---
df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
df.drop(columns=['mid'], inplace=True)

# Optional: Sample a portion for faster experimentation (remove this line in production)
# df = df.sample(frac=0.3, random_state=42)

# --- One-Hot Encode ---
df = pd.get_dummies(df, columns=[
    'bat_team', 'bowl_team', 'venue',
    'batsman', 'bowler', 'striker', 'non-striker'
])

# --- Features & Target ---
X = df.drop('total', axis=1)
y = df['total']

# --- Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train Model (Optimized) ---
model = RandomForestRegressor(
    n_estimators=50,          # reduced for speed
    max_depth=20,             # limits tree depth
    max_features='sqrt',      # faster split finding
    random_state=42,
    n_jobs=-1                 # use all CPU cores
)

print("⏳ Training the model... (this might take a moment)")
model.fit(X_train, y_train)

# --- Save Model ---
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to models/model.pkl")