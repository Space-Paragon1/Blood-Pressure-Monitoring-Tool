while True:
    try:
        systolic=int(input("Enter your systolic pressure:"))
        diastolic=int(input(Enter your diastolic pressure:))
        if systolic<0 or diastolic<0:
            print("Cannot be negative.Try again!!")
    except ValueError:
        print("This is not a value")
    break
    def determine_bp(hypertensive,diastolic):
        if systolic<120 and diastolic<80:
            return"normal"
        elif systolic<139,or diastolic<89:
            return"elevated_blood_pressure"
        elif systolic>=140 or diastolic>=90:
            return"hypertensive"

    def determine_FUP():
        if determine_bp(systolic,diastolic)=="normal":
            return"There is no follow_up"
        elif determine_bp(systolic,diastolic)=="elevated_blood_pressure":
            return"Go for follow-up once every six months"
        elif determine_bp(systolic,diastolic)=="hypertensive":
            return"Go for follow-up once daily"
    print(determine_FUP())

    hypertensive_count=0
    hypertensive_with_followup=0
    for i in range(5):
        print(f"\nPatient{i+1}")
        systolic=int(input("Enter the systolic pressure"))
        diastolic=int(input("Enter the diastolic pressure"))

        if determine_bp(systolic,diastolic)=="hypertensive":
            hypertensive_count+=1
            has_followup=input("Is follow-up plan documented?Yes/No")
            if has_followup=="yes":
                hypertensive_with_followup+=1

    if hypertensive_count>0:
        percentage=(hypertensive_with_followup/hypertensive_count)*100
        print(f"{percentage}% of hypertensive patients has a documented follow_up plan")
    else:
        print("\nNo hypertensive patients found.")
