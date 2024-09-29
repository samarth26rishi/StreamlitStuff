import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai 

genai.configure(api_key='AIzaSyBQOVwNNAwLqpnQqVwVvk6uo2dJo4g6dt8')
model=genai.GenerativeModel('gemini-1.5-flash')#this was the newest model , i can udgrade in the future

def get_gemini_response(input_text,image_data,prompt):
    response= model.generate_content([input_text,image_data[0],prompt])#it will generate according to the parametersare given
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
             }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded you fool !")
    
st.set_page_config(page_title="Sam's Invoice Generator")
st.sidebar.header('Calcul-Ai')
st.sidebar.write('Made by Samarth Rishi')
st.sidebar.write('Powered by Gemini Ai')
st.header("Calcul-Ai")
st.subheader('Made by Samarth Rishi')
st.subheader("Manage your expenses with Calcul-Ai")
input=st.text_input("How may i serve you?",key="input")
uploaded_file=st.file_uploader('Choose an image',type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploded Image",use_column_width=True)
ssubmit=st.button("Let's move ahead :)")

input_prompt="""
You are an expert in calculus i will upload an image with a calculus question , solve it and give me the steps
"""
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)
