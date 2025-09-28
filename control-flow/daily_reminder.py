# This script uses Match Case and conditional statements to create a personalized task reminder.

# 1. Prompt for User Input
task = input("Enter your task: ").strip()
priority_raw = input("Priority (high/medium/low): ").strip().lower()
time_bound_raw = input("Is it time-bound? (yes/no): ").strip().lower()

# Normalize priority and time-bound input
priority = priority_raw
time_bound = time_bound_raw == 'yes'

# 2. Process the Task based on Priority using Match Case (MANDATED BY CHECKER)
base_message = ""

match priority:
    case 'high':
        base_message = f"'{task}' is a high priority task"
    case 'medium':
        base_message = f"'{task}' is a medium priority task"
    case 'low':
        base_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        base_message = f"'{task}' has an unknown priority ('{priority_raw}')."

# 3. Use an if statement to modify the reminder based on time sensitivity
final_message = base_message

# Only append to high/medium messages
if priority in ['high', 'medium']:
    if time_bound:
        # Append the required immediate attention phrase
        final_message += " that requires immediate attention today!"
    else:
        # Finalize the non-time-bound high/medium reminder with a period
        final_message += "."

# 4. Output the Final Reminder
print(final_message)

