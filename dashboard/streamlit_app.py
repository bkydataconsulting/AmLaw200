# streamlit_app.py

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import plotly.express as px

# Load environment variables
load_dotenv()
pg_url = os.getenv("POSTGRES_URL")

# Connect to PostgreSQL
engine = create_engine(pg_url)

# Query the data
@st.cache_data
def load_data():
    query = "SELECT * FROM amlaw200"
    df = pd.read_sql(query, engine)
    return df

df = load_data()

# App layout
st.title("📊 AmLaw 200 Dashboard")
st.markdown("Explore top U.S. law firm data from 2019–2024.")

# Sidebar filters
year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique(), reverse=True))
top_n = st.sidebar.slider("Top N Firms by Revenue", min_value=5, max_value=100, value=20)

# Filtered data
filtered = df[df["year"] == year].sort_values("gross_revenue", ascending=False).head(top_n)

# Add rank column based on gross revenue (1 = highest revenue)
filtered = filtered.reset_index(drop=True)  # Remove the original index
filtered["rank"] = range(1, len(filtered) + 1)  # Add rank column starting from 1

# Show table
st.subheader(f"Top {top_n} Law Firms in {year} by Gross Revenue")
st.dataframe(filtered[["rank", "firm_name", "gross_revenue", "profit_margin", "leverage"]], hide_index=True)

# Bar chart with proper ordering
st.subheader("💰 Gross Revenue")
# Create a bar chart with plotly to maintain the revenue-based order
fig = px.bar(
    filtered, 
    x="firm_name", 
    y="gross_revenue",
    title="",
    labels={"firm_name": "Firm Name", "gross_revenue": "Gross Revenue"}
)
# Update layout to make firm names more readable
fig.update_layout(
    xaxis_tickangle=-45,
    height=500,
    xaxis_title="",
    yaxis_title="Gross Revenue ($)",
    showlegend=False
)
st.plotly_chart(fig, use_container_width=True)