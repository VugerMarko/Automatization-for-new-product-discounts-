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

linkSet = []

linkSet = flagProductObj.model.split()
linkSet.insert(0, flagProductObj.name)

linkSet = [item for item in linkSet if item != "Električna"]
linkSet = [item for item in linkSet if item != "gitara"]
linkSet = [item for item in linkSet if "(" not in item and ")" not in item]

print(f"Link set: {linkSet}")

baseLink = "https://www.muziker.hr/"

linkSet = list(dict.fromkeys(linkSet))

newLink = "-".join(linkPart.lower() for linkPart in linkSet)

print(baseLink + newLink)

if flagProductObj.discount != "N/A" and flagProductObj.status == "Na skladištu":
    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender, password)
        
        message = MIMEText(subject)
        message["Subject"] = f"Your Flagged Product Is Here! {flagProductObj.name} {flagProductObj.model} is on discount!"
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
    print("the flagged product is not on discount.")
    