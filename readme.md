# 🌍 Urban Heat Intelligence System

## 🚀 Overview

The **Urban Heat Intelligence System** is an AI-powered platform designed to monitor, analyze, and mitigate urban heat patterns in real time. It integrates **machine learning, geospatial visualization, and live weather data** to provide actionable insights for urban planning and environmental sustainability.

This system goes beyond basic analytics by offering:

* 🔮 Predictive forecasting
* 🔥 Heat risk detection
* 🌿 Intelligent mitigation strategies
* 📊 Explainable AI insights

---

## 🧠 Key Capabilities

* 📡 Real-time weather monitoring using OpenWeather API
* 🤖 Multi-model machine learning pipeline
* 🌍 Interactive geospatial visualization
* 📊 Explainable AI (SHAP-based insights)
* 🔮 Future temperature forecasting
* 🚨 High-risk heat alerts

---

## ✨ Features

### 📊 Dashboard

* KPI cards (temperature, humidity, wind)
* Heat distribution visualization
* High-risk zone alerts

### 🗺 Live Map

* Interactive map with heat zones
* Color-coded risk levels
* Heatmap visualization

### 📈 Zone Analysis

* Live vs predicted temperature
* Heat risk scoring
* 📊 AI-based explanation (SHAP)

### 🌿 Mitigation Module

* Simulates cooling strategies:

  * Urban forests 🌳
  * Cool roofs 🏠
  * Wind corridors 🌬
* Recommends best solution

### 🏆 Ranking System

* Ranks zones based on heat severity

### 📜 Historical Analysis

* Tracks past temperature trends
* Time-based visualization

### 🏗 Planning Module

* Simulates long-term urban interventions

### 🔮 Forecast Module

* Predicts next 3 hours temperature
* Trend visualization

### ➕ Add Location

* Add custom zones dynamically

---

## 🤖 Machine Learning Models

| Model          | Type           | Purpose                   |
| -------------- | -------------- | ------------------------- |
| XGBoost        | Regression     | Temperature prediction    |
| Random Forest  | Classification | Heatwave detection        |
| KMeans         | Clustering     | Hotspot identification    |
| Strategy Model | Classification | Mitigation recommendation |

---

## 🧮 Heat Risk Formula

```text
Heat Risk = 0.5 × Temperature + 0.3 × Humidity − 0.2 × Wind Speed
```

---

## 🏗 Project Architecture

```
Locations → Weather API → Database → Feature Engineering → ML Models → Dashboard
```

---

## 📁 Project Structure

```
.
├── .streamlit/
│   └── secrets.toml
├── pages
    └── index.html
├── notebooks/
    └── Urban_Heat_Mitigation (2).ipynb
├── utils/
│   ├── api.py
|   ├── features.py
|   ├── grid.py
│   ├── zone_analysis.py
│   ├── livemap.py
│   ├── mitigation.py
│   ├── ranking.py
│   ├── planning.py
│   └── history.py
├── db.py
├── app.py
├── xgb_model.pkl
├── heatwave_model.pkl
├── kmeans_model.pkl
├── strategy_model.pkl
├── label_encoder.pkl
├── urban_heat.db
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mohammedavez125/Urban_Heat_Mitigation_System
cd Urban_Heat_Mitigation_System
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Setup (OpenWeather)

### Step 1: Get API Key

* Visit: https://home.openweathermap.org/
* Generate API key

### Step 2: Add to Secrets

Create file:

```
.streamlit/secrets.toml
```

Add:

```toml
API_KEY = "your_api_key_here"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🗄 Database

* SQLite: `urban_heat.db`
* Auto-initialized via:

```python
from db import *
init_db()
```

---

## 📦 Dependencies

* streamlit
* pandas
* plotly
* folium
* scikit-learn
* xgboost
* shap
* joblib
* requests

---

## 🚀 Future Improvements

* 🌍 Satellite-based heat data integration
* 📱 Mobile application interface
* 🔔 Real-time alert notifications
* 📊 Power BI integration
* 🧠 AI chatbot for explanations
* ⏱ 24-hour forecasting

---

## 🧠 Key Highlights

✔ Real-time + predictive system
✔ Explainable AI integration
✔ Multi-model architecture
✔ Decision-support system

---

## 📜 License

Add your license (MIT recommended)
