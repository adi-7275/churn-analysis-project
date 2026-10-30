import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Analysis")
st.subheader("Customer Intelligence Dashboard")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("exported_churn_data.csv")

df = load_data()

# Calculate KPIs
churn_rate = df["churn_flag"].mean() * 100
retention_rate = 100 - churn_rate
arpu = df["monthly_charges"].mean()

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric("Churn Rate", f"{churn_rate:.2f}%")
col3.metric("Retention Rate", f"{retention_rate:.2f}%")
col4.metric("ARPU", f"₹{arpu:.2f}")

st.divider()

# Churn by plan
st.subheader("Churn Rate by Plan")

churn_plan = (
    df.groupby("plan_type")["churn_flag"]
    .mean() * 100
)

st.bar_chart(churn_plan)

# Churn by state
st.subheader("Churn Rate by State")

churn_state = (
    df.groupby("state")["churn_flag"]
    .mean() * 100
)

st.bar_chart(churn_state)

# Customer data
st.subheader("Customer Details")

st.dataframe(df, use_container_width=True)