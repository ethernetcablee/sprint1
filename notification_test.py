import NoAPP
from datetime import datetime, timedelta
import schedule 
import time 


"""
test file to test notification and email functions from NoAPP.py
does this by setting a reminder for one minute from the current time and calling functions from NoAPP.py to send a test notification and email
"""


#sets to current time 
current_datetime = datetime.now()
# Add one minute to current time
next_minute = current_datetime + timedelta(minutes=1)
reminderdaystring = current_datetime.strftime("%A")
REMINDER_DAY = reminderdaystring.lower()
# Format time as string (e.g., "14:30") with one minute added
REMINDER_TIME = next_minute.strftime("%H:%M")

#test strings
MEDICATION_NAME = "TEST MEDICATION NAME"
NAME_USER = "Test User"




if __name__ == "__main__":
    #Use getattr() to schedule dynamically
    if hasattr(schedule.every(), REMINDER_DAY):
        getattr(schedule.every(), REMINDER_DAY).at(REMINDER_TIME).do(
            NoAPP.remind, "---TEST--- ", f"Take {MEDICATION_NAME} at this time", 10
        )
        getattr(schedule.every(), REMINDER_DAY).at(REMINDER_TIME).do(
            NoAPP.send_email, "---TEST--- ",f"Hi {NAME_USER},\n\nIt's time to take your {MEDICATION_NAME}.\n\n—Your Reminder App"
        )

        print(f"Scheduled for {REMINDER_DAY.title()} at {REMINDER_TIME}")
    else:
        print(f"Invalid day: {REMINDER_DAY}")

    while True:
        schedule.run_pending()
        time.sleep(1)