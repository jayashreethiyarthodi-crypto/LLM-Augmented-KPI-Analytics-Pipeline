import streamlit as st
import sqlite3
import pandas as pd
from llm.insight_generator import generate_insights

st.set_page_config(page_title="GenAI Analytics Insight Generator")

st.title("📈 GenAI-Powered Analytics Insight Generator")

conn = sqlite3.connect("data/retail_sales.db")
query = """
SELECT
    strftime('%Y-%m', date) AS month,
    category,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY month, category;
"""
df = pd.read_sql(query, conn)
conn.close()

st.subheader("KPI Data")
st.dataframe(df)

if st.button("Generate Insights"):
    with st.spinner("Generating insights..."):
        insights = generate_insights(df)
    st.subheader("Executive Insights")
    st.write(insights)
