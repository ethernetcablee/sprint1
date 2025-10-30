import schedule
import time
from plyer import notification
import smtplib
from email.mime.text import MIMEText


SENDER_EMAIL = "noahbasch@gmail.com"          # my Gmail address here
APP_PASSWORD = "epyg lvmt yjvc scxg"              # Gmail App Password
RECIPIENT_EMAIL = "noahbasch@gmail.com"            # who receives the email
MEDICATION_NAME = "XYZ"
NAME_USER = "Noah"

#sends an email from gmail account
def send_email(subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    # Gmail over SSL (simple & reliable)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
#details of reminder 
def remind():
    notification.notify(
        title="Medication Reminder",
        message="Take XYZ meds at this time",
        timeout=10,
    )

    subject = "Medication Reminder"
    body = f"Hi {NAME_USER},\n\nIt's time to take your {MEDICATION_NAME} medication.\n\n—Your Reminder App"
    try:
        send_email(subject, body)
        print(" Success! Email sent.")
    except Exception as e:
        print(" Failure! Email failed:", e)

schedule.every().thursday.at("18:50").do(remind)
print("Next run:")
while True:
    schedule.run_pending()
    time.sleep(1)
