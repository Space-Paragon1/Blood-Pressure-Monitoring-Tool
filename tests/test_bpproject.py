import bpproject


def test_determine_bp():
    assert bpproject.determine_bp(118, 79) == "normal"
    assert bpproject.determine_bp(125, 85) == "elevated_blood_pressure"
    assert bpproject.determine_bp(150, 95) == "hypertensive"


def test_determine_FUP():
    assert bpproject.determine_FUP('normal') == 'There is no follow_up'
    assert bpproject.determine_FUP('elevated_blood_pressure') == 'Go for follow-up once every six months'
    assert bpproject.determine_FUP('hypertensive') == 'Go for follow-up once daily'
