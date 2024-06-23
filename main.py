import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.reminders = []
        self.todo_list = []
        self.context = []
        self.user_preferences = ""
        self.name = "AEVA"
        self.phonetic_name = "AY-vah"
        self.gender = "female"
        self.memory = {
            "name": self.name,
            "phonetic_name": self.phonetic_name,
            "gender": self.gender,
            "user_name": "Ashleigh"
        }

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                self.speak("Sorry, the speech service is down.")
                return None

    def set_reminder(self, reminder):
        self.reminders.append(reminder)
        self.speak(f"Got it, I'll remind you to {reminder}.")
        print(f"Reminder: {reminder}")

    def create_todo_list(self, items):
        self.todo_list.extend(items)
        self.speak(f"I've added {', '.join(items)} to your to-do list.")
        print(f"To-do list: {', '.join(items)}")

    def search_web(self, query):
        try:
            url = f"https://www.google.com/search?q={query}"
            self.speak(f"Searching the web for: {query}")
            print(f"Searching for: {query}")
            return url
        except Exception as e:
            self.speak("An error occurred while searching the web.")
            print(f"Error: {e}")

    def get_reminders(self):
        if self.reminders:
            self.speak("Your reminders are: " + ", ".join(self.reminders))
            print("Reminders: " + ", ".join(self.reminders))
        else:
            self.speak("You have no reminders.")
            print("No reminders.")

    def get_todo_list(self):
        if self.todo_list:
            self.speak("Your to-do list items are: " + ", ".join(self.todo_list))
            print("To-do list: " + ", ".join(self.todo_list))
        else:
            self.speak("Your to-do list is empty.")
            print("No to-do list items.")

    def chat_with_gpt(self, prompt, complexity="high", max_length=150, temperature=0.7, top_p=0.9):
        model = "gpt-3.5-turbo" if complexity == "high" else "text-curie-001"
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Your name is {self.name}. You are a virtual assistant. Be helpful and conversational."},
            {"role": "user", "content": prompt}
        ]
        try:
            response = client.chat.completions.create(model=model,
            messages=messages,
            max_tokens=max_length,
            temperature=temperature,
            top_p=top_p)
            answer = response.choices[0].message.content.strip()
            self.speak(answer)
            print(answer)
            self.context.append(f"User: {prompt}")
            self.context.append(f"{self.name}: {answer}")
            return answer
        except Exception as e:
            self.speak("An error occurred while chatting with GPT.")
            print(f"Error: {e}")
            return None

    def generate_greeting(self):
        prompt = "Generate a friendly greeting for Ashleigh, introduce yourself as AEVA (pronounced AY-vah)."
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=60,
            temperature=1)
            greeting = response.choices[0].message.content.strip()
            return greeting
        except Exception as e:
            self.speak("An error occurred while generating a greeting.")
            print(f"Error: {e}")
            return "Hello, Ashleigh! AEVA here! How can I assist you today?"

    def generate_goodbye(self):
        prompt = "Generate a friendly goodbye for Ashleigh from AEVA (pronounced AY-vah)."
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=60,
            temperature=1)
            goodbye = response.choices[0].message.content.strip()
            return goodbye
        except Exception as e:
            self.speak("An error occurred while generating a goodbye.")
            print(f"Error: {e}")
            return "Goodbye, Ashleigh!"

    def handle_personal_questions(self, command):
        if "your name" in command:
            self.speak(f"My name is {self.memory['name']}, pronounced {self.memory['phonetic_name']}.")
        elif "your gender" in command:
            self.speak(f"I am {self.memory['gender']}.")
        elif "who am I" in command:
            self.speak(f"Your name is {self.memory['user_name']}.")

    def handle_command(self, command):
        exit_commands = ["that's all", "i'm done", "goodbye", "bye", "exit", "quit"]
        if any(cmd in command for cmd in exit_commands):
            goodbye = self.generate_goodbye()
            self.speak(goodbye)
            return False

        if 'reminder' in command:
            self.speak("What would you like me to remind you about?")
            reminder = self.listen()
            if reminder:
                self.set_reminder(reminder)
        elif 'to-do list' in command:
            self.speak("What items would you like to add to your to-do list?")
            items = self.listen()
            if items:
                items = items.split(' and ')
                self.create_todo_list(items)
        elif 'search' in command:
            query = command.replace('search', '').strip()
            url = self.search_web(query)
            if url:
                self.speak(f"You can check the search results here: {url}")
                print(f"Search URL: {url}")
        elif 'reminders' in command:
            self.get_reminders()
        elif 'to-do list' in command:
            self.get_todo_list()
        elif 'your name' in command or 'your gender' in command or 'who am I' in command:
            self.handle_personal_questions(command)
        else:
            self.chat_with_gpt(command)
        return True

    def main(self):
        greeting = self.generate_greeting()
        self.speak(greeting)
        while True:
            command = self.listen()
            if command:
                if not self.handle_command(command):
                    break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.main()