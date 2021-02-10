"""Sends email to me to let me know everything ran smoothly."""

import smtplib
import ssl
from email.mime.text import MIMEText


def new_imports_log(mailchimp_created, mailchimp_updated, mailchimp_error_count, errors, tagged, gmail_pass):
    """Sends email describing the lastest import.
    
    Args:
    mailchimp_created: Int, number of new users added to mailchimp list
    mailchimp_updated: Int, number of users updated in mailchimp list
    mailchimp_error_count: Int, number of errors while importing users
    errors: List, descriptions of errors that occured while importing users tagged
    gmail_pass: Str, password for gmail account to send mail"""

    port = 465  # For SSL
    sender_email = "magicmock2@gmail.com"
    receiver_email = "klf16@my.fsu.edu"
    smtp_server = "smtp.gmail.com"
    
    message = f"Created: {mailchimp_created}, Updated: {mailchimp_updated}, Tagged: {tagged}, Errors: {mailchimp_error_count} - {errors}"
    msg = MIMEText(message, 'plain')

    msg['Subject'] = f"Argo Email: {mailchimp_error_count} errors"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmail_pass)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def no_new_imports_log(gmail_pass):
    """Sends email notifying me that the script ran but there were no new users to import.
    
    Args:
    gmail_pass: Str, password for gmail account to send mail"""
    port = 465  # For SSL
    sender_email = "magicmock2@gmail.com"
    receiver_email = "klf16@my.fsu.edu"
    smtp_server = "smtp.gmail.com"

    message = "No new Argo users to import today."
    msg = MIMEText(message, 'plain')

    msg['Subject'] = "Argo Email: No New Users"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, gmail_pass)
        server.sendmail(sender_email, receiver_email, msg.as_string())