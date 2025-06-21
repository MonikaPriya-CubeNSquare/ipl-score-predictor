import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="CubeNSquare IPL Predictor", layout="centered")

st.title("🏏 CubeNSquare IPL Score Predictor")
st.caption("Part of the Pallikoodam Data Science Internship")

# Try loading the model
try:
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    model_features = model.feature_names_in_
except Exception as e:
    st.error(f"Model could not be loaded: {e}")
    st.stop()

# User input fields
bat_team = st.selectbox("Batting Team", ['RCB', 'MI', 'CSK', 'KKR'])
bowl_team = st.selectbox("Bowling Team", ['RCB', 'MI', 'CSK', 'KKR'])
venue = st.selectbox("Venue", ['Mumbai', 'Chennai', 'Delhi'])

runs = st.number_input("Current Runs", min_value=0, step=1)
wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)
overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
run_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0, step=1)
wicket_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, step=1)

# Build input dictionary
input_dict = {
    'runs': runs,
    'wickets': wickets,
    'overs': overs,
    'run_last_5': run_last_5,
    'wicket_last_5': wicket_last_5,
    f'bat_team_{bat_team}': 1,
    f'bowl_team_{bowl_team}': 1,
    f'venue_{venue}': 1
}

# Initialize input DataFrame and fill missing columns
input_df = pd.DataFrame([input_dict])
for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_features]

# Button to predict
if st.button("Predict Final Score"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏆 Predicted Final Score: {int(prediction)}")
        with st.expander("📊 See Input Features"):
            st.write(input_df)
    except Exception as e:
        st.error(f"Prediction failed: {e}")
