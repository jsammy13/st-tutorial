import streamlit as st

st.title("Hello World this is Jo's first app")

st.subheader("Building the first app on the Streamlit platform")

st.text(" Hi everyone, this is just a testing of the new platform to see what it can do")

st.markdown("### This is a markdown  section of the page")

st.success("Success command")
st.info("Here is some information")
st.error("We hit an error")
st.warning("Here is a warning")
exp=ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.write("Writing a series of text")
st.write("writing a range of numbers")
st.write(range(10))

if st.checkbox("Show/Hide"):
         st.text("Showing the widget")
   
status = st.radio("Select Gender: ", ('Male', 'Female','not mention'))
if (status =='Male'):
         st.success("Male")
elif (status =='Female'):
         st.success("Female")
else:
         st.warning("no need to know")

st.button("Click me for no action")
if(st.button("Click Here")):
         st.text("This is the response text from the click")

name =st.text_input("Enter Your Name ", "John Smith Jones....")
if(st.button('Submit')):
         result = name.title()
         st.success(result)

         
level = st.slider("Select the level", 1, 100)
st.text('Selected: {}'.format(level))







         

         






