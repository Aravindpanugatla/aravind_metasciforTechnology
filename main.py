import streamlit as st

# Set page
st.set_page_config(page_title=" BMI Calculator",)
st.title(" BMI Calculator")

# Input Fields
height = st.number_input("Enter Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Enter Weight (kg)", min_value=10, max_value=300, value=70)

# Calculate BMI
if st.button("Calculate BMI", use_container_width=True):
    bmi = weight / ((height / 100) ** 2)
    st.write(f" Your BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning(" Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success(" Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning(" Overweight")
    else:
        st.error(" Obese")

st.image(r"C:\Users\aravind\OneDrive\Desktop\streamlit\stlapp\space.jpg", caption=" BMI Classification Chart", use_container_width=True)
