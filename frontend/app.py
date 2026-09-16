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
# TITLE
# ============================================================

st.title("🔋 EV Battery Supply Chain Monitor")

st.subheader("Autonomous Disruption Monitoring Agent")

st.write(
    "AI-powered system for monitoring disruptions in the EV battery "
    "supply chain and supporting supply chain risk management."
)

st.divider()


# ============================================================
# BACKEND CONFIGURATION
# ============================================================

API_URL = "http://127.0.0.1:8000"


# ============================================================
# GENERIC API GET FUNCTION
# ============================================================

def api_get(endpoint, timeout=10):
    """
    Send a GET request to the FastAPI backend.
    """

    try:

        response = requests.get(
            f"{API_URL}{endpoint}",
            timeout=timeout
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:

        return None


# ============================================================
# LOAD NEWS
# ============================================================

def get_news():
    """
    Get news events from FastAPI.
    """

    data = api_get(
        "/news",
        timeout=15
    )

    if isinstance(data, list):
        return data

    return []


# ============================================================
# LOAD RISK DATA
# ============================================================

def get_risk_data():
    """
    Get risk analysis results from FastAPI.
    """

    data = api_get(
        "/risk",
        timeout=15
    )

    if isinstance(data, list):
        return data

    return []


# ============================================================
# LOAD RECOMMENDATION
# ============================================================

def get_recommendation():
    """
    Get recommendation from FastAPI.

    Recommendation may take longer because it runs
    through the risk and recommendation agents.
    """

    data = api_get(
        "/recommendation",
        timeout=30
    )

    if isinstance(data, dict):
        return data

    return None


# ============================================================
# CHECK FASTAPI BACKEND
# ============================================================

def check_backend():
    """
    Check whether FastAPI backend is running.
    """

    try:

        response = requests.get(
            f"{API_URL}/docs",
            timeout=5
        )

        return response.status_code == 200

    except requests.exceptions.RequestException:

        return False


# ============================================================
# CHECK ORCHESTRATOR
# ============================================================

def check_orchestrator():
    """
    Check whether the orchestrator endpoint is working.
    """

    data = api_get(
        "/orchestrator",
        timeout=15
    )

    return data


# ============================================================
# LOAD DATA
# ============================================================

news = get_news()

risks = get_risk_data()

recommendation = get_recommendation()

orchestrator_data = check_orchestrator()


# ============================================================
# VALIDATE DATA
# ============================================================

if not isinstance(news, list):

    news = []


if not isinstance(risks, list):

    risks = []


# ============================================================
# SUPPLY CHAIN DASHBOARD
# ============================================================

st.header("📊 Supply Chain Dashboard")


# ============================================================
# CALCULATE METRICS
# ============================================================

active_disruptions = len(risks)


high_risk_count = sum(
    1
    for risk in risks
    if str(
        risk.get("severity", "")
    ).lower() == "high"
)


# ============================================================
# AFFECTED SUPPLIERS
# ============================================================

supplier_names = set()


for risk in risks:

    supplier = risk.get("supplier")

    if supplier:

        supplier_names.add(
            str(supplier)
        )


if supplier_names:

    affected_suppliers = len(
        supplier_names
    )

else:

    affected_suppliers = len(risks)


# ============================================================
# DISPLAY DASHBOARD METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        label="📰 News Events",
        value=len(news)
    )


with col2:

    st.metric(
        label="⚠️ Active Disruptions",
        value=active_disruptions
    )


with col3:

    st.metric(
        label="🔴 High Risk Events",
        value=high_risk_count
    )


with col4:

    st.metric(
        label="🏭 Affected Suppliers",
        value=affected_suppliers
    )


st.divider()


# ============================================================
# RISK EVENTS
# ============================================================

st.header("⚠️ Risk Events")


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

        # ----------------------------------------------------
        # Severity icon
        # ----------------------------------------------------

        severity_lower = str(
            severity
        ).lower()


        if severity_lower == "high":

            icon = "🔴"

        elif severity_lower == "medium":

            icon = "🟠"

        elif severity_lower == "low":

            icon = "🟢"

        else:

            icon = "⚪"


        # ----------------------------------------------------
        # Risk Expander
        # ----------------------------------------------------

        with st.expander(
            f"{icon} {severity} — {title}"
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


            # ------------------------------------------------
            # Optional supplier information
            # ------------------------------------------------

            if risk.get("supplier"):

                st.write(
                    f"**Supplier:** "
                    f"{risk.get('supplier')}"
                )


            # ------------------------------------------------
            # Optional source information
            # ------------------------------------------------

            if risk.get("source"):

                st.write(
                    f"**Source:** "
                    f"{risk.get('source')}"
                )


            if risk.get("url"):

                st.write(
                    f"**Source URL:** "
                    f"{risk.get('url')}"
                )


else:

    st.info(
        "No risk events available. "
        "Make sure the FastAPI backend is running."
    )


st.divider()


# ============================================================
# RECOMMENDED ACTION
# ============================================================

st.header("🤖 Recommended Action")


if recommendation:

    # --------------------------------------------------------
    # Extract recommendation
    # --------------------------------------------------------

    recommendation_data = recommendation.get(
        "recommendation",
        {}
    )


    # --------------------------------------------------------
    # Validate recommendation
    # --------------------------------------------------------

    if not isinstance(
        recommendation_data,
        dict
    ):

        recommendation_data = {}


    # --------------------------------------------------------
    # Recommended action
    # --------------------------------------------------------

    recommended_action = recommendation_data.get(
        "recommended_action",
        "No recommendation available."
    )


    st.success(
        recommended_action
    )


    # --------------------------------------------------------
    # Recommendation details
    # --------------------------------------------------------

    recommendation_col1, recommendation_col2 = st.columns(2)


    with recommendation_col1:

        st.write(
            f"**Disruption Type:** "
            f"{recommendation_data.get('disruption_type', 'Unknown')}"
        )


    with recommendation_col2:

        st.write(
            f"**Risk Level:** "
            f"{recommendation_data.get('risk_level', 'Unknown')}"
        )


    # --------------------------------------------------------
    # Related risk
    # --------------------------------------------------------

    related_risk = recommendation.get(
        "risk",
        {}
    )


    if isinstance(
        related_risk,
        dict
    ) and related_risk:

        st.write("### Related Risk")


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

    st.warning(
        "Recommendation service is currently unavailable."
    )


st.divider()


# ============================================================
# SYSTEM STATUS
# ============================================================

st.header("🟢 System Status")


# ============================================================
# BACKEND STATUS
# ============================================================

backend_status = check_backend()


status_col1, status_col2 = st.columns(2)


with status_col1:

    if backend_status:

        st.success(
            "FastAPI Backend: Connected"
        )

    else:

        st.error(
            "FastAPI Backend: Disconnected"
        )


# ============================================================
# ORCHESTRATOR STATUS
# ============================================================

with status_col2:

    if orchestrator_data:

        st.success(
            "Orchestrator: Data Received"
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