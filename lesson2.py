import streamlit as st

st.title('Welcome to BMI Calculator')

weight =st.number_input("Enter your weight (in kgs)")

status= st.radio('Select you height format: ', ('cm', 'meter', 'feet'))

if(status == 'cm') :
  height = st.number_input('Centimeters ')
  
  try:
    bmi = weight/((height/100)**2)
  except:
    st.text("Enter some value of height in cm")
    
elif(status =='meter'):
  height = st.number_input('Meter ')
  
  try:
    bmi = weight/(height **2)
  except:
    st.text("Enter some value of height in m")
 
else:
  height = st.number_input('Feet ')
  
  try:
    bmi = weight/((height/3.28)**2)
  except:
    st.text("Enter some value in height in ft")
 


