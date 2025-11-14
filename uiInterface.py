import NoAPP
"""
Show Reminders
Add new Reminder
Delete Reminder
Modify Reminders
"""
x = input("(1) Add new reminder\n(2) Delete reminder\n(3) Modify reminder\n(4) Show reminders\n")
match x:
    case "1":
        print("Add new reminder")
    case "2":
        print("Delete reminder")
    case "3":
        print("Modify reminder")
    case "4":
        print("Show reminders")
