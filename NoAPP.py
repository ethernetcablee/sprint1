
import schedule
import time
from plyer import notification
import smtplib
from email.mime.text import MIMEText


SENDER_EMAIL = ""          # my Gmail address here
APP_PASSWORD = ""          #  App Password
RECIPIENT_EMAIL = ""       # who receives the email
MEDICATION_NAME = ""         # medication name
NAME_USER = "Noah"
REMINDER_TIME = "00:00" 
REMINDER_DAY = "" # e.g., schedule.THURSDAY

subject = "Medication Reminder App"

title = ""
message = ""
timout = 10


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
def remind(title: str, message: str, timeout: int):
    # use the parameters you passed in
    notification.notify(
        title=title,
        message=message,
        timeout=timeout,
    )

def run_scheduler():
    print("[NoAPP] Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(1)


#  everything above stays the same 

if __name__ == "__main__":
    #Use getattr() to schedule dynamically
    if hasattr(schedule.every(), REMINDER_DAY):
        getattr(schedule.every(), REMINDER_DAY).at(REMINDER_TIME).do(
            remind, "Medication Reminder", "Take {MEDICATION_NAME} at this time", 10
        )
        getattr(schedule.every(), REMINDER_DAY).at(REMINDER_TIME).do(
            send_email, "---TEST--- ",f"Hi {NAME_USER},\n\nIt's time to take your {MEDICATION_NAME}.\n\n—Your Reminder App"
        )  
        print(f"Scheduled for {REMINDER_DAY.title()} at {REMINDER_TIME}")
#rejects invalid day input! and prints error message
    else:
        print(f"Invalid day: {REMINDER_DAY}")

    #while True:
        #schedule.run_pending()
        #time.sleep(1)
