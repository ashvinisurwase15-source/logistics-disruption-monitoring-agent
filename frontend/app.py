import streamlit as st

# Page configuration
st.set_page_config(
    page_title="EV Battery Supply Chain Monitor",
    page_icon="🔋",
    layout="wide"
)

# Title
st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader("Autonomous Disruption Monitoring Agent")

st.write(
    "AI-powered system for monitoring disruptions in the EV battery "
    "supply chain and supporting supply chain risk management."
)

st.divider()

# Dashboard overview
st.header("Supply Chain Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Active Disruptions", "0")

with col2:
    st.metric("High Risk Events", "0")

with col3:
    st.metric("Affected Suppliers", "0")

st.divider()

st.info(
    "Monitoring system initialized. Supply chain intelligence "
    "will appear here as monitoring agents are added."
)