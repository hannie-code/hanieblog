import streamlit as st
from PIL import Image
from datetime import datetime

st.title("Editable Biography App")

col1, col2 = st.columns([3, 1])

with col1:
    st.header("About Me")
    name = st.text_input("Enter your full name", "Hanna C. Bernadez")
    bio = st.text_area("Write a short bio about yourself", 
                       "I am a first year student, taking the course of Bachelor of Science in Computer Engineering.")
    birthday = st.text_input("Enter your birthday", "June 24, 2006")
    
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%B %d, %Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    st.write(f"Age: {age}")
             
    gender = st.selectbox("Select your gender", ["Female", "Male", "Other", "Prefer not to say"])

    st.header("Educational Attainment")

    education_options = [
        "College Graduate",
        "College Level",
        "High School Graduate",
        "Middle School Level",
        "Elementary Graduate",
        "Others"
    ]
    
    education_selected  = []
    
    for option in education_options:
        if st.checkbox(option):
            education_selected.append(option)
    
    st.write("*Your Selected Educational Attainment:*")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")
    
    st.header("Parental Information")
    father_name = st.text_input("Father's Name", "Mr. Seth P. Bernadez")
    father_occupation = st.text_input("Father's Occupation", "Tricycle Driver")
    mother_name = st.text_input("Mother's Name", "Mrs. Jasmine C. Bernadez")
    mother_occupation = st.text_input("Mother's Occupation", "Housewife")

    st.header("Contact Information")
    email = st.text_input("Email", "bernadezhana@gmail.com")
    phone = st.text_input("Phone", "09852274527")
    facebook = st.text_input("Facebook Profile URL", "https://www.facebook.com/hanbndz")


    st.header("Hobbies & Interests")
    hobbies = st.text_area("List your hobbies or interests", 
                           "- Playing Volleyball and Watching Korean Drama")
with col2:
    st.subheader("Photo")
    st.image('Hanna.jpg',width=200)


col1, col2 = st.columns([3, 1])

with col1:
    st.header("Your Profile")
    st.subheader(f"Name: {name}")
    st.write(f"Bio: {bio}")
    st.write(f"*Age:* {age}")
    st.write(f"*Gender:* {gender}")
    
    st.subheader("Educational Attainment")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")

    st.subheader("Parental Information")
    st.write(f"Father's Name: {father_name}  \n**Occupation:** {father_occupation}")
    st.write(f"Mother's Name: {mother_name}  \n**Occupation:** {mother_occupation}")

    st.subheader("Contact Information")
    st.write(f"- Email: {email}  \n- Phone: {phone}")
    st.write(f"- Facebook: [Profile]({facebook})")

    st.subheader("Hobbies & Interests")
    st.write(hobbies)

with col2:
    if uploaded_photo:
        st.image(photo, caption=f"{name}'s Photo", use_column_width=True)
    else:
        st.write("No photo uploaded.")
