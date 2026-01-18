import streamlit as st
import pandas as pd

from attendance import calculate_attendance
from scheduler import schedule_tasks

st.set_page_config(page_title="Student Utility App", layout="centered")

st.title("🎓 College Student Utility App")
st.caption("A simple tool to calculate attendance and plan tasks for college students.")


tab1, tab2 = st.tabs(["📊 Attendance Calculator", "📅 Task Scheduler"])

# ---------------- ATTENDANCE CALCULATOR ----------------
with tab1:
    st.header("Attendance Calculator")

    subject = st.text_input("Subject Name")
    classes_per_week = st.number_input("Classes per week", min_value=1, step=1)
    semester_weeks = st.number_input("Semester duration (weeks)", min_value=1, step=1)
    min_percentage = st.number_input("Minimum attendance %", value=75)
    classes_missed = st.number_input("Classes already missed", min_value=0, step=1)

    if st.button("Calculate Attendance"):
        result = calculate_attendance(
            classes_per_week,
            semester_weeks,
            min_percentage,
            classes_missed
        )

        st.subheader("Results")
        st.write(f"**Total Classes:** {result['total_classes']}")
        st.write(f"**Maximum Classes You Can Miss:** {result['max_allowed_miss']}")
        st.write(f"**Classes Missed:** {result['classes_missed']}")
        st.write(f"**Remaining Safe Misses:** {result['remaining_safe_miss']}")
        st.write(f"**Status:** {result['status']}")

# ---------------- TASK SCHEDULER ----------------
with tab2:
    st.header("Task Scheduler")

    task_name = st.text_input("Task Name")
    duration = st.number_input("Duration (hours)", min_value=1, step=1)
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    day = st.selectbox("Preferred Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    if st.button("Add Task"):
        st.session_state.tasks.append({
            "task": task_name,
            "duration": duration,
            "priority": priority,
            "day": day
        })
        st.success("Task added")

    if st.session_state.tasks:
        schedule = schedule_tasks(st.session_state.tasks)
        st.subheader("Your Schedule")

        for d, tasks in schedule.items():
            st.write(f"### {d}")
            df = pd.DataFrame(tasks)
            st.table(df)
