import streamlit as st
from send_email import email_function
import pandas

topics_file = pandas.read_csv("topics.csv")

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?",
                         topics_file["topic"])
    raw_message = st.text_area("Your message")

    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    {topic}
    {raw_message}
    """

    button = st.form_submit_button("Submit")

    if button:
        email_function(message)
        st.info("Your email was sent successfully.")
