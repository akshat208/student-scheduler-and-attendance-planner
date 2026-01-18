def schedule_tasks(tasks):
    # Sort tasks by priority: High > Medium > Low
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order[x["priority"]])

    schedule = {}
    for task in tasks:
        day = task["day"]
        if day not in schedule:
            schedule[day] = []
        schedule[day].append(task)

    return schedule


def reschedule_task(task, schedule):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_index = days.index(task["day"])

    for next_day in days[current_index + 1:]:
        if next_day not in schedule:
            schedule[next_day] = [task]
            task["day"] = next_day
            return schedule

    return schedule
