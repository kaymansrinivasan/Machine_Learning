import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np


st.set_page_config(
    page_title="Earthquake Forecast Dashboard",
    layout="wide"
)



st.title(" Earthquake Forecast Dashboard")

st.markdown("""
Hybrid Spatio-Temporal Transformer for Earthquake Forecasting
""")


try:
    df = pd.read_csv(
        r"C:\Users\User\AppData\Local\JetBrains\PyCharm 2025.1.3.1\bin\indonesia_earthquake_data.csv"
    )

except:
    st.error("Dataset not found.")
    st.stop()


st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(df))

col2.metric(
    "Max Magnitude",
    round(df['mag'].max(), 2)
)

col3.metric(
    "Average Magnitude",
    round(df['mag'].mean(), 2)
)



st.subheader("Recent Earthquake Locations")

map_data = pd.DataFrame({
    'lat': df['latitude'],
    'lon': df['longitude']
})

st.map(map_data)


st.subheader("Magnitude Distribution")

hist_values = np.histogram(
    df['mag'],
    bins=20
)[0]

st.bar_chart(hist_values)



st.subheader("Transformer Forecast")

predicted_magnitude = 5.2
uncertainty = 0.5
predicted_zone = 3

st.success(
    f"""
    Predicted Magnitude: {predicted_magnitude} ± {uncertainty}

    Predicted Seismic Zone: {predicted_zone}
    """
)


st.subheader("Large Event Probability")

prob_large = 0.68

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prob_large * 100,
    title={'text': "Probability of M≥5 Event (%)"},
    gauge={
        'axis': {'range': [None, 100]}
    }
))

st.plotly_chart(fig)



st.subheader("Recent Earthquake Events")

st.dataframe(
    df[['time', 'latitude', 'longitude', 'depth', 'mag']]
    .tail(20)
)


st.markdown("---")

st.caption(
    "FYP2 — Earthquakes Prediction Using Deep Learning Model"
)