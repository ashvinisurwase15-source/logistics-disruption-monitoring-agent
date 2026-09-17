import streamlit as st
import requests


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EV Battery Supply Chain Monitor",
    page_icon="🔋",
    layout="wide"
)


# --------------------------------------------------
# BACKEND CONFIGURATION
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000"


# --------------------------------------------------
# API FUNCTIONS
# --------------------------------------------------

def get_news():
    try:
        response = requests.get(
            f"{API_URL}/news",
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return []

    except requests.exceptions.RequestException:
        return []


def get_risks():
    try:
        response = requests.get(
            f"{API_URL}/risk",
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return []

    except requests.exceptions.RequestException:
        return []


def get_suppliers():
    try:
        response = requests.get(
            f"{API_URL}/supplier",
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return []

    except requests.exceptions.RequestException:
        return []


def get_recommendation():
    try:
        response = requests.get(
            f"{API_URL}/recommendation",
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


def get_sourcing(material="Lithium"):
    try:
        response = requests.get(
            f"{API_URL}/sourcing",
            params={"material": material},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

news = get_news()
risks = get_risks()
suppliers = get_suppliers()
recommendation = get_recommendation()
sourcing = get_sourcing("Lithium")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader("Autonomous Disruption Monitoring Agent")

st.write(
    "AI-powered monitoring system for detecting supply chain "
    "disruptions, assessing risk, identifying affected suppliers, "
    "and recommending mitigation strategies."
)

st.divider()


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

st.header("📊 Supply Chain Dashboard")

high_risk_count = sum(
    1
    for risk in risks
    if str(risk.get("severity", "")).lower() == "high"
)

active_disruptions = len(risks)

news_count = len(news)

supplier_count = len(suppliers)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "📰 News Events",
        news_count
    )


with col2:
    st.metric(
        "⚠️ Active Disruptions",
        active_disruptions
    )


with col3:
    st.metric(
        "🔴 High Risk Events",
        high_risk_count
    )


with col4:
    st.metric(
        "🏭 Affected Suppliers",
        supplier_count
    )


st.divider()


# --------------------------------------------------
# LATEST NEWS
# --------------------------------------------------

st.header("📰 Latest News Events")


if news:

    for article in news:

        with st.expander(
            article.get("title", "Unknown News")
        ):

            st.write(
                f"**Source:** "
                f"{article.get('source', 'Unknown')}"
            )

            st.write(
                f"**Published Date:** "
                f"{article.get('published_date', 'Unknown')}"
            )

            st.write(
                f"**Summary:** "
                f"{article.get('summary', 'No summary available.')}"
            )

            url = article.get("url")

            if url:
                st.link_button(
                    "Read Article",
                    url
                )

else:

    st.info("No news events available.")


st.divider()


# --------------------------------------------------
# RISK EVENTS
# --------------------------------------------------

st.header("⚠️ Risk Analysis")


if risks:

    for risk in risks:

        severity = risk.get(
            "severity",
            "Unknown"
        )

        title = risk.get(
            "title",
            "Unknown Risk"
        )

        with st.expander(
            f"{severity} - {title}"
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

    st.info("No risk events detected.")


st.divider()


# --------------------------------------------------
# RECOMMENDATION
# --------------------------------------------------

st.header("🤖 AI Recommended Action")


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
        "Recommendation service is unavailable."
    )


st.divider()


# --------------------------------------------------
# ALTERNATIVE SOURCING
# --------------------------------------------------

st.header("🔄 Alternative Sourcing")

if sourcing:

    material = sourcing.get(
        "material",
        "Unknown"
    )

    alternative_suppliers = sourcing.get(
        "alternative_suppliers",
        []
    )

    st.write(
        f"**Material:** {material}"
    )

    if alternative_suppliers:

        st.write(
            "**Alternative Suppliers:**"
        )

        for supplier in alternative_suppliers:

            st.success(
                f"🏭 {supplier}"
            )

    else:

        st.info(
            "No alternative suppliers found."
        )

else:

    st.warning(
        "Sourcing service is unavailable."
    )


st.divider()


# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.header("🟢 System Status")


try:

    health_response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if health_response.status_code == 200:

        st.success(
            "FastAPI Backend: Online"
        )

    else:

        st.error(
            "FastAPI Backend: Error"
        )

except requests.exceptions.RequestException:

    st.error(
        "FastAPI Backend: Offline"
    )