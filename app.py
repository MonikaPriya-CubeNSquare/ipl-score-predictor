import streamlit as st
import pandas as pd
import pickle
import os
import gdown
import requests

st.set_page_config(page_title="CubeNSquare IPL Predictor", layout="centered")
st.title("🏏 CubeNSquare IPL Score Predictor")
st.caption("Now featuring player-level insights — powered by Data Science interns!")

MODEL_ID = "14c_fAFqU5f9rCT5k5lgGuQL3PKQpTlWi"
MODEL_URL = f"https://drive.google.com/uc?export=download&id={MODEL_ID}"
MODEL_PATH = "models/model.pkl"

# Download model if not already present
if not os.path.exists(MODEL_PATH):
    try:
        os.makedirs("models", exist_ok=True)
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False, use_cookies=True)
    except Exception as e:
        st.warning(f"⚠️ gdown failed: {e}\nTrying backup method...")
        try:
            with requests.get(MODEL_URL, stream=True) as r:
                r.raise_for_status()
                with open(MODEL_PATH, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except Exception as err:
            st.error(f"❌ Could not download model: {err}")
            st.stop()

# Load model
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    model_features = model.feature_names_in_
except Exception as e:
    st.error(f"❌ Model could not be loaded: {e}")
    st.stop()

# Extract encoded options dynamically
def extract_options(prefix):
    return sorted(set(col.replace(prefix + '_', '') for col in model_features if col.startswith(prefix + '_')))

teams = extract_options('bat_team')
venues = extract_options('venue')
players = extract_options('batsman')

# User Inputs
bat_team = st.selectbox("Batting Team", teams)
bowl_team = st.selectbox("Bowling Team", teams)
venue = st.selectbox("Venue", venues)
batsman = st.selectbox("Batsman", players)
bowler = st.selectbox("Bowler", players)
striker = st.selectbox("Striker", players)
non_striker = st.selectbox("Non-Striker", players)

runs = st.number_input("Current Runs", min_value=0, step=1)
wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)
overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
run_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0, step=1)
wicket_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, step=1)

# Input dictionary and prediction
input_dict = {
    'runs': runs,
    'wickets': wickets,
    'overs': overs,
    'run_last_5': run_last_5,
    'wicket_last_5': wicket_last_5,
    f'bat_team_{bat_team}': 1,
    f'bowl_team_{bowl_team}': 1,
    f'venue_{venue}': 1,
    f'batsman_{batsman}': 1,
    f'bowler_{bowler}': 1,
    f'striker_{striker}': 1,
    f'non-striker_{non_striker}': 1
}

input_df = pd.DataFrame([input_dict])
for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_features]

# Predict
if st.button("Predict Final Score"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏆 Predicted Final Score: {int(prediction)}")
        with st.expander("📊 View Input Details"):
            st.write(input_df)
    except Exception as e:
        st.error(f"Prediction failed: {e}")