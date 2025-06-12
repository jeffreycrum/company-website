import pandas
import streamlit as st

import email_util

df = pandas.read_csv("topics.csv")

st.header('Contact Us!')

with st.form(key='email_form'):
    user_email = st.text_input("Enter your email: ")
    raw_message = st.text_area("Enter your message.")
    reason = st.selectbox(
        "What would you like to discuss?",
        df['topic']
    )
    message = f"""\
Subject: {reason} request from {user_email}

{raw_message}
"""
    button = st.form_submit_button("Send Email")
    if button:
        email_util.send_email(message)
        st.info("Your email was sent successfully")
