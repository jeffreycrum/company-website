import streamlit as st
import email_util

st.header('Contact Us!')

with st.form(key='email_form'):
    user_email = st.text_input("Enter your email: ")
    raw_message = st.text_area("Enter your message.")
    message = f"""\
Subject: Inquiry from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Send Email")
    if button:
        email_util.send_email(message)
        print(button)
        st.info("Your email was sent successfully")
