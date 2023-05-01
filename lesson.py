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


         

         






