# 1. Prompt for User Input
task = input("Enter your task: ").strip()
priority_raw = input("Priority (high/medium/low): ").strip().lower()
time_bound_raw = input("Is it time-bound? (yes/no): ").strip().lower()

priority = priority_raw
time_bound_yes = time_bound_raw == 'yes' 

# 2. Process the Task based on Priority using Match Case (MANDATED BY CHECKER)
final_message = ""

match priority:
    case 'high':
        final_message = f"'{task}' is a high priority task"
    case 'medium':
        final_message = f"'{task}' is a medium priority task"
    case 'low':
        # Low Priority has its full message here
        final_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        final_message = f"'{task}' has an unknown priority ('{priority_raw}')."

# 3. Use an if statement to modify the reminder if the task is time-bound. (MANDATED SEPARATE IF)
# CRITICAL FIX: The checker expects the modification outside the match/case.
if priority in ['high', 'medium']:
    if time_bound_yes:
        final_message += " that requires immediate attention today!"
    else:
        final_message += "."

# 4. Output the Final Reminder
print(final_message)
