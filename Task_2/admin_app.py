import streamlit as st
import pandas as pd
from common.storage import init_storage, read_data

init_storage()

st.set_page_config("Admin Dashboard", layout="wide")
st.title("Admin Dashboard")

USER_APP_URL = "https://your-user-app.streamlit.app"

st.markdown(f"🔗 [Go to User Dashboard]({USER_APP_URL})")

df = read_data()

st.metric("Total Reviews", len(df))

if not df.empty:
    st.metric("Average Rating", round(df["rating"].mean(), 2))

    st.subheader("Ratings Distribution")
    st.bar_chart(df["rating"].value_counts().sort_index())

    st.subheader("Recent Feedback")
    st.dataframe(df.sort_values("timestamp", ascending=False))

    st.subheader("AI Suggested Actions")
    st.table(df[["rating", "summary", "recommended_action"]])
