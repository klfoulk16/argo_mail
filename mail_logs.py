"""Sends email to me to let me know everything ran smoothly."""

import smtplib
import ssl
from email.mime.text import MIMEText
import os


def new_imports_log(mailchimp_created, mailchimp_updated, mailchimp_error_count, errors, tagged):
    """
    Sends email describing the lastest import.
    
    Args:
    mailchimp_created: Int, number of new users added to mailchimp list
    mailchimp_updated: Int, number of users updated in mailchimp list
    mailchimp_error_count: Int, number of errors while importing users
    errors: List, descriptions of errors that occured while importing users tagged
    """

    port = 465  # For SSL
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = "smtp.gmail.com"
    
    message = f"Created: {mailchimp_created}, Updated: {mailchimp_updated}, Tagged: {tagged}, Errors: {mailchimp_error_count} - {errors}"
    msg = MIMEText(message, 'plain')

    msg['Subject'] = f"Argo Email: {mailchimp_error_count} errors"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        

def other_news_log(subject, message):
    """
    Sends email notifying me that the script ran but there were no new users to import.
    
    Args:
    subject: Str, subject for email
    message: Str, email content
    """
    port = 465  # For SSL
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = "smtp.gmail.com"

    msg = MIMEText(message, 'plain')

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())