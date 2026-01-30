import sqlite3
import pandas as pd
import streamlit as st
import os


# Absolute project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DB_PATH = os.path.join(BASE_DIR, "database", "social_media.db")

# Create folder (fixes "unable to open file")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)




conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM posts", conn)

st.title("📊 Social Media ETL Dashboard - REDDIT")

st.subheader("All Posts")
st.dataframe(df)

st.subheader("Sentiment Distribution")
st.bar_chart(df["sentiment"])

st.subheader("Top Positive Posts")
st.write(df.sort_values("sentiment", ascending=False).head(5)[["caption", "sentiment"]])

st.subheader("Top Negative Posts")
st.write(df.sort_values("sentiment", ascending=True).head(5)[["caption", "sentiment"]])
