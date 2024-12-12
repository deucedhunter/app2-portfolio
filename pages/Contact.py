import streamlit as st
from send_email import send_email


st.header("Contact Page")
with st.form(key='form'):
    user_email = st.text_input("Email Address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message=message)
        st.info("Email sent")