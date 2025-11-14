from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import NoAPP

TIME_MASK = "%I.%M %p"   # e.g., "10.00 AM"; "09.00 PM"
DATE_MASK = "%m/%d/%Y"

class ValidationError(Exception):
    pass

@dataclass(frozen=True)
class Reminder:
    medicine_name: str
    dosage: str
    when: datetime
    option: Optional[str] = None  # stored for UI/teammate; not validated here

class ReminderService:
    """
    Minimal logic for Test Case 1 & 2 only:
      - TC01: Create reminder with valid inputs -> save
      - TC02: Missing required field -> raise ValidationError
    Notes:
      - No duplicate checking (that's for TC03).
      - No boundary checks like 50-char name (that's TC04).
      - No notification scheduling (teammate owns that).
    """
    def __init__(self) -> None:
        self._reminders: List[Reminder] = []

    def _parse_when(self, date_str: str, time_str: str) -> datetime:
        try:
            d = datetime.strptime(date_str, DATE_MASK).date()
        except ValueError:
            raise ValidationError("Date must be MM/DD/YYYY")
        try:
            t = datetime.strptime(time_str, TIME_MASK).time()
        except ValueError:
            raise ValidationError("Time must match x.xx AM/PM (e.g., 10.00 AM, 09.00 PM)")
        return datetime.combine(d, t)

    def add_reminder(self, *, medicine_name: str, dosage: str, date_str: str, time_str: str, option: str | None = None) -> Reminder:
        # Only the required-fields rule for TC02
        if not medicine_name or not dosage or not time_str:
            raise ValidationError("Required: medicine name, dosage, time")
        when = self._parse_when(date_str, time_str)

        # Save (no duplicate logic here)
        r = Reminder(medicine_name=medicine_name.strip(), dosage=dosage.strip(), when=when, option=option)
        self._reminders.append(r)
        return r

    def list_reminders_on(self, date_str: str) -> List[Reminder]:
        try:
            target = datetime.strptime(date_str, DATE_MASK).date()
        except ValueError:
            raise ValidationError("Date must be MM/DD/YYYY")
        return [r for r in self._reminders if r.when.date() == target]

def schedule_reminder(medicine_name, dosage, day, time, user_name="User"):
    """
    Connects the reminder created in medicine_core to the notification system in NoAPP.
    """
    # Set scheduler variables
    NoAPP.MEDICATION_NAME = medicine_name
    NoAPP.NAME_USER = user_name
    NoAPP.REMINDER_DAY = day.lower()
    NoAPP.REMINDER_TIME = time

    print(f"[CORE] Scheduling reminder for {medicine_name} on {day} at {time}...")

    # We do NOT start NoAPP's infinite while-loop here
    # The UI will start it at the end of all reminders
    return True
