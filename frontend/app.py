import streamlit as st
import requests


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="EV Battery Supply Chain Monitor",
    page_icon="🔋",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader("Autonomous Disruption Monitoring Agent")

st.write(
    "AI-powered system for monitoring disruptions in the EV battery "
    "supply chain and supporting supply chain risk management."
)

st.divider()


# --------------------------------------------------
# Backend Configuration
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000"


# --------------------------------------------------
# Load Risk Data
# --------------------------------------------------

def get_risk_data():
    try:
        response = requests.get(
            f"{API_URL}/risk",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        return []

    except requests.exceptions.RequestException:
        return []


# --------------------------------------------------
# Load Recommendation
# --------------------------------------------------

def get_recommendation():
    try:
        response = requests.get(
            f"{API_URL}/recommendation",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

st.header("Supply Chain Dashboard")


risks = get_risk_data()
recommendation = get_recommendation()


# Make sure risk data is a list
if not isinstance(risks, list):
    risks = []


# --------------------------------------------------
# Metrics
# --------------------------------------------------

high_risk_count = sum(
    1
    for risk in risks
    if str(risk.get("severity", "")).lower() == "high"
)

affected_suppliers = len(risks)

active_disruptions = len(risks)


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        label="Active Disruptions",
        value=active_disruptions
    )


with col2:
    st.metric(
        label="High Risk Events",
        value=high_risk_count
    )


with col3:
    st.metric(
        label="Affected Suppliers",
        value=affected_suppliers
    )


st.divider()


# --------------------------------------------------
# Risk Events
# --------------------------------------------------

st.header("⚠️ Risk Events")


if risks:

    for risk in risks:

        with st.expander(
            f"{risk.get('severity', 'Unknown')} - "
            f"{risk.get('title', 'Unknown Risk')}"
        ):

            st.write(
                f"**Category:** "
                f"{risk.get('category', 'Unknown')}"
            )

            st.write(
                f"**Region:** "
                f"{risk.get('region', 'Unknown')}"
            )

            st.write(
                f"**Confidence:** "
                f"{risk.get('confidence', 0)}"
            )

            st.write(
                f"**Reason:** "
                f"{risk.get('reason', 'Not available')}"
            )

else:

    st.info(
        "No risk events available. "
        "Make sure the FastAPI backend is running."
    )


st.divider()


# --------------------------------------------------
# Recommendation
# --------------------------------------------------

st.header("🤖 Recommended Action")


if recommendation:

    recommendation_data = recommendation.get(
        "recommendation",
        {}
    )

    st.success(
        recommendation_data.get(
            "recommended_action",
            "No recommendation available."
        )
    )

    st.write(
        f"**Disruption Type:** "
        f"{recommendation_data.get('disruption_type', 'Unknown')}"
    )

    st.write(
        f"**Risk Level:** "
        f"{recommendation_data.get('risk_level', 'Unknown')}"
    )

else:

    st.warning(
        "Recommendation service is currently unavailable."
    )