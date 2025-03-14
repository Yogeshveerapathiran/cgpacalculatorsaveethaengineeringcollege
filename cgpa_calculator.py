import streamlit as st

def letter_to_gpa(letter):
    mapping = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}
    return mapping.get(letter, 0)

def calculate_cgpa(previous_cgpa, previous_credits, grades, credits):
    total_credits = previous_credits + sum(credits)
    weighted_sum = (previous_cgpa * previous_credits) + sum(g * c for g, c in zip(grades, credits))
    return round(weighted_sum / total_credits, 2) if total_credits else 0

st.title("SAVEETHA ENGINEERING COLLEGE")
st.title("CGPA Calculator")
st.write("Enter your grades (either all numerical or all letter-based) and corresponding credits to calculate CGPA.")

user_name = st.text_input("Enter your name:")

grade_type = st.radio("Select Grade Type:", ["Numeric", "Letter"], horizontal=True)
num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1, value=5)

previous_cgpa = st.number_input("Enter previous CGPA:", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
previous_credits = st.number_input("Enter total completed credits:", min_value=0, step=1, value=0)

grades, credits = [], []

for i in range(num_subjects):
    col1, col2 = st.columns(2)
    with col1:
        if grade_type == "Numeric":
            grade = st.number_input(f"Grade for Subject {i+1}:", min_value=0.0, max_value=10.0, step=0.1, value=8.0, key=f"num_{i}")
        else:
            letter = st.selectbox(f"Letter Grade for Subject {i+1}", ["O", "A+", "A", "B+", "B", "C", "F"], key=f"letter_{i}")
            grade = letter_to_gpa(letter)
    with col2:
        credit = st.number_input(f"Credits for Subject {i+1}:", min_value=1, step=1, value=3, key=f"credit_{i}")
    grades.append(grade)
    credits.append(credit)

if st.button("Calculate CGPA"):
    cgpa = calculate_cgpa(previous_cgpa, previous_credits, grades, credits)
    st.success(f"{user_name}, your updated CGPA is: {cgpa}")

st.markdown("""
---
**Yogesh V.S-2022-2026**
""")
