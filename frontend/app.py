import streamlit as st
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EV Battery Supply Chain Monitor",
    page_icon="🔋",
    layout="wide"
)


# ============================================================
# FASTAPI CONFIGURATION
# ============================================================

API_URL = "http://127.0.0.1:8000"


# ============================================================
# API HELPER
# ============================================================

def get_api_data(endpoint):
    """
    Send GET request to FastAPI backend.
    """

    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=15
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None


# ============================================================
# LOAD DATA FROM FASTAPI
# ============================================================

news_data = get_api_data("/news")
risk_data = get_api_data("/risk")
supplier_data = get_api_data("/supplier")
recommendation_data = get_api_data("/recommendation")
orchestrator_data = get_api_data("/orchestrator")
health_data = get_api_data("/health")


# ============================================================
# SAFETY CHECKS
# ============================================================

if not isinstance(news_data, list):
    news_data = []

if not isinstance(risk_data, list):
    risk_data = []

if not isinstance(supplier_data, list):
    supplier_data = []


# ============================================================
# TITLE
# ============================================================

st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader(
    "Autonomous Disruption Monitoring Agent"
)

st.write(
    "AI-powered multi-agent system for monitoring "
    "disruptions across the EV battery supply chain."
)

st.divider()


# ============================================================
# DASHBOARD
# ============================================================

st.header("📊 Supply Chain Dashboard")


# ------------------------------------------------------------
# Metrics
# ------------------------------------------------------------

news_count = len(news_data)

active_disruptions = len(risk_data)

high_risk_events = sum(
    1
    for risk in risk_data
    if str(risk.get("severity", "")).lower() == "high"
)

affected_suppliers = len(supplier_data)


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
        high_risk_events
    )


with col4:
    st.metric(
        "🏭 Affected Suppliers",
        affected_suppliers
    )


st.divider()


# ============================================================
# NEWS EVENTS
# ============================================================

st.header("📰 Latest News Events")


if news_data:

    for article in news_data:

        title = article.get(
            "title",
            "Unknown News Event"
        )

        source = article.get(
            "source",
            "Unknown Source"
        )

        summary = article.get(
            "summary",
            "No summary available."
        )

        url = article.get(
            "url",
            ""
        )

        published_date = article.get(
            "published_date",
            None
        )

        with st.expander(title):

            st.write(
                f"**Source:** {source}"
            )

            if published_date:
                st.write(
                    f"**Published:** {published_date}"
                )

            st.write(
                f"**Summary:** {summary}"
            )

            if url:
                st.markdown(
                    f"[🔗 Read Source]({url})"
                )

else:

    st.info(
        "No news events available."
    )


st.divider()


# ============================================================
# RISK EVENTS
# ============================================================

st.header("⚠️ Risk Events")


if risk_data:

    for risk in risk_data:

        title = risk.get(
            "title",
            "Unknown Risk"
        )

        severity = risk.get(
            "severity",
            "Unknown"
        )

        category = risk.get(
            "category",
            "Unknown"
        )

        region = risk.get(
            "region",
            "Unknown"
        )

        confidence = risk.get(
            "confidence",
            0
        )

        reason = risk.get(
            "reason",
            "No reason available."
        )

        with st.expander(
            f"{severity} - {title}"
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Category:** {category}"
                )

                st.write(
                    f"**Region:** {region}"
                )

            with col2:

                st.write(
                    f"**Severity:** {severity}"
                )

                st.write(
                    f"**Confidence:** {confidence}"
                )

            st.write(
                f"**Reason:** {reason}"
            )

else:

    st.info(
        "No risk events detected."
    )


st.divider()


# ============================================================
# SUPPLIER IMPACT
# ============================================================

st.header("🏭 Supplier Impact")


if supplier_data:

    for supplier in supplier_data:

        supplier_name = supplier.get(
            "supplier",
            "Unknown"
        )

        material = supplier.get(
            "material",
            "Unknown"
        )

        region = supplier.get(
            "region",
            "Unknown"
        )

        impact_level = supplier.get(
            "impact_level",
            "Unknown"
        )

        reason = supplier.get(
            "reason",
            "No reason available."
        )

        with st.expander(
            f"{impact_level} Impact - {supplier_name}"
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Supplier:** {supplier_name}"
                )

                st.write(
                    f"**Material:** {material}"
                )

            with col2:

                st.write(
                    f"**Region:** {region}"
                )

                st.write(
                    f"**Impact Level:** {impact_level}"
                )

            st.write(
                f"**Reason:** {reason}"
            )

else:

    st.info(
        "No supplier impact data available."
    )


st.divider()


# ============================================================
# AI MITIGATION RECOMMENDATIONS
# ============================================================

st.header("🤖 AI Mitigation Recommendations")


if recommendation_data:

    # Handle nested recommendation response
    if isinstance(recommendation_data, dict):

        recommendation = recommendation_data.get(
            "recommendation"
        )

        related_risk = recommendation_data.get(
            "risk"
        )

        if recommendation:

            recommended_action = recommendation.get(
                "recommended_action",
                "No recommendation available."
            )

            disruption_type = recommendation.get(
                "disruption_type",
                "Unknown"
            )

            risk_level = recommendation.get(
                "risk_level",
                "Unknown"
            )

            st.success(
                recommended_action
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Disruption Type:** "
                    f"{disruption_type}"
                )

            with col2:

                st.write(
                    f"**Risk Level:** "
                    f"{risk_level}"
                )

            if related_risk:

                st.subheader(
                    "Related Risk"
                )

                st.write(
                    f"**Risk Event:** "
                    f"{related_risk.get('title', 'Unknown')}"
                )

                st.write(
                    f"**Severity:** "
                    f"{related_risk.get('severity', 'Unknown')}"
                )

                st.write(
                    f"**Confidence:** "
                    f"{related_risk.get('confidence', 0)}"
                )

        else:

            st.info(
                "No mitigation recommendations available."
            )

    else:

        st.info(
            "No mitigation recommendations available."
        )

else:

    st.info(
        "No mitigation recommendations available."
    )


st.divider()


# ============================================================
# MULTI-AGENT ORCHESTRATOR
# ============================================================

st.header("🔄 Multi-Agent Orchestrator")


if orchestrator_data:

    if isinstance(orchestrator_data, dict):

        # ----------------------------------------------------
        # Orchestrator Metrics
        # ----------------------------------------------------

        orch_news_count = orchestrator_data.get(
            "news_count",
            0
        )

        orch_risk_count = orchestrator_data.get(
            "risk_count",
            0
        )

        orch_supplier_count = orchestrator_data.get(
            "supplier_count",
            0
        )

        orch_recommendation_count = orchestrator_data.get(
            "recommendation_count",
            0
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "News",
                orch_news_count
            )

        with col2:

            st.metric(
                "Risks",
                orch_risk_count
            )

        with col3:

            st.metric(
                "Suppliers",
                orch_supplier_count
            )

        with col4:

            st.metric(
                "Recommendations",
                orch_recommendation_count
            )

        st.success(
            "Multi-Agent Orchestrator is running successfully."
        )

        # ----------------------------------------------------
        # Orchestrator Risks
        # ----------------------------------------------------

        orchestrator_risks = orchestrator_data.get(
            "risks",
            []
        )

        if orchestrator_risks:

            st.subheader(
                "Detected Risks"
            )

            for risk in orchestrator_risks:

                if isinstance(risk, dict):

                    st.write(
                        f"**{risk.get('severity', 'Unknown')}** - "
                        f"{risk.get('title', 'Unknown Risk')}"
                    )

        # ----------------------------------------------------
        # Orchestrator Recommendations
        # ----------------------------------------------------

        orchestrator_recommendations = (
            orchestrator_data.get(
                "recommendations",
                []
            )
        )

        if orchestrator_recommendations:

            st.subheader(
                "Generated Recommendations"
            )

            for rec in orchestrator_recommendations:

                if isinstance(rec, dict):

                    st.write(
                        rec.get(
                            "recommended_action",
                            "No action available."
                        )
                    )

    else:

        st.warning(
            "Unexpected orchestrator response."
        )

else:

    st.error(
        "Orchestrator is currently unavailable."
    )


st.divider()


# ============================================================
# SYSTEM STATUS
# ============================================================

st.header("🟢 System Status")


col1, col2 = st.columns(2)


with col1:

    if health_data:

        st.success(
            "FastAPI Backend: Connected"
        )

    else:

        st.error(
            "FastAPI Backend: Disconnected"
        )


with col2:

    if orchestrator_data:

        st.success(
            "Orchestrator: Online"
        )

    else:

        st.error(
            "Orchestrator: No Data"
        )


st.divider()


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "EV Battery Supply Chain Monitor | "
    "AI-powered Autonomous Disruption Monitoring System"
)
st.divider()

# --------------------------------------------------
# Supply Chain Knowledge Graph
# --------------------------------------------------

st.header("🔗 Supply Chain Knowledge Graph")

try:
    graph_response = requests.get(
        f"{API_URL}/graph",
        timeout=10
    )

    if graph_response.status_code == 200:

        graph_data = graph_response.json()
        graph_path = graph_data.get("graph_path")

        if graph_path:

            import os

            if os.path.exists(graph_path):
                st.image(
                    graph_path,
                    caption="EV Battery Supply Chain Knowledge Graph",
                    use_container_width=True
                )
            else:
                st.warning("Knowledge graph image was not found.")

        else:
            st.warning("Graph path was not returned by the API.")

    else:
        st.error("Knowledge Graph API returned an error.")

except requests.exceptions.RequestException:
    st.warning("Knowledge Graph service is currently unavailable.")