# 🏏 CubeNSquare’s Pallikoodam – IPL Score Predictor

Welcome to the official repository for the **IPL Score Predictor App**, a machine‑learning–powered tool developed as part of the *CubeNSquare’s Pallikoodam – Data Science Internship*. This project showcases how historical match data, team dynamics, and player performance can be used to predict the final score of an IPL innings **in real time**.

---

## 📌 Project Overview

This **Streamlit** web application allows users to enter current match details—batting team, bowler, venue, runs so far, player names, etc.—and predicts the expected final score using a trained **Random Forest Regressor** model.

> Think of it as cricket × data science: modeling momentum, pressure, and match conditions to generate live predictions.

---

## 🧠 Key Features

* **Real‑time** final‑score prediction based on live match inputs
* Team‑ and venue‑specific learning via one‑hot encoded features
* Player‑level modeling: `batsman`, `bowler`, `striker`, `non‑striker`
* Built with **Python**, **Streamlit**, and **scikit‑learn**
* Ready for one‑click deployment on **Streamlit Cloud**

---

## 📊 Dataset Schema

We use a cleaned historical IPL dataset (`data/ipl_data.csv`) containing per‑over snapshots with the following key columns:

| Column           | Description                             |
| ---------------- | --------------------------------------- |
| `date`           | Match date                              |
| `venue`          | Stadium where the match was played      |
| `bat_team`       | Batting team                            |
| `bowl_team`      | Bowling team                            |
| `batsman`        | Current batsman                         |
| `bowler`         | Current bowler                          |
| `striker`        | Player facing the delivery              |
| `non_striker`    | Runner at the non‑striker’s end         |
| `runs`           | Runs scored so far                      |
| `wickets`        | Wickets fallen                          |
| `overs`          | Overs completed                         |
| `runs_last_5`    | Runs in the last 5 overs                |
| `wickets_last_5` | Wickets lost in the last 5 overs        |
| `total`          | **Target** – final score of the innings |

---

## 📁 Project Structure

```text
CubeNSquare_IPL_Score_Predictor/
├── app.py            # Streamlit UI
├── train_model.py    # Model‑training script
├── requirements.txt  # Python dependencies
├── README.md         # Project guide (this file)
├── data/
│   └── ipl_data.csv  # Cleaned IPL dataset
└── models/
    └── model.pkl     # Trained ML model
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your‑username>/ipl-score-predictor.git
cd ipl-score-predictor
```

### 2. Create & activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

This generates `models/model.pkl`.

---

## ▶️ Run the app locally

```bash
streamlit run app.py
```

Your default browser will open the app. Enter live match conditions and get an instant score projection!

---

## 🌐 Deploy to Streamlit Cloud

1. Push your project to **GitHub**.
2. Sign in to [streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **New App**, choose your repo, and set **`app.py`** as the main file.
4. Click **Deploy** – get a public URL to share with mentors and friends 🎉.

---

## 🛠️ Quick one‑liner for setup & run (optional)

> **save as `setup_and_run.sh`** and make it executable (`chmod +x setup_and_run.sh` on macOS/Linux).

```bash
#!/usr/bin/env bash
python -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
python train_model.py && \
streamlit run app.py
```

---

## ✅ Tech Stack

* **Python 3.10+**
* **Pandas**, **scikit‑learn**
* **Streamlit**
* **RandomForestRegressor**
* **GitHub + Streamlit Cloud**

---

## 🚧 Roadmap / Future Improvements

* Confidence intervals or prediction ranges
* Model‑explainability dashboard (SHAP)
* Switch to **XGBoost** or **LightGBM** for accuracy gains
* Auto‑populate match stats via live IPL API
* Feature‑importance visualizations

---

## 🙋‍♀️ About the Internship

This repository is part of **CubeNSquare’s Pallikoodam Data Science Internship**, focused on real‑world ML applications, hands‑on model building, and end‑to‑end deployment.

*Want to contribute?* Open an issue or contact the internship coordinator.

---

## 📃 License

Licensed under the **MIT License** – use, modify, and share responsibly.
