# Buddy Chatbot

A simple rule-based chatbot with a web chat interface. Python (Flask) handles the replies, and plain HTML/CSS/JavaScript handles the UI. The frontend talks to the backend through a JSON API.

## Features

- Chat interface with quick-reply buttons
- Whole-phrase matching (so "hi" does not match inside "this")
- Live time and date replies
- Hinglish responses for greetings, mood, motivation and basic tech questions

## Tech stack

Python, Flask, HTML, CSS, JavaScript (fetch API)

## How to run

```
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project structure

```
chatbot/
├── app.py              # Flask server and chatbot logic
├── requirements.txt
└── templates/
    └── index.html      # Chat UI
```

## API

`POST /chat`

Request: `{"message": "hello"}`
Response: `{"reply": "Hi, welcome. How can I help you?"}`

## Limitations

- Matches exact phrases only, so spelling variations need their own keys
- No conversation memory between messages

## Future improvements

- Fuzzy matching for typos
- Multiple trigger phrases per response
- Conversation history
