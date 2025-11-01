
from datetime import datetime, timedelta
from medicine_core import ReminderService, ValidationError

TODAY = datetime.now().strftime("%m/%d/%Y")
TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%m/%d/%Y")

def test_tc01_happy_path_zoloft():
    svc = ReminderService()
    r = svc.add_reminder(
        medicine_name="Zoloft",
        dosage="50 mg",
        date_str=TOMORROW,
        time_str="10.00 AM",
        option="1 hour before"  # stored only; teammate handles notifications
    )
    assert r.medicine_name == "Zoloft"
    assert r.dosage == "50 mg"
    assert r.when.strftime("%m/%d/%Y") == TOMORROW
    assert r.when.strftime("%I.%M %p") == "10.00 AM"
    assert r.option == "1 hour before"
    # saved & retrievable for tomorrow
    assert len(svc.list_reminders_on(TOMORROW)) == 1

def test_tc02_missing_required_blank_name():
    svc = ReminderService()
    try:
        svc.add_reminder(
            medicine_name="",   # blank medicine
            dosage="50 mg",
            date_str=TODAY,
            time_str="09.00 PM",
            option="At time of Event"
        )
        assert False, "Expected ValidationError for missing required field (medicine name)"
    except ValidationError:
        pass
