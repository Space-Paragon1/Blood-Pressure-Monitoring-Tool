def get_bp_readings():
    """Prompt the user for blood pressure readings and validate them."""
    while True:
        try:
            systolic = int(input("Enter your systolic pressure: "))
            diastolic = int(input("Enter your diastolic pressure: "))
            if systolic < 0 or diastolic < 0:
                print("Cannot be negative. Try again!!")
                continue
            return systolic, diastolic
        except ValueError:
            print("Invalid input. Please enter integers.")


def determine_bp(systolic, diastolic):
    """Return blood pressure classification."""
    if systolic < 120 and diastolic < 80:
        return "normal"
    elif 120 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "elevated_blood_pressure"
    else:
        return "hypertensive"


def determine_FUP(status):
    """Return follow-up recommendation for a status."""
    if status == "normal":
        return "There is no follow_up"
    elif status == "elevated_blood_pressure":
        return "Go for follow-up once every six months"
    else:
        return "Go for follow-up once daily"


def main():
    hypertensive_count = 0
    hypertensive_with_followup = 0
    for i in range(5):
        print(f"\nPatient {i+1}")
        systolic, diastolic = get_bp_readings()
        status = determine_bp(systolic, diastolic)
        print(determine_FUP(status))
        if status == "hypertensive":
            hypertensive_count += 1
            has_followup = input("Is follow-up plan documented? Yes/No ").strip().lower()
            if has_followup == "yes":
                hypertensive_with_followup += 1

    if hypertensive_count:
        percentage = (hypertensive_with_followup / hypertensive_count) * 100
        print(f"{percentage}% of hypertensive patients has a documented follow_up plan")
    else:
        print("\nNo hypertensive patients found.")


if __name__ == "__main__":
    main()
