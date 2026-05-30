import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("Car Price Prediction App")

# Inputs
make = st.text_input("Make", "Toyota")

model_name = st.text_input(
    "Model",
    "Corolla"
)

type_car = st.selectbox(
    "Type",
    ["Sedan", "SUV", "Sports"]
)

origin = st.selectbox(
    "Origin",
    ["Asia", "USA", "Europe"]
)

drivetrain = st.selectbox(
    "DriveTrain",
    ["Front", "Rear", "All"]
)

engine_size = st.number_input(
    "Engine Size",
    1.0,
    10.0,
    2.0
)

cylinders = st.number_input(
    "Cylinders",
    2,
    12,
    4
)

horsepower = st.number_input(
    "Horsepower",
    50,
    1000,
    150
)

mpg_city = st.number_input(
    "MPG City",
    5,
    100,
    20
)

mpg_highway = st.number_input(
    "MPG Highway",
    5,
    100,
    30
)

weight = st.number_input(
    "Weight",
    1000,
    6000,
    3000
)

wheelbase = st.number_input(
    "Wheelbase",
    50,
    200,
    100
)

length = st.number_input(
    "Length",
    100,
    300,
    180
)

invoice = st.number_input(
    "Invoice",
    1000,
    100000,
    20000
)

# Prediction
if st.button("Predict MSRP"):

    input_df = pd.DataFrame([{
        'Make': make,
        'Model': model_name,
        'Type': type_car,
        'Origin': origin,
        'DriveTrain': drivetrain,
        'Invoice': invoice,
        'EngineSize': engine_size,
        'Cylinders': cylinders,
        'Horsepower': horsepower,
        'MPG_City': mpg_city,
        'MPG_Highway': mpg_highway,
        'Weight': weight,
        'Wheelbase': wheelbase,
        'Length': length
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted MSRP: ${prediction:,.2f}")
