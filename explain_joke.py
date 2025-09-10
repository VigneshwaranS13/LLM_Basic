import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def explain_joke(joke):
    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[            
            {
                "role": "user",
                "content": f"Explain the joke: {joke}",
            },
        ],
        )
        explanation = response.choices[0].message.content
        return explanation
        

    except Exception as e:
        return f"An error occurred: {e}"

def main():
    st.title("Joke Explainer")
    
    # Text box for user to input joke
    joke = st.text_area("Enter your joke here:")
    
    # Submit button
    if st.button("Submit"):
        if joke:
            explanation = explain_joke(joke)
            st.subheader("Explanation")
            st.write(explanation)
        else:
            st.warning("Please enter a joke before submitting.")

if __name__ == "__main__":
    main()