#streamlit_app.py
import streamlit as st
import pandas as pd

st.title("Earthquake Forecast Dashboard")

# 1. Current earthquake map
st.subheader("Recent Earthquakes (Indonesia)")
map_data = pd.DataFrame({
    'lat': df['latitude'],
    'lon': df['longitude']
})
st.map(map_data)  # shows scatter on map

# 2. Forecast hotspots
st.subheader("Forecasted Hotspots")
# (Placeholder: one could overlay DBSCAN zones with risk levels)
st.write("Hotspot map coming soon...")

# 3. Gauges for large-event risk
st.subheader("Large-Event Probability")
import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prob_large*100,
    title={'text': "Prob M≥5 in 7 days (%)"},
    gauge={'axis': {'range': [None, 100]}}
))
st.plotly_chart(fig)

st.write("Transformer prediction: Mag ~5.2, uncertainty ±0.5, zone: 3")