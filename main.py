import os
from dotenv import load_dotenv
import openai
import pyttsx3
import speech_recognition as sr
import schedule
import requests
from bs4 import BeautifulSoup
from plyer import notification

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables using os.getenv
openai_api_key = os.getenv('OPENAI_API_KEY')
openweathermap_api_key = os.getenv('OPENWEATHERMAP_API_KEY')
google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
astronomy_api_key = os.getenv('ASTRONOMY_API_KEY')

# Initialize OpenAI client
openai.api_key = openai_api_key

def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def test_openai():
    prompt = "Hello, world!"
    response = get_chatgpt_response(prompt)
    print("OpenAI response:", response)

def test_pyttsx3():
    engine = pyttsx3.init()
    engine.say("Hello, world!")
    engine.runAndWait()

def test_schedule():
    def job():
        print("Scheduled job executed.")
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()

def test_requests():
    response = requests.get('https://www.google.com')
    print("Requests status code:", response.status_code)

def test_beautifulsoup4():
    response = requests.get('https://www.google.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    print("BeautifulSoup title:", soup.title.string)

def test_plyer():
    notification.notify(
        title='Test Notification',
        message='Hello, world!',
        timeout=10
    )

def cli():
    print("Welcome to AEVA CLI! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = get_chatgpt_response(user_input)
        print(f"AEVA: {response}")

if __name__ == "__main__":
    cli()
    # Uncomment to test other functionalities
    # test_openai()
    # test_pyttsx3()
    # test_requests()
    # test_beautifulsoup4()
    # test_plyer()
    # test_schedule()
