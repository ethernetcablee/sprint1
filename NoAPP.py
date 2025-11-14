import schedule
import time
import threading
from plyer import notification
import smtplib
from email.mime.text import MIMEText

# Set by UI
SENDER_EMAIL = ""
APP_PASSWORD = ""
RECIPIENT_EMAIL = ""
NAME_USER = ""

# Store all scheduled jobs so we can cancel them
# Format: (medicine, day, time, job1, job2)
scheduled_jobs = []

# EMAIL NOTIFICATION
def send_email(subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

# DESKTOP NOTIFICATION
def remind(title: str, message: str, timeout: int):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout,
    )

# SCHEDULE A REMINDER
def schedule_reminder(medicine, day, time, user_name):
    # Popup notification job
    job1 = schedule.every().__getattribute__(day).at(time).do(
        remind,
        "Medication Reminder",
        f"Take your {medicine}",
        10
    )

    # Email job
    job2 = schedule.every().__getattribute__(day).at(time).do(
        send_email,
        "Medication Reminder",
        f"Hi {user_name},\n\nIt's time to take your {medicine}.\n-- Reminder App"
    )

    scheduled_jobs.append((medicine, day, time, job1, job2))

    print(f"[NoAPP] Scheduled {medicine} on {day} at {time}")

# CANCEL A REMINDER
def cancel_reminder(medicine, day, time):
    for entry in scheduled_jobs:
        med, d, t, job1, job2 = entry
        if med == medicine and d == day and t == time:
            schedule.cancel_job(job1)
            schedule.cancel_job(job2)
            scheduled_jobs.remove(entry)
            print(f"[NoAPP] CANCELLED reminder: {medicine} on {day} at {time}")
            return True
    print(f"[NoAPP] No matching reminder to cancel.")
    return False

#   START BACKGROUND LOOP
def start_scheduler_background():
    def loop():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=loop, daemon=True)
    t.start()
