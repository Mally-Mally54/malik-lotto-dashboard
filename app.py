
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Malik's Lotto Predictor", layout="centered")
st.title("🔢 Malik's Lucky Algorithm Dashboard")

st.markdown("""
Welcome to Malik's secret tool for analyzing and predicting lottery numbers.
This dashboard uses historical draw data to make data-driven predictions using machine learning.
""")

# Sidebar inputs
lotto_type = st.sidebar.selectbox("Choose Lottery Type", ["SA Lotto 6/52", "Powerball 5/50", "Mega Sena 6/60"])
total_numbers = st.sidebar.number_input("Total Numbers in Draw", min_value=10, max_value=100, value=52)
draw_size = st.sidebar.number_input("Numbers per Draw", min_value=3, max_value=10, value=6)

# File uploader
uploaded_file = st.file_uploader("Upload Historical Draws (CSV format)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'numbers' not in df.columns:
        st.error("CSV must contain a 'numbers' column with number lists like [1, 5, 10, 23, 33, 47]")
    else:
        df['numbers'] = df['numbers'].apply(lambda x: eval(x) if isinstance(x, str) else x)

        def create_feature_matrix(draws, total_numbers):
            feature_matrix = []
            for draw in draws:
                features = [1 if i in draw else 0 for i in range(1, total_numbers + 1)]
                feature_matrix.append(features)
            return np.array(feature_matrix)

        X = create_feature_matrix(df['numbers'], total_numbers)
        if len(X) < 2:
            st.warning("Need at least 2 draws to generate a prediction")
        else:
            X_train, y_train = X[:-1], X[1:]

            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            next_draw_prediction = model.predict([X[-1]])[0]
            predicted_numbers = [i+1 for i, val in enumerate(next_draw_prediction) if val == 1]

            st.subheader("📈 Predicted Next Draw")
            st.success(f"Predicted Numbers: {predicted_numbers}")

            st.markdown("""
            *Disclaimer: This prediction tool is for entertainment and analytical exploration. Lottery games are based on chance, and no method guarantees a win.*
            """)
else:
    st.info("Please upload a CSV file with past draw numbers.")
