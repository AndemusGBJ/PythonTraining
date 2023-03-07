''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
import email_config
import smtplib
import schedule, time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os




def sendEmail(recipient, subject, body, filename=""):
    # Create the email message to send
    message = MIMEMultipart()
    message['From'] = "Albert Gubanja"
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    # Attach the file from the current directory
    if filename != "":
        attach_file_name = os.path.basename(filename)
        fileO= os.path.join("reports", filename)
        attach_file = open(fileO, "rb")
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

    # Send the email
    server = smtplib.SMTP(email_config.server_config, email_config.server_port_config)
    server.starttls()
    server.login(email_config.email_address_config, email_config.pwd_config)
    server.sendmail(email_config.email_address_config, recipient, message.as_string())
    server.quit()

    

def sendemail2(recipient, subject, body, filename=""):
    # Create a message object
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "Albert Gubanja"
    msg["To"] = recipient
    msg.set_content(body)

    # Attach a file from the current directory
    if filename != "":
        file_path = os.path.join("reports", filename)
        with open(file_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(filename)
        msg.add_attachment(file_data, maintype="text", subtype="plain", filename=file_name)

    # Connect to an SMTP server and send the message
    with smtplib.SMTP(email_config.server_config, email_config.server_port_config) as s:
        s.starttls()
        s.login(email_config.email_address_config, email_config.pwd_config)
        s.send_message(msg)
    

# Loop send the emails
def send_emails():
    reciptients = ["albert.gubanja@worldmerit.org", "albert.gubanja@qsimpact.org", "albert.gubanja@studentambassadors.com"]
    daily_message ="""Hi,
    Find the daily report attached.
    Thanks"""
    for recipient in reciptients:
        sendemail2(recipient,"Today Report",  daily_message, "first_report.txt")



# Schedule the send mail function to run every day at 2:30 PM
schedule.every().day.at("14:30").do(send_emails)

# For keeping the script running while waiting for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)