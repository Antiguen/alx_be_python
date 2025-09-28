# 1. Prompt for User Input
task = input("Enter your task: ").strip()
priority_raw = input("Priority (high/medium/low): ").strip().lower()
time_bound_raw = input("Is it time-bound? (yes/no): ").strip().lower()

priority = priority_raw
time_bound_yes = time_bound_raw == 'yes' # Use boolean for cleaner final logic

# 2. Process the Task based on Priority using Match Case (MANDATED BY CHECKER)
final_message = ""

match priority:
    case 'high':
        if time_bound_yes:
            # High Priority, Time-bound
            final_message = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            # High Priority, Not Time-bound
            final_message = f"'{task}' is a high priority task."
    case 'medium':
        if time_bound_yes:
            # Medium Priority, Time-bound
            final_message = f"'{task}' is a medium priority task that requires immediate attention today!"
        else:
            # Medium Priority, Not Time-bound
            final_message = f"'{task}' is a medium priority task."
    case 'low':
        # Low Priority (Not affected by time-bound status)
        final_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        # Handles invalid priority input
        final_message = f"'{task}' has an unknown priority ('{priority_raw}')."

# 3. Output the Final Reminder
print(final_message)
