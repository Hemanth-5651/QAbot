import google.generativeai as genai
import os

import streamlit as st
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def gemini(question):
    response=chat.send_message(question,stream=False)
    return response
st.set_page_config(page_title="Q&A demo")
st.header("gemini llm application")
if 'chat' not in st.session_state:
    st.session_state['chat']=[]
input=st.text_input("input:",key="input")
submit=st.button("ask the question")

if submit and input:
    res=gemini(input)
    st.session_state['chat'].append(("You",input))
    st.subheader("the response is:")
    
    # for chunk in res:
    #     st.write(chunk.text)
    #     st.session_state['chat'].append(("Bot:",chunk.text))
    st.write(res.text)
    st.session_state['chat'].append(("Bot:",res.text))
st.subheader("the chat history is")
for role,msg in st.session_state['chat']:
    st.write(role," : ",msg)