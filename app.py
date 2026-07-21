import pandas as pd
from sklearn.datasets import load_breast_cancer
import streamlit as st
from my_module.model import predict

# Page configuration
st.set_page_config(
    page_title="Breast Cancer Prediction NTI Task",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🧬",
)

st.header(":blue[Welcome to Breast Cancer Prediction NTI Task]")

st.write(
    "This Website is built using Streamlit & Scikit-Learn to analyze & visualize the Wisconsin Breast Cancer dataset to predict tumor classification"
)
st.write(
    "The dataset contains 30 numerical features computed from a digitized image of a fine needle aspirate of a breast mass."
)

# Load data
cancer = load_breast_cancer()
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df["target"] = cancer.target
df["target_name"] = df["target"].map({0: "malignant", 1: "benign"})

# Dataset preview buttons
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    if st.button("Show Breast Cancer Dataset", use_container_width=True):
        st.write("Here is the Breast Cancer dataset:")
        st.dataframe(df)

with col_btn2:
    if st.button("Show Dataset Summary", use_container_width=True):
        st.write("Here is the summary statistics of the dataset:")
        st.write(df.describe())

# Visualizations
st.header("Dataset Visualization")
tab1, tab2, tab3 = st.tabs(["Line Chart", "Scatter Chart", "Bar Chart"])

with tab1:
    st.line_chart(
        df, x="mean radius", y="mean texture", use_container_width=True
    )
with tab2:
    st.scatter_chart(
        df,
        x="mean radius",
        y="mean texture",
        color="target_name",
        use_container_width=True,
    )
with tab3:
    st.bar_chart(df, x="mean radius", y="mean area", use_container_width=True)

# Prediction Section
st.header("Tumor Classification Prediction")
st.write("Adjust the sliders below for all 30 features to test the model")

input_features = []
# Create 3 columns for a cleaner layout of the 30 sliders
cols = st.columns(3)

# Loop dynamically through all 30 features to create sliders
for i, feature_name in enumerate(cancer.feature_names):
    col = cols[i % 3]
    with col:
        min_val = float(df[feature_name].min())
        max_val = float(df[feature_name].max())
        mean_val = float(df[feature_name].mean())

        val = st.slider(
            label=feature_name.upper(),
            min_value=round(min_val, 2),
            max_value=round(max_val, 2),
            value=round(mean_val, 2),
            step=(max_val - min_val) / 100,
        )
        input_features.append(val)

st.divider()

# Predict Button
if st.button("Predict Tumor", type="primary", use_container_width=True):
    result = predict(input_features)
    if result == "malignant":
        st.error(f"The predicted tumor is **{result.upper()}** (Malignant)")
    else:
        st.success(
            f"The predicted tumor is **{result.upper()}** (Benign)"
        )