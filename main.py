import os
from dotenv import load_dotenv
from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import schedule
import requests
from bs4 import BeautifulSoup
from plyer import notification

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with the API key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Check if the API key is loaded correctly
if not client.api_key:
    raise ValueError("OpenAI API key is missing. Please check your .env file.")

def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def cli():
    print("Welcome to AEVA! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = get_chatgpt_response(user_input)
        print(f"AEVA: {response}")

if __name__ == "__main__":
    cli()
