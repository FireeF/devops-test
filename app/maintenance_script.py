#!/usr/bin/env python3
"""
Simple email sending script for cron job
Sends a message to your desired email

For Gmail, you'll need an App Password (not your regular Gmail password):
Go to Google Account settings
Security → 2-Step Verification → App passwords or https://myaccount.google.com/apppasswords
Generate an app password for "Mail"
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email():
    """Send email notification"""
    
    # Email configuration
    sender_email = 'example@gmail.com' #Replace with your email
    sender_password = 'abcd efgh ijkl mnop'  # Replace with App Password from Google
    recipient_email = 'example@gmail.com' #Replace with recipient email
    
    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Cron Job Notification'
    
    # Email body
    body = "This is a cronejob sending a message!"
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"Email sent successfully to {recipient_email} at {datetime.now()}")
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("Running maintenance script...")
    send_email()
    print("Maintenance script completed.")
