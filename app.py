import streamlit as st
import pandas as pd

st.title("AI Crop Advisory System")

data = pd.read_csv("crop_data.csv")

st.sidebar.header("Farmer Input")

season = st.sidebar.selectbox("Season", data["Season"].unique())
soil = st.sidebar.selectbox("Soil Type", data["Soil_Type"].unique())
land = st.sidebar.number_input("Land (Acres)", 1.0)

filtered = data[(data["Season"] == season) & (data["Soil_Type"] == soil)]

if not filtered.empty:
    st.write("Recommended Crops:")
    st.dataframe(filtered)

    crop = filtered.iloc[0]

    cost = (crop["Seed_Cost"] + crop["Fertilizer_Cost"] + crop["Labor_Cost"]) * land
    revenue = (crop["Expected_Yield"] * crop["Market_Price"]) * land
    profit = revenue - cost

    st.write("Total Cost:", cost)
    st.write("Revenue:", revenue)
    st.write("Profit:", profit)

    st.write("Advice:")
    st.write(f"{crop['Crop']} is suitable. Risk: {crop['Common_Risks']}")
else:
    st.write("No crop found")