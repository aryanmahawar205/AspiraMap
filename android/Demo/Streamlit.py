import streamlit as st

st.header("AspiraMap")

st.markdown("""
       AspiraMap is an AI-powered career guidance platform designed to help students and professionals find personalized career pathways. 
       By integrating advanced AI models, the platform provides tailored career advice, recommendations for skills development, 
       and future progression opportunities based on an individual’s aptitude, aspirations, and work experience. AspiraMap is accessible 
       via both an Android app and an interactive webpage, ensuring broad accessibility and a seamless user experience.
    """)
st.header("Find Your Career")
st.write("Please fill in the following details to get personalized career guidance.")

    # 1. Full Name  
full_name = st.text_input("Full Name")

    # 2. Email Address
email = st.text_input("Email Address")

    # 3. Age
age = st.slider("Age", min_value=16, max_value=25, value=14)

    # 4. Gender
gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])

    # 5. Preferred Subjects in School
subjects = st.multiselect("Preferred Subjects in School", ["Science", "Commerce", "Arts", "Other"])

    # 6. Extracurricular Activities
extracurriculars = st.text_area("Extracurricular Activities")

    # 7. Career Interests
career_interests = st.text_area("Career Interests")

    # 8. Skills and Strengths
skills = st.text_area("Skills and Strengths")

    # 9. Work Experience
work_experience = st.text_area("Work Experience")

    # 10. Future Goals
future_goals = st.text_area("Future Goals")

    # 11. Current Education Status
education_status = st.selectbox("Current Education Status", ["Completed Class 12", "Currently in Class 12"])

    # 12. Preferred Type of Further Education
education_type = st.selectbox("Preferred Type of Further Education", ["University degree", "Vocational training", "Online courses", "Other"])

    # 13. Subjects of Interest for Further Study
further_study_subjects = st.multiselect("Subjects of Interest for Further Study", ["Science", "Engineering", "Business", "Arts", "Others"])

    # 14. Academic Performance
academic_performance = st.slider("Academic Performance (Percentage)", 0, 100, 75)

    # 15. Learning Style
learning_style = st.radio("Learning Style", ["Visual", "Auditory", "Hands-on", "Mixed"])

    # 16. Influential Figures
influential_figures = st.text_area("Influential Figures (e.g., parents, teachers, professionals)")

    # 17. Geographic Preferences
geographic_preferences = st.multiselect("Geographic Preferences", ["Local", "National", "International"])

    # 18. Financial Considerations
financial_considerations = st.slider("Financial Considerations (Budget)", 0, 100000, 50000)

    # 19. Career Role Models
role_models = st.text_area("Career Role Models")

    # 20. Concerns About Career Choices
career_concerns = st.text_area("Concerns About Career Choices")

    # Submit button
if st.button("Submit"):
        st.success("Thank you for providing your information! Our AI will generate personalized career guidance based on your inputs.")
