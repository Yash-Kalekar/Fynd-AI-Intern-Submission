import streamlit as st
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import google.generativeai as genai

from common.llm import call_llm, combined_prompt
from common.storage import init_storage, read_data, write_data

# Setup
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-lite-latest")

init_storage()

st.set_page_config("User Feedback", layout="centered")
st.title("Submit Your Feedback")


rating = st.slider("Rating", 1, 5, 3)
review = st.text_area("Your Review")

if st.button("Submit"):
    raw = call_llm(model, combined_prompt(rating, review))
    parsed = json.loads(raw)

    df = read_data()
    df.loc[len(df)] = [
        datetime.now(),
        rating,
        review,
        parsed["user_response"],
        parsed["summary"],
        parsed["recommended_action"]
    ]
    write_data(df)

    st.success("Submitted!")
    st.subheader("AI Response")
    st.write(parsed["user_response"])
