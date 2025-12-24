import sqlite3
import pandas as pd
from llm.insight_generator import generate_insights
from llm.anomaly_explainer import detect_anomalies, explain_anomalies

conn = sqlite3.connect("data/retail_sales.db")

with open("sql/kpi_queries.sql") as f:
    query = f.read()

df = pd.read_sql(query, conn)
conn.close()

print("\n📊 KPI RESULTS\n")
print(df.head())

print("\n🤖 GENAI INSIGHTS\n")
insights = generate_insights(df)
print(insights)

print("\n🚨 ANOMALY ANALYSIS\n")
anomalies = detect_anomalies(df)
anomaly_summary = explain_anomalies(anomalies)
print(anomaly_summary)
