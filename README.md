# 🧬 Breast Cancer Diagnostic & Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYMENT_LINK_HERE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

An interactive web application built with **Streamlit** and **Scikit-Learn** that analyzes, visualizes, and classifies tumor features from the Wisconsin Breast Cancer dataset as either **Benign (حميد)** or **Malignant (خبيث)** using Machine Learning.

---

## 🌐 Live Demo

👉 **[Click here to try the Live Application](YOUR_DEPLOYMENT_LINK_HERE)** 👈
*(Note: Replace YOUR_DEPLOYMENT_LINK_HERE with your Streamlit Community Cloud URL)*

---

## ✨ Features

- **📊 Interactive Data Exploration:** View the full dataset, inspect statistical summaries, and explore feature distributions.
- **📈 Dynamic Visualizations:** Includes built-in Line Charts, Scatter Charts (colored by tumor class), and Bar Charts to analyze relationships between cellular features.
- **🎛️ 30-Feature Custom Sliders:** Intuitively organized in a 3-column responsive layout, allowing users to tweak every cellular parameter (e.g., mean radius, mean texture, perimeter, area, smoothness, etc.).
- **⚡ Real-time Prediction:** Uses a trained **Decision Tree Classifier** to instantly classify the tumor based on user input with visual alert indicators.

---

## 🛠️ Tech Stack

- **Frontend & UI:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (DecisionTreeClassifier)
- **Data Manipulation & Math:** Pandas, NumPy

---

## 📁 Project Structure

```text
my_project/
├── app.py # Main Streamlit UI and dashboard logic
├── requirements.txt # Project dependencies for deployment
├── README.md # Project documentation
└── my_module/
    ├── __init__.py # Package initializer
    └── model.py # Machine learning model loading, training, and prediction logic
```

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

---

## 📚 About the Dataset

This application utilizes the classic **Wisconsin Breast Cancer Diagnostic Dataset** loaded directly via Scikit-Learn (`load_breast_cancer`). 
- **Number of Instances:** 569
- **Number of Attributes:** 30 numeric, predictive attributes and the class
- **Target Classes:** 
  - `0` : **Malignant** (Malignant - Cancerous tumor)
  - `1` : **Benign** (Benign - Non-cancerous tumor)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/alfarouq637/breast_cancer_dataset_streamlit_task/issues).

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
