# 1. Prompt for User Input
task = input("Enter your task: ").strip()
priority_raw = input("Priority (high/medium/low): ").strip().lower()
time_bound_raw = input("Is it time-bound? (yes/no): ").strip().lower()

# Normalize inputs
priority = priority_raw
time_bound = time_bound_raw == 'yes'

# 2. Process the Task based on Priority using IF/ELIF/ELSE
base_message = ""

# Determine the base message based on priority
if priority == 'high':
    base_message = f"'{task}' is a high priority task"
elif priority == 'medium':
    base_message = f"'{task}' is a medium priority task"
elif priority == 'low':
    # Low priority has a complete message by itself (as per example)
    base_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
else:
    # Handles invalid priority input
    base_message = f"'{task}' has an unknown priority ('{priority_raw}')."

# 3. Use an if statement to modify the reminder based on time sensitivity
final_message = base_message

# Only modify the high/medium reminders if they are time-bound
if priority in ['high', 'medium']:
    if time_bound:
        # Append the required immediate attention phrase for time-bound tasks
        final_message += " that requires immediate attention today!"
    else:
        # Finalize the non-time-bound high/medium reminder with a period
        final_message += "."

# 4. Output the Final Reminder
print(final_message)
