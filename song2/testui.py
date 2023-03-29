import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

from mic_input import listen
from main import chat


# initialize the Tkinter GUI
root = tk.Tk()
root.title("Chatbot")
root.geometry("600x500")
root.configure(bg="#222222")


# create a style object with rounded edges
style = tk.ttk.Style(root)
style.configure("TButton", padding=6, relief="flat", background="#ccc", borderwidth=0, bordercolor="#ccc", font=("Helvetica", 14), foreground="#000")
style.map("TButton", foreground=[('active', '#000')], background=[('active', '#ddd')], relief=[('pressed', 'groove'), ('!pressed', 'flat')])

# add labels and entry box for user input
label = tk.Label(root, text="Enter your message:", font=("Helvetica", 16), fg="#ffffff", bg="#222222")
label.pack(pady=10)

input_box = tk.Entry(root, width=50, font=("Helvetica", 14), bg="#333333", fg="#ffffff")
input_box.pack(pady=10)

# add scrolled text widget to display chat history
output_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Helvetica", 14), bg="#333333", fg="#ffffff")
output_box.pack(pady=10)

# define the chatbot function
def chatbot(input):
    chat(input)
    # your chatbot code here


# define a function to get user input and show chatbot response
def get_response():
    # get user input
    user_input = input_box.get()

    # clear input box
    input_box.delete(0, tk.END)

    # show user input in output box
    output_box.insert(tk.END, "You: " + user_input + "\n")

    # get chatbot response
    results = chatbot(user_input)

    # show chatbot response in output box
    output_box.insert(tk.END, "Bot: " + results + "\n")

# define a function to run the chatbot function in a separate thread
def run_chatbot_thread():
    Thread(target=chatbot).start()

# add button to submit user input
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=get_response, bg="#555555", fg="#ffffff", activebackground="#777777", activeforeground="#ffffff")
submit_button.pack(pady=10)

# add button to start chatbot
start_button = tk.Button(root, text="Start Chatbot", font=("Helvetica", 14), command=run_chatbot_thread)
start_button.pack(pady=10)

# start the Tkinter event loop
root.mainloop()
