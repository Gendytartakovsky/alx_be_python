task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time bound? (yes or no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UKNOWN priority."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
print(reminder)
