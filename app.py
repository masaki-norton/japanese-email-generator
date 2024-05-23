import streamlit as st
import pandas as pd
import openai
import os

# Get credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Japanese Email Assistant")

# system prompt using data
df = pd.read_csv("japanese_business_email_examples_clean.csv")
emails_json = df.sample(frac=0.5).reset_index(drop=True).to_json(orient="records", force_ascii=False)

system_prompt = f"""
You are an assistant that generates Japanese business emails based on provided examples.
Here are some examples of how to structure the emails:

{emails_json}

Now, please generate an email based on the following input.
"""
# Get user prompt
user_prompt = st.text_area("Enter your prompt:")

def get_chatgpt_response(system_prompt, user_prompt):
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].message.content

# Display response to user
if st.button("Send"):
    if user_prompt:
        resposne = get_chatgpt_response(system_prompt, user_prompt)
        st.write(f"ChatGPT: \n{resposne}")
    else:
        st.write("Please enter a prompt.")
