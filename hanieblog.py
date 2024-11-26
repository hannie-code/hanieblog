import streamlit as st

# Title of the app
st.title("Biography Generator")

# Input fields
st.sidebar.header("Enter Your Details")
name = st.sidebar.text_input("Name", "")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
occupation = st.sidebar.text_input("Occupation", "")
hobbies = st.sidebar.text_area("Hobbies (comma-separated)", "")
goals = st.sidebar.text_area("Goals or Aspirations", "")

# Display biography
if st.sidebar.button("Generate Biography"):
    if name and age and occupation:
        st.header("Your Biography")
        st.write(f"*Name:* {name}")
        st.write(f"*Age:* {age}")
        st.write(f"*Occupation:* {occupation}")
        st.write(f"*Hobbies:* {', '.join(hobby.strip() for hobby in hobbies.split(',')) if hobbies else 'None'}")
        st.write(f"*Goals:* {goals if goals else 'Not specified'}")
    else:
        st.error("Please fill in all the required fields (Name, Age, and Occupation).")