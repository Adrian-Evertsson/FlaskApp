import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

# Load the .env file
load_dotenv()

def send_mail(customer, dealer, rating, comments):
    # Access environment variables
    login = os.getenv('MAILTRAP_LOGIN')
    password = os.getenv('MAILTRAP_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    port = int(os.getenv('SMTP_PORT', 587))  # Default to 587 if not set
    message = f'<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())