import streamlit as st
import numpy as np
import joblib


st.set_page_config(page_title="Engine PdM Dashboard", page_icon="⚙️", layout = "wide")
st.title("⚙️ Engine Predictive Maintenance & Lifespan Dashboard")
st.write("Enterprise infrastructure tool to evaluate Remaining Useful Life (RUL) via live asset sensor telemetry streams.")
st.markdown("---")

try:
    model = joblib.load('engine_model.pkl')
except FileNotFoundError:
    st.error("⚠️ 'engine_model.pkl' not found! Please place the downloaded model file in this directory.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    st.subheader("📊 Live Sensor Telemetry Input")
    current_cycle = st.slider("Current Operational Cycle", 1, 250, 45)
    sensor_2 = st.slider("Sensor 2 (Core Temp)", 640.0, 650.0, 642.0)
    sensor_3 = st.slider("Sensor 3 (LPT Speed)", 1570.0, 1600.0, 1585.0)
    sensor_4 = st.slider("Sensor 4 (HPC Speed)", 1390.0, 1430.0, 1405.0)
    sensor_7 = st.slider("Sensor 7 (HPT Ratio)", 550.0, 560.0, 553.0)
    sensor_11 = st.slider("Sensor 11 (Actuator Position)", 46.0, 48.0, 47.0)
    sensor_12 = st.slider("Sensor 12 (Fan Speed Ratio)", 520.0, 530.0, 521.0)
    sensor_15 = st.slider("Sensor 15 (Bypass Ratio)", 8.3, 8.6, 8.4)
    sensor_20 = st.slider("Sensor 20 (Bleed Enthalpy)", 38.5, 40.0, 39.0)
    sensor_21 = st.slider("Sensor 21 (Vibration Index)", 23.0, 24.5, 23.3)


with col2:
    st.subheader("💡 Predictive Maintenance Assesment")

    input_features = np.array([[current_cycle, sensor_2, sensor_3, sensor_4, sensor_7,sensor_11, sensor_12, sensor_15, sensor_20, sensor_21]])
    predicted_rul = max(0, float(model.predict(input_features)))
    total_life = current_cycle + predicted_rul
    life_consumed = (current_cycle / total_life) * 100 if total_life > 0 else 100

    m1, m2 = st.columns(2)
    m1.metric("Predicted Remaining Life", f"{int(predicted_rul)} Cycles")
    m2.metric("Lifespan Consumed", f"{life_consumed:.1f}%")

    if predicted_rul > 60:
        st.success("🟢 Status: Nominal. Normal asset operations authorized.")
    elif 25 <= predicted_rul <= 60:
        st.warning("🟡 Status: Advisory. Schedule preventative maintenance flag within next 20 cycles.")
    else:
        st.error("🔴 CRITICAL: Extreme deterioration risk. Immediate structural intervention required.")