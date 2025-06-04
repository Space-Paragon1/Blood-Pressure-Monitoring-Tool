# Blood-Pressure-Monitoring-Tool
#Problem Statement:
A healthcare data collection task required developing a program to:
Collect blood pressure readings (systolic and diastolic) from patients.
Classify patients' blood pressure status based on standard medical guidelines.
Recommend follow-up actions based on their classification.
Track how many hypertensive patients have a documented follow-up plan.
Compute the percentage of hypertensive patients with follow-up documentation.

#Objective:
The main goal was to build a system that:
Determines whether a patient is normal, elevated, or hypertensive.
Advises an appropriate follow-up frequency.
Accepts inputs for five patients and records whether hypertensive patients have a documented follow-up plan.
Reports the percentage of hypertensive patients who are properly followed up.


#Solution Overview
The program performs the following:
User Input Validation:
Repeatedly prompts for valid, non-negative integer values for systolic and diastolic pressure.
Handles non-integer inputs gracefully with error messages.


#Blood Pressure Classification:
Uses AHA (American Heart Association)-style logic:
Normal: Systolic < 120 and Diastolic < 80
Elevated: Systolic 120–139 or Diastolic 80–89
Hypertensive: Systolic ≥ 140 or Diastolic ≥ 90

#Follow-Up Recommendation:
Normal: No follow-up needed.
Elevated: Follow-up every six months.
Hypertensive: Follow-up daily.

#Data Collection Loop:
Iterates through five patients.
Tracks how many are hypertensive.
Asks whether a follow-up plan is documented for hypertensive patients.

#Summary Output:
Prints the percentage of hypertensive patients with documented follow-up plans.

#Usage
Run the script in a Python environment. Follow prompts to enter:
Systolic and diastolic readings
Whether follow-up plans are documented for hypertensive patients


