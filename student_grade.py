import streamlit as st

st.set_page_config(page_title="Student Grade Calculator", page_icon="🎓", layout="centered")

st.title("🎓 Student Grade Calculator")
st.write("Enter the marks for each subject to calculate percentage and grade.")

num_subjects = st.number_input("Enter number of subjects", min_value=1, max_value=20, step=1)

marks = []
for i in range(int(num_subjects)):
    mark = st.number_input(f"Enter marks for Subject {i+1}", min_value=0.0, max_value=100.0, step=1.0)
    marks.append(mark)

if st.button("Calculate Grade"):
    if len(marks) > 0:
        total_marks = sum(marks)
        percentage = total_marks / (num_subjects * 100) * 100

        # Grading logic
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        st.success(f"✅ Total Marks: {total_marks:.2f}")
        st.info(f"📊 Percentage: {percentage:.2f}%")
        st.warning(f"🎯 Grade: {grade}")
    else:
        st.error("Please enter marks for at least one subject.")
