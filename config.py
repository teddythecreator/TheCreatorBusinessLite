import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

PAGE_SPEED_API_KEY = os.getenv("PAGE_SPEED_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GA_TRACKING_ID = os.getenv("GOOGLE_ANALYTICS_ID")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")

def check_env():
    missing = [v for v in [
        "PAGE_SPEED_API_KEY", "OPENAI_API_KEY", "GOOGLE_ANALYTICS_ID",
        "SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASSWORD", "EMAIL_FROM"
    ] if not os.getenv(v)]
    if missing:
        st.error("❗️ Faltan variables en .env: " + ", ".join(missing))
