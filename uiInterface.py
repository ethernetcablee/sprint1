import NoAPP
from medicine_core import ReminderService, ValidationError
service = ReminderService()
"""
Show Reminders
Add new Reminder
Delete Reminder
Modify Reminders
"""
def add_new_reminder():
    med = input("Medicine name: ")
    dosage = input("Dosage: ")
    day = input("Day (e.g., monday): ")
    time = input("Time (HH:MM): ")

    medicine_core.schedule_reminder(med, dosage, day, time, user_name="Noah")
    print("Reminder added and scheduled!")

x = input("(1) Add new reminder\n(2) Delete reminder\n(3) Modify reminder\n(4) Show reminders\n")
match x:
    case "1":
        med = input("Medicine name: ")
        dose = input("Dosage: ")
        day = input("Day: ")
        time = input("Time (HH:MM): ")

        medicine_core.schedule_reminder(med, dose, day, time, "Noah")
        print("Reminder added! Starting scheduler...")
        NoAPP.run_scheduler()
    case "2":
        print("Delete reminder")
    case "3":
        print("Modify reminder")
    case "4":
        print("Show reminders")



print("Running scheduled reminders...")
NoAPP.run_scheduler()
