import streamlit as st
from simulation import simulate_workflow

st.set_page_config(page_title="Predictive Process Simulation", layout="wide")

st.title("📊 Predictive Process Simulation & SLA Forecasting")

st.markdown("Simulate workflows and predict SLA risks **before they occur**.")

st.sidebar.header("⚙️ Workforce Allocation")

intake_agents = st.sidebar.slider("Intake Agents", 1, 10, 5)
review_agents = st.sidebar.slider("Review Agents", 1, 10, 3)
approval_agents = st.sidebar.slider("Approval Agents", 1, 10, 4)

st.sidebar.header("📥 Current Backlog")
intake_queue = st.sidebar.number_input("Intake Queue", 0, 500, 40)
review_queue = st.sidebar.number_input("Review Queue", 0, 500, 120)
approval_queue = st.sidebar.number_input("Approval Queue", 0, 500, 30)

workflow_params = {
    "Intake": {
        "arrival_rate": 20,
        "service_rate": 10,
        "agents": intake_agents,
        "queue": intake_queue
    },
    "Review": {
        "arrival_rate": 15,
        "service_rate": 5,
        "agents": review_agents,
        "queue": review_queue
    },
    "Approval": {
        "arrival_rate": 10,
        "service_rate": 8,
        "agents": approval_agents,
        "queue": approval_queue
    }
}

if st.button("🔮 Run Prediction"):
    results = simulate_workflow(workflow_params)

    st.subheader("📈 Forecast Results")

    for stage, output in results.items():
        col1, col2, col3 = st.columns(3)
        col1.metric(f"{stage} – Avg Wait (hrs)", output["avg_wait_time"])
        col2.metric(f"{stage} – SLA Breach %", f"{output['breach_probability']}%")

        if output["breach_probability"] > 50:
            col3.error("⚠️ High Risk Bottleneck")
        else:
            col3.success("✅ Under Control")
