
# AEVA Project
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg) ![Version](https://img.shields.io/badge/version-0.1.0-blue) ![Python Version](https://img.shields.io/badge/python-3.11.9-blue)

---

## Overview

**AEVA** stands for **Ashleigh Ekari's Virtual Assistant**. It is a personal project aimed at building a virtual assistant using Python. AEVA is designed to help manage my daily tasks, connect to Google Calendar, and provide various utilities for personal productivity.

---

## Work in Progress

**Note:** AEVA is currently in active development and not yet ready for release. Some features may not be fully implemented or functional.

---

## Features

- **Google Calendar Integration:** AEVA can fetch and display your Google Calendar events.
- **Voice Recognition:** Using SpeechRecognition to interpret voice commands.
- **Text-to-Speech:** Uses pyttsx3 to convert text to speech.
- **OpenAI Integration:** Leverages OpenAI's API for enhanced conversational capabilities.

---

## Setup Instructions

### Prerequisites

- Python 3.11.9
- Virtual environment setup

### Installation

**1. Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/AEVA.git
   cd AEVA
   ```
   
**2. Create a Virtual Environment:**
```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

**3. Install Dependencies::**
```bash
pip install -r requirements.txt
```

**4. Set Up Google Calendar API:**

- Enable the Google Calendar API on your Google Cloud project.
- Download credentials.json and place it in the project directory.

### Running the Project

**1. Activate Virtual Environment:**
```bash
source env/bin/activate   # On Windows: env\Scripts\activate
```

**2. Running AEVA**
```bash
python main.py
```
---

## Usage
*as of 6t/23/24, These features have not implemented yet*

 To interact with AEVA, use voice commands like:

- "What's on my schedule today?" - Fetches today's Google Calendar events.
- "Add a reminder to call John." - Adds a reminder to your to-do list.
- "What's the weather like?" - Fetches current weather information.