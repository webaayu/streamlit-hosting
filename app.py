import streamlit as st
st.set_page_config(page_title="Information Extractor")
st.header("Extract Information from PDF")
uploaded_file = st.file_uploader("choose a pdf file...", type=["pdf"])

if uploaded_file is not None:
# Display uploaded file details
st.subheader("Uploaded PDF File Details:")
st.write("File Name:", uploaded_file.name)
st.write("File Size:", len(uploaded_file.getvalue()), "bytes")

input=st.text_input("Ask Question: ",key="input")
submit = st.button("Tell me about the PDF")
#if submit button is clicked,
if submit:
st.subheader("The response is..")
st.write(“response”) # st.write(response) if answer stored in variable
