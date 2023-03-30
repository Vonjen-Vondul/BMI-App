import streamlit as st
from PIL import Image

st.title("BMI Calculator App")

img=Image.open("BMI.JPG")

st.image(img)

weight=st.number_input("What is your weight in KG", step=1)
height=st.number_input("What is your Height in Metre")


def body_mass_index(weight,height):
    bmi = round(weight/(height**2),1)
    
    if bmi < 18.5:
        return(f'your BMI is : {bmi}, you are underweight')
    elif 18.4 < bmi < 25:
        return(f'your BMI is : {bmi}, you are normal')
    elif 25.9 < bmi < 30:
        return(f'your BMI is : {bmi}, you are overweight')
    elif 29.9 < bmi < 35:
        return(f'your BMI is : {bmi}, class 1 obesity ')
    elif 34.9 < bmi < 40:
        return(f'your BMI is : {bmi}, class 2 obesity')
    else:
        return(f'your BMI is : {bmi}, extreme scenario consult your doctor')


if st.button("Calculate BMI"):
    st.write(body_mass_index(weight,height))



