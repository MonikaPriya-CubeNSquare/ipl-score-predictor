

```markdown
# 🏏 CubeNSquare's Pallikoodam – IPL Score Predictor

Welcome to the official repository for the **IPL Score Predictor App**, a machine learning-powered tool developed as part of the *CubeNSquare’s Pallikoodam – Data Science Internship*. This project showcases how historical match data, team dynamics, and player performance can be used to predict the final score of an IPL innings in real time.

---

## 📌 Project Overview

This Streamlit-based web application allows users to enter current match details—like batting team, bowler, stadium, runs scored so far, and player names—and predicts the expected final score using a trained **Random Forest Regressor** model.

> Think of it as cricket meets data science: you're modeling momentum, pressure, and match conditions to generate live predictions.

---

## 🧠 Key Features

- Real-time final score prediction based on match inputs
- Team and venue-specific learning using one-hot encoded features
- Player-level modeling: `batsman`, `bowler`, `striker`, `non-striker`
- Built with Python, Streamlit, and scikit-learn
- Ready for deployment on **Streamlit Cloud**

---

## 📊 Dataset Schema

We use a historical IPL dataset (`ipl_data.csv`) that contains per-ball or per-over match snapshots with the following key columns:

| Column            | Description                            |
|-------------------|----------------------------------------|
| `date`            | Date of the match                      |
| `venue`           | Stadium where the match was played     |
| `bat_team`        | Batting team name                      |
| `bowl_team`       | Bowling team name                      |
| `batsman`         | Currently batting player               |
| `bowler`          | Current bowler                         |
| `striker`         | Player facing the delivery             |
| `non-striker`     | Other player on strike                 |
| `runs`            | Runs scored so far                     |
| `wickets`         | Wickets fallen                         |
| `overs`           | Overs completed                        |
| `runs_last_5`     | Runs scored in the last 5 overs        |
| `wickets_last_5`  | Wickets lost in the last 5 overs       |
| `total`           | **Target variable:** final score       |

---

## 📁 Project Structure

```
CubeNSquare_IPL_Score_Predictor/
├── app.py                  # Streamlit app UI
├── train_model.py          # Model training script
├── requirements.txt        # Python dependencies
├── README.md               # Project guide
├── data/
│   └── ipl_data.csv        # Cleaned IPL dataset
├── models/
│   └── model.pkl           # Trained ML model
```

---

## ⚙️ Setup Instructions

> Recommended: Use VS Code and a virtual environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/ipl-score-predictor.git
   cd ipl-score-predictor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Model**
   ```bash
   python train_model.py
   ```

   This generates `model.pkl` inside the `models/` folder.

---

## ▶️ Run the App Locally

Once the model is trained, launch the web app with:

```bash
streamlit run app.py
```

This opens the app in your default browser. You can enter match conditions and predict the final score!

---

## 🌐 Deploying to Streamlit Cloud

> Make your app public and shareable!

1. Push your entire project to a GitHub repo
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in
3. Click **“New app”**, select your GitHub repo, and set `app.py` as the main file
4. Click **Deploy**

You'll get a public URL to share with your team and mentors 🎉

---

## ✅ Technologies Used

- Python 3.10+
- Pandas, scikit-learn
- Streamlit
- RandomForestRegressor
- GitHub + Streamlit Cloud

---

## 🚧 Future Improvements

- Add model confidence intervals or prediction ranges
- Experiment with XGBoost or LightGBM for improved accuracy
- Use live match APIs for auto-populating match stats
- Visualize feature importance and add explainability

---

## 🙋‍♀️ About the Internship

This project is part of **CubeNSquare’s Pallikoodam Data Science Internship**, focused on real-world machine learning applications, hands-on model building, and end-to-end deployment.

Want to contribute or learn more? Reach out to the internship coordinator or open an issue on this repo!

---

## 📃 License

MIT License – use, modify, and share responsibly.
```

---

