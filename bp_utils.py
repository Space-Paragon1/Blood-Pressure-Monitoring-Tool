def determine_bp(systolic, diastolic):
    """Classify blood pressure reading.

    Args:
        systolic (int): Systolic pressure in mmHg.
        diastolic (int): Diastolic pressure in mmHg.

    Returns:
        str: "normal", "elevated_blood_pressure", or "hypertensive".
    """
    if systolic < 120 and diastolic < 80:
        return "normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "elevated_blood_pressure"
    elif systolic >= 140 or diastolic >= 90:
        return "hypertensive"
    else:
        return "hypertensive"
