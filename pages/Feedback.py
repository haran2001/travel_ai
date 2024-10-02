import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Feedback Section
st.header("Feedback")

st.write(
    "We would love to hear your thoughts, suggestions, concerns, or problems with anything so we can improve!"
)

# User input fields for feedback
user_name = st.text_input("Your Name (Optional)")
user_email = st.text_input("Your Email (Optional)")
feedback_type = st.selectbox(
    "Type of Feedback", ["Suggestion", "Complaint", "Question", "Other"]
)
feedback_text = st.text_area("Your Feedback")


# Function to send email
def send_email(subject, body):
    # Replace these with your email details
    sender_email = os.environ.get("MAIL_USERNAME")
    sender_password = os.environ.get("MAIL_PASSWORD")
    recipient_email = "hari.ayapps@gmail.com"

    # Set up the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(e)
        return False


# Submit button
if st.button("Submit Feedback"):
    if feedback_text:
        feedback = {
            "name": user_name,
            "email": user_email,
            "type": feedback_type,
            "text": feedback_text,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Prepare email content
        email_subject = f"New Feedback: {feedback_type}"
        email_body = f"""
        Name: {user_name or 'N/A'}
        Email: {user_email or 'N/A'}
        Type: {feedback_type}
        Feedback: {feedback_text}
        Timestamp: {feedback['timestamp']}
        """

        # Send the feedback email
        if send_email(email_subject, email_body):
            st.success("Thank you for your feedback! Your feedback has been sent.")
        else:
            st.error(
                "An error occurred while sending your feedback. Please try again later."
            )
    else:
        st.error("Please enter your feedback before submitting.")
