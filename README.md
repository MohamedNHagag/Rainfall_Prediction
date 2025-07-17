# 🌧 Rainfall Prediction using Machine Learning

## 📌 Project Overview
This project focuses on predicting whether it will **rain tomorrow** based on historical weather data using **Machine Learning classification models**.  
Accurate rainfall prediction is essential for agriculture, water resource management, and disaster prevention.

---

## ✅ Problem Statement
Given weather-related features (temperature, humidity, wind speed, pressure, etc.), predict the target variable **RainTomorrow** (Yes/No).

---

## 🛠 Steps Taken:
### 1️⃣ **Data Exploration**
- Loaded and explored the dataset to understand its structure.
- Checked for missing values and inconsistent data.

### 2️⃣ **Data Cleaning & Preprocessing**
- Handled missing values using imputation techniques.
- Encoded categorical features using **Label Encoding / One-Hot Encoding**.
- Scaled numerical features for better performance.

### 3️⃣ **Exploratory Data Analysis (EDA)**
- Analyzed correlations between weather features and rainfall occurrence.
- Visualized patterns using **Matplotlib** and **Seaborn** (heatmaps, bar plots).

### 4️⃣ **Feature Selection**
- Identified top features impacting rainfall:
  - Humidity3pm
  - Rainfall
  - Cloud3pm
  - Pressure9am

### 5️⃣ **Model Building**
- Applied multiple classification algorithms:
  - **Logistic Regression**
  - **Random Forest Classifier**
  - **Decision Tree Classifier**
- Evaluated models using:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-Score**

### 6️⃣ **Model Evaluation**
- Compared models and visualized results using a **Confusion Matrix**.

---

## 📈 Key Insights:
✔ High humidity and low pressure strongly correlate with rainfall chances.  
✔ Random Forest delivered the best overall accuracy among the tested models.

---

## 🛠 Tools & Technologies:
- **Python**
- **Libraries**: `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scikit-learn`
- **Jupyter Notebook** for development.

---
