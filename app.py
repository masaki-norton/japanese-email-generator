import streamlit as st
import openai
import os

# Get credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Japaense Email Assistant")

# Get prompts from user
system_prompt = st.text_area("Enter system prompt:", "You are a helpful assistant.")
user_prompt = st.text_area("Enter your prompt:")

def get_chatgpt_response(system_prompt, user_prompt):
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].message.content

# Display response to user
if st.button("Send"):
    if user_prompt:
        resposne = get_chatgpt_response(system_prompt, user_prompt)
        st.write(f"ChatGPT: {resposne}")
    else:
        st.write("Please enter a prompt.")
