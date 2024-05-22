import streamlit as st
import openai
import os

# Get credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# st.title("Japaense Email Assistant")

# # Get prompts from user
# system_prompt = st.text_area("Enter system prompt:", "You are a helpful assistant.")
# user_prompt = st.text_area("Enter your prompt:")

def get_chatgpt_response(system_prompt, user_prompt):
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ]
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].message.content

system_prompt = "You are an assistant."
user_prompt = "What can you help me out with?"

print(get_chatgpt_response(system_prompt, user_prompt))
