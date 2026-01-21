import os

import streamlit as st

from app.utils.email import start_periodic_notifier

if not os.path.exists("./data/"):
    os.makedirs("./data/")

# start_periodic_notifier()

st.set_page_config(
    page_title="Home - VSAT App",
    page_icon="🏠",
)

st.title("VSAT Chatbot Home")
st.write("Welcome to the VSAT Chatbot application.")
