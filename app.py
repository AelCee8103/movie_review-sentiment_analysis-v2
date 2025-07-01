import streamlit as st
import joblib
from sklearn.linear_model import LogisticRegression

# Dictionary of model names and their file paths
model_files = {
    "Logistic Regression": "logistic_regression_best.pkl",
    "Passive Aggressive": "passive_aggressive.pkl",
    "Random Forest": "random_forest.pkl",
    "Linear SVC": "linear_svc_model.pkl",
    "XGBoost": "XGBoost.pkl"
}

# Load vectorizer once
tfidf = joblib.load('tfidf_vectorizer.pkl')

st.title("Movie Sentiment Analysis")

# Dropdown for model selection
model_name = st.selectbox(
    "Choose a model:",
    options=list(model_files.keys()),
    index=0  # Default to Logistic Regression
)

if model_name == "Logistic Regression":
    # Load best params and model
    best_params = joblib.load('logistic_regression_best_params.pkl')
    model = joblib.load(model_files[model_name])
    # Optionally, re-instantiate LogisticRegression with best_params if needed:
    # model = LogisticRegression(**best_params)
    # model.coef_ = loaded_model.coef_
    # model.intercept_ = loaded_model.intercept_
else:
    model = joblib.load(model_files[model_name])

review = st.text_area("Enter a review:")
if st.button("Predict"):
    vector = tfidf.transform([review])
    prediction = model.predict(vector)[0]
    if prediction == 1:
        st.markdown(
            "<div style='background-color:rgba(185,251,192,0.7);padding:20px;border-radius:8px;text-align:center;'><span style='color:#000;font-size:20px;'>Positive</span></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:rgba(255,77,77,0.7);padding:20px;border-radius:8px;text-align:center;'><span style='color:#000;font-size:20px;'>Negative</span></div>",
            unsafe_allow_html=True
        )
