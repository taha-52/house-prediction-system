import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
MODEL_PATH = Path(__file__).parent / "house_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Predictor")
st.write("Enter the details of the house to estimate its price.")

st.subheader("🏡 Property Details")

area = st.number_input(
    "Area (sq ft)",
    min_value=100,
    max_value=50000,
    value=1000,
    step=100
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

parking = st.number_input(
    "Parking spaces",
    min_value=0,
    max_value=10,
    value=1,
    step=1
)

mainroad = st.selectbox(
    "Main Road Access",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

if st.button("🔮 Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    predicted_price = model.predict(input_data)[0]

    st.success(
        f"🏠 Estimated House Price: ₹{predicted_price:,.0f}"
    )
