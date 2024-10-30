from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="llama3")
st.title("Laks Chatbot With Llama3 🚀")

prompt = st.text_area("Enter your prompt:")


if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response...."):
            st.button("stop")
            st.write(llm.stream(prompt,stop=['<|eot_id|>']))