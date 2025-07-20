Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time bound? (yes/no): ")

match Priority:
    case "high":
        reminder = f"Reminder: '{Task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{Task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{Task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{Task}' has an UKNOWN priority."
if Time_bound == "yes":
    reminder += " It requires immediate attention today!"
print(reminder)
