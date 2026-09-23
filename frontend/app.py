import streamlit as st
import requests


st.set_page_config(
    page_title="EV Battery Supply Chain Monitor",
    page_icon="🔋",
    layout="wide"
)


API_URL = "http://127.0.0.1:8000"


def get_api_data(endpoint):
    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=30
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


# --------------------------------------------------
# API DATA
# --------------------------------------------------

news_data = get_api_data("/news")
risk_data = get_api_data("/risk")
supplier_data = get_api_data("/supplier")
recommendation_data = get_api_data("/recommendation")
sourcing_data = get_api_data("/sourcing?material=Lithium")
orchestrator_data = get_api_data("/orchestrator")


# --------------------------------------------------
# DATA VALIDATION
# --------------------------------------------------

if not isinstance(news_data, list):
    news_data = []

if not isinstance(risk_data, list):
    risk_data = []

if not isinstance(supplier_data, list):
    supplier_data = []

if not isinstance(orchestrator_data, dict):
    orchestrator_data = {}

impacts_data = orchestrator_data.get("impacts", [])

if not isinstance(impacts_data, list):
    impacts_data = []


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader("Autonomous Disruption Monitoring Agent")

st.write(
    "AI-powered monitoring system for detecting supply chain "
    "disruptions, assessing risk, identifying affected suppliers, "
    "analyzing business impact, and recommending mitigation strategies."
)

st.divider()


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

st.header("📊 Supply Chain Dashboard")


high_risk_count = sum(
    1
    for risk in risk_data
    if str(risk.get("severity", "")).lower() == "high"
)


active_disruptions = len(risk_data)
news_count = len(news_data)
supplier_count = len(supplier_data)


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


if news_data:

    for article in news_data:

        with st.expander(
            article.get(
                "title",
                "Unknown News"
            )
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
# RISK ANALYSIS
# --------------------------------------------------

st.header("⚠️ Risk Analysis")


if risk_data:

    for risk in risk_data:

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
# BUSINESS IMPACT ANALYSIS
# --------------------------------------------------

st.header("📊 Business Impact Analysis")


if impacts_data:

    for index, impact in enumerate(
        impacts_data,
        start=1
    ):

        disruption_type = impact.get(
            "disruption_type",
            "Unknown"
        )

        material = impact.get(
            "material",
            "Unknown"
        )

        priority = impact.get(
            "priority",
            "Unknown"
        )

        with st.expander(
            f"Impact Event {index} - {disruption_type}"
        ):

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Production Impact",
                    impact.get(
                        "production_impact",
                        "Unknown"
                    )
                )

            with col2:
                st.metric(
                    "Shortage Risk",
                    impact.get(
                        "shortage_risk",
                        "Unknown"
                    )
                )

            with col3:
                st.metric(
                    "Cost Impact",
                    impact.get(
                        "cost_impact",
                        "Unknown"
                    )
                )

            with col4:
                st.metric(
                    "Priority",
                    priority
                )

            st.write(
                f"**Material:** {material}"
            )

            st.write(
                f"**Risk Level:** "
                f"{impact.get('risk_level', 'Unknown')}"
            )

            st.write(
                f"**Business Impact:** "
                f"{impact.get('business_impact', 'Not available')}"
            )

else:

    st.info(
        "No business impact analysis available."
    )


st.divider()


# --------------------------------------------------
# AI RECOMMENDED ACTION
# --------------------------------------------------

st.header("🤖 AI Recommended Action")


if recommendation_data:

    recommendation_data_inner = (
        recommendation_data.get(
            "recommendation",
            {}
        )
    )

    st.success(
        recommendation_data_inner.get(
            "recommended_action",
            "No recommendation available."
        )
    )

    st.write(
        f"**Disruption Type:** "
        f"{recommendation_data_inner.get(
            'disruption_type',
            'Unknown'
        )}"
    )

    st.write(
        f"**Risk Level:** "
        f"{recommendation_data_inner.get(
            'risk_level',
            'Unknown'
        )}"
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


if sourcing_data:

    material = sourcing_data.get(
        "material",
        "Unknown"
    )

    alternative_suppliers = sourcing_data.get(
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
# MULTI-AGENT SYSTEM SUMMARY
# --------------------------------------------------

st.header("🔄 Multi-Agent System")


if orchestrator_data:

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "News",
            orchestrator_data.get(
                "news_count",
                0
            )
        )

    with col2:
        st.metric(
            "Risks",
            orchestrator_data.get(
                "risk_count",
                0
            )
        )

    with col3:
        st.metric(
            "Suppliers",
            orchestrator_data.get(
                "supplier_count",
                0
            )
        )

    with col4:
        st.metric(
            "Impacts",
            orchestrator_data.get(
                "impact_count",
                0
            )
        )

    with col5:
        st.metric(
            "Recommendations",
            orchestrator_data.get(
                "recommendation_count",
                0
            )
        )

else:

    st.warning(
        "Orchestrator service is unavailable."
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