import math

def calculate_attendance(classes_per_week, semester_weeks, min_percentage, classes_missed):
    total_classes = classes_per_week * semester_weeks
    min_required = math.ceil((min_percentage / 100) * total_classes)
    max_allowed_miss = total_classes - min_required
    remaining_safe_miss = max_allowed_miss - classes_missed

    status = "Safe"
    if remaining_safe_miss < 0:
        status = "Attendance in danger"

    return {
        "total_classes": total_classes,
        "max_allowed_miss": max_allowed_miss,
        "classes_missed": classes_missed,
        "remaining_safe_miss": remaining_safe_miss,
        "status": status
    }
