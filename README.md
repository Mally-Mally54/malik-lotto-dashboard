
# Malik's Lucky Algorithm Dashboard 🎯

This is a Streamlit-based machine learning dashboard built to predict lottery numbers based on historical draw data.

## Features
- Upload CSVs of past lottery draws
- Uses Random Forest to detect patterns and make predictions
- Supports various lotteries (SA Lotto, Powerball, Mega Sena)

## How to Use
1. Upload a CSV file with one column named `numbers`, where each row contains a list like `[1, 4, 9, 23, 31, 44]`.
2. Select your lottery format and number size from the sidebar.
3. View your AI-powered prediction for the next draw!

## Files
- `app.py` – main app
- `requirements.txt` – Python package dependencies
- `lotto_data.csv` – example dataset

## Deploy to Streamlit Cloud
1. Fork or clone this repo
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub
4. Click 'New App' and select this repo
5. Set `app.py` as the main file and deploy!

> *Disclaimer: No system can guarantee lottery wins. This tool is for data analysis and educational fun.*
