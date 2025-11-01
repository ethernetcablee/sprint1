
from datetime import datetime, timedelta
from medicine_core import ReminderService, ValidationError

svc = ReminderService()
today = datetime.now().strftime("%m/%d/%Y")
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m/%d/%Y")

print("== TC01 Demo (Zoloft, 50 mg, tomorrow 10:00 AM, 1 hour before) ==")
r = svc.add_reminder(
    medicine_name="Zoloft",
    dosage="50 mg",
    date_str=tomorrow,
    time_str="10.00 AM",
    option="1 hour before"
)
print("Saved:", r)

print("\n== TC02 Demo (blank medicine, 50 mg, today 09:00 PM, at time of event) ==")
try:
    svc.add_reminder(
        medicine_name="",
        dosage="50 mg",
        date_str=today,
        time_str="09.00 PM",
        option="At time of Event"
    )
except ValidationError as e:
    print("Caught expected validation error:", e)
