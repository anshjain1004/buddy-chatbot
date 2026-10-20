from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

#CHATBOT LOGIC 

responses = {
    # Greetings
    "hello": "Hi, welcome. How can I help you?",
    "hi": "Hello! Kaise ho?",
    "hey": "Hey there! Kya chal raha hai?",
    "good morning": "Good morning! Aaj ka din productive banao.",
    "good afternoon": "Good afternoon! Lunch ho gaya?",
    "good evening": "Good evening! Din kaisa raha?",
    "good night": "Good night! Kal fresh mind se code karna.",

    # Basic conversation
    "how are you": "I am very fine. Thank you",
    "who are you": "I am a smart AI chatbot",
    "what is your name": "Mera naam Buddy hai, your coding buddy.",
    "what can you do": "Main basic questions ka answer de sakta hoon aur motivate bhi kar sakta hoon.",
    "who made you": "Mujhe ek student developer ne Python mein banaya hai.",
    "thank you": "You're welcome!",
    "thanks": "Koi baat nahi, kabhi bhi poochho.",
    "sorry": "Koi problem nahi, no worries.",
    "help": "Aap mujhse hello, joke, motivate me, what time, ya what date jaise sawal pooch sakte ho.",

    # Mood
    "happy": "Great to hear that",
    "sad": "Sab theek ho jayega. Thoda break lo aur phir wapas aao.",
    "tired": "Thoda rest lo, 10 minute ka break bhi kaafi hota hai.",
    "bored": "Ek chhota project ya LeetCode problem try karo!",
    "angry": "Deep breath lo. Thoda paani piyo aur relax karo.",

    # Motivation
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "i am stressed": "Ek time pe ek task karo, sab ho jayega.",
    "i failed": "Failure bhi ek lesson hai. Dobara try karo.",
    "give me advice": "Consistency talent se zyada important hoti hai.",

    # Tech and coding
    "what is python": "Python ek high-level, easy-to-learn programming language hai.",
    "what is c++": "C++ ek fast, compiled language hai jo DSA aur system programming mein use hoti hai.",
    "what is dsa": "DSA matlab Data Structures and Algorithms. Coding interviews ka core part.",
    "what is ai": "AI matlab Artificial Intelligence, jahan machines insaano jaisa sochne ki koshish karti hain.",
    "what is bug": "Bug code mein ek error ya galti hoti hai.",
    "what is debugging": "Debugging matlab code ke bugs dhoondna aur fix karna.",
    "what is github": "GitHub ek platform hai jahan aap apna code store aur share karte ho.",
    "what is api": "API ek bridge hai jo do software ko aapas mein baat karne deta hai.",

    # Fun
    "tell me a joke": "Programmer ko bulb badalne ko bola, usne kaha: yeh hardware problem hai!",
    "joke": "Python wale ne C++ wale se kaha: tumhare semicolons kahan hain?",
    "favourite language": "Mujhe Python pasand hai, kyunki simple hai.",

    # Exit
    "bye": "Goodbye! Keep coding.",
}

dynamicResponses = {
    "what time": lambda: "Abhi time hai " + datetime.now().strftime("%I:%M %p"),
    "current time": lambda: "Abhi time hai " + datetime.now().strftime("%I:%M %p"),
    "what is the time": lambda: "Abhi time hai " + datetime.now().strftime("%I:%M %p"),
    "what date": lambda: "Aaj ki date hai " + datetime.now().strftime("%d %B %Y"),
    "today's date": lambda: "Aaj ki date hai " + datetime.now().strftime("%d %B %Y"),
    "what is the date": lambda: "Aaj ki date hai " + datetime.now().strftime("%d %B %Y"),
}


def getResponseBot(userQuestion):
    
    # Punctuation hatao (apostrophe nahi, "today's" ke liye)
    for ch in "?!.,":
        userQuestion = userQuestion.replace(ch, "")

    # Beech ke extra spaces hatao, lowercase karo, dono side space lagao
    userQuestion = " " + " ".join(userQuestion.lower().split()) + " "

    for key, func in dynamicResponses.items():
        if " " + key + " " in userQuestion:
            return func()

    # Longest key pehle
    for key in sorted(responses, key=len, reverse=True):
        if " " + key + " " in userQuestion:
            return responses[key]

    return "I don't know. I am currently in learning mode. I will learn that quickly."


# ROUTES

@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()

    if message == "":
        return jsonify({"reply": "Kuch likho to sahi!"}), 400

    # Input ki length limit, taaki koi bahut bada text na bhej sake
    message = message[:300]

    return jsonify({"reply": getResponseBot(message)})


if __name__ == "__main__":
    app.run(debug=True)