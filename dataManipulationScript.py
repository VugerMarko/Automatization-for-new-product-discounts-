import csv
from main import *
import smtplib
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
port = 465

sender = "markovugerlol@gmail.com"
password = "cpbl hpis jblc wkki"

recipient = "markovugerlol@gmail.com"

subject = {}

subject = "".join(f"{attr_name}: {attr_value}\n" for attr_name, attr_value in flagProductObj.__dict__.items())

if flagProductObj.discount != "N/A":
    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender, password)
        
        message = MIMEText(subject)
        message["Subject"] = "Your Flagged Product Is Here!"
        message["From"] = sender
        message["To"] = recipient
        server.sendmail(sender, recipient, message.as_string())
        
        print("Email sent succesfully!")

    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        server.quit()

else:
    print("the product is not on discount.")
    