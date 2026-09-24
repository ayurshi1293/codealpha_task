import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


# ---------------- BOT LOGIC ---------------- #

def get_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey", "hii"]:
        return "Hello! 👋 Welcome to Simple Chatbot. How can I help you today?"

    elif message in ["how are you", "how are you doing"]:
        return "I'm doing great! 😊 Thanks for asking."

    elif message in ["what is your name", "your name", "name"]:
        return "I'm a Simple Chabot 🤖, a simple Python rule-based chatbot."

    elif message in ["help", "what can you do"]:
        return (
            "I can respond to greetings, basic questions, "
            "time/date requests and simple conversations."
        )

    elif message in ["time", "current time", "what is the time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. 🕐"

    elif message in ["date", "today", "what is today's date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}. 📅"

    elif message in ["thanks", "thank you", "thankyou"]:
        return "You're welcome! 😊"

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return (
            "I'm sorry, I don't understand that yet. 🤔\n"
            "Try 'help' to see what I can do."
        )


# ---------------- CHAT FUNCTIONS ---------------- #

def send_message():
    message = user_entry.get().strip()

    if not message:
        return

    add_message("You", message, "user")
    user_entry.delete(0, tk.END)

    response = get_response(message)

    root.after(400, lambda: add_message("Simple Chatbot", response, "bot"))


def quick_message(message):
    user_entry.delete(0, tk.END)
    user_entry.insert(0, message)
    send_message()


def add_message(sender, message, message_type):
    chat_area.config(state=tk.NORMAL)

    if message_type == "user":
        chat_area.insert(
            tk.END,
            f"\nYou\n",
            "user_name"
        )
        chat_area.insert(
            tk.END,
            f"{message}\n",
            "user_message"
        )

    else:
        chat_area.insert(
            tk.END,
            f"\n🤖 Simple Chatbot\n",
            "bot_name"
        )
        chat_area.insert(
            tk.END,
            f"{message}\n",
            "bot_message"
        )

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)

    add_message(
        "Simple Chatbot",
        "Chat cleared! 🧹\nHello again! How can I help you?",
        "bot"
    )


def show_help():
    add_message(
        "Simple Chatbot",
        "Available commands:\n"
        "• hello\n"
        "• how are you\n"
        "• your name\n"
        "• help\n"
        "• time\n"
        "• date\n"
        "• thanks\n"
        "• bye",
        "bot"
    )


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("Simple Chatbot - Python Rule-Based Chatbot")
root.geometry("850x650")
root.minsize(650, 500)
root.configure(bg="#eef3fb")


# Header
header = tk.Frame(
    root,
    bg="#10243f",
    height=85
)

header.pack(fill=tk.X)
header.pack_propagate(False)


title_frame = tk.Frame(header, bg="#10243f")
title_frame.pack(side=tk.LEFT, padx=25, pady=12)


tk.Label(
    title_frame,
    text="🤖 Simple Chatbot",
    font=("Segoe UI", 22, "bold"),
    bg="#10243f",
    fg="white"
).pack(anchor="w")


tk.Label(
    title_frame,
    text="Your Friendly Rule-Based Assistant",
    font=("Segoe UI", 10),
    bg="#10243f",
    fg="#b9c8dc"
).pack(anchor="w")


# Online status
status_frame = tk.Frame(header, bg="#10243f")
status_frame.pack(side=tk.RIGHT, padx=25)


tk.Label(
    status_frame,
    text="●",
    font=("Arial", 15),
    bg="#10243f",
    fg="#35d98b"
).pack(side=tk.LEFT)


tk.Label(
    status_frame,
    text=" Online",
    font=("Segoe UI", 11, "bold"),
    bg="#10243f",
    fg="white"
).pack(side=tk.LEFT)


# Chat area
chat_frame = tk.Frame(
    root,
    bg="white",
    bd=0
)

chat_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=20,
    pady=(20, 10)
)


chat_area = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="white",
    fg="#263957",
    bd=0,
    padx=20,
    pady=15,
    state=tk.DISABLED
)

chat_area.pack(
    fill=tk.BOTH,
    expand=True
)


# Text styles
chat_area.tag_config(
    "user_name",
    foreground="#2769d7",
    font=("Segoe UI", 10, "bold")
)

chat_area.tag_config(
    "user_message",
    foreground="#182b49",
    font=("Segoe UI", 11)
)

chat_area.tag_config(
    "bot_name",
    foreground="#10243f",
    font=("Segoe UI", 10, "bold")
)

chat_area.tag_config(
    "bot_message",
    foreground="#263957",
    font=("Segoe UI", 11)
)


# Welcome message
add_message(
    "Simple Chatbot",
    "Hello! 👋 Welcome to Simple Chatbot.\n"
    "Type 'help' to see what I can do.",
    "bot"
)


# Quick action buttons
quick_frame = tk.Frame(
    root,
    bg="#eef3fb"
)

quick_frame.pack(
    fill=tk.X,
    padx=20,
    pady=5
)


quick_buttons = [
    ("👋 Hello", "hello"),
    ("😊 How are you?", "how are you"),
    ("👤 Your name", "your name"),
    ("🕐 Time", "time"),
    ("❓ Help", "help")
]


for text, command in quick_buttons:

    button = tk.Button(
        quick_frame,
        text=text,
        font=("Segoe UI", 9, "bold"),
        bg="white",
        fg="#2769d7",
        activebackground="#2769d7",
        activeforeground="white",
        relief=tk.FLAT,
        cursor="hand2",
        padx=10,
        pady=7,
        command=lambda cmd=command: quick_message(cmd)
    )

    button.pack(
        side=tk.LEFT,
        padx=4
    )


# Input area
input_frame = tk.Frame(
    root,
    bg="white"
)

input_frame.pack(
    fill=tk.X,
    padx=20,
    pady=(5, 20)
)


user_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="white",
    fg="#263957",
    relief=tk.FLAT,
    bd=0
)

user_entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=15,
    pady=12
)


send_button = tk.Button(
    input_frame,
    text="➤ Send",
    font=("Segoe UI", 10, "bold"),
    bg="#2769d7",
    fg="white",
    activebackground="#1d55b0",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    padx=18,
    pady=9,
    command=send_message
)

send_button.pack(
    side=tk.RIGHT,
    padx=8
)


# Clear button
clear_button = tk.Button(
    input_frame,
    text="Clear",
    font=("Segoe UI", 9),
    bg="#f0f3f8",
    fg="#52627a",
    relief=tk.FLAT,
    cursor="hand2",
    command=clear_chat
)

clear_button.pack(
    side=tk.RIGHT,
    padx=5
)


# Enter key support
root.bind(
    "<Return>",
    lambda event: send_message()
)


# Start application
root.mainloop()