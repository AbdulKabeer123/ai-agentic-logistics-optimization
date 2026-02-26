import os
from dotenv import load_dotenv
load_dotenv()  # Must be first

import streamlit as st
from services.multi_vehicle import Vehicle, Fleet
from services.groq_agent import agent_decision
import pandas as pd
import time

st.set_page_config(page_title="🚚 AI Agentic Logistics Dashboard", layout="wide")
st.title("🚚 AI Agentic Logistics Dashboard")
st.subheader("Real-Time ETA & Freshness Scores")

# --- Initialize Fleet ---
if "fleet" not in st.session_state:
    vehicles = [
        Vehicle("V1", (24.8607, 67.0011), (24.8138, 67.0330)),
        Vehicle("V2", (24.8607, 67.0011), (24.8000, 67.0500)),
        Vehicle("V3", (24.8607, 67.0011), (24.8200, 67.0200))
    ]
    st.session_state.fleet = Fleet(vehicles)
    st.session_state.last_update = 0

fleet = st.session_state.fleet
refresh_rate = 15  # seconds

# --- Update fleet (button or auto-refresh) ---
if st.button("Update Status") or (time.time() - st.session_state.last_update >= refresh_rate):
    fleet.update_all()
    st.session_state.last_update = time.time()

# --- Prepare Data ---
rows = []
for v in fleet.vehicles:
    rows.append({
        "Vehicle": v.id,
        "ETA (min)": v.eta,
        "Weather": v.weather,
        "Freshness (%)": v.freshness,
        "Urban Event": v.urban_event
    })

df = pd.DataFrame(rows)

# --- Groq AI Suggestion ---
groq_suggestion = agent_decision(rows)
st.markdown("### 🤖 Groq Agent Suggestion")
st.write(groq_suggestion)

# --- Highlight Best Vehicle ---
best = fleet.best_vehicle()
st.markdown(f"### ✅ Best Vehicle: {best.id}")

# --- Color-coded Freshness Table ---
def color_freshness(val):
    if val >= 80:
        return "background-color: #8BC34A"  # green
    elif val >= 50:
        return "background-color: #FFEB3B"  # yellow
    else:
        return "background-color: #F44336; color:white"  # red

st.dataframe(df.style.map(color_freshness, subset=["Freshness (%)"]))