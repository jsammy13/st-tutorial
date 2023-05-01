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
 
if(st.button ('Calculate BMI')):
  st.text("Your BMI Index is {}.".format(bmi))
  
  if(bmi <16):
    st.error("You are extremely Underweight")
  elif (bmi >= 16 and bmi <18.5):
    st.warning("You are underweight")
  elif (bmi >=18.5 and bmi <25):
    st.success("Healthy")
  elif (bmi >=25 and bmi <=30):
    st.warning("Overweight")
  elif (bmi >=30):
    st.error("Extremely Overweight")
  


