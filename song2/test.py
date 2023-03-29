import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

from mic_input import listen
from model import model , bag_of_words , words , labels , data, np , nltk
import random

from songbot import suggest_song


# initialize the Tkinter GUI
root = tk.Tk()
root.title("Chatbot")
root.geometry("600x500")
root.configure(bg="#222222")




# add labels and entry box for user input
label = tk.Label(root, text="Enter your message:", font=("Helvetica", 16), fg="#ffffff", bg="#222222")
label.pack(pady=10)

input_box = tk.Entry(root, width=50, font=("Helvetica", 14), bg="#333333", fg="#ffffff")
input_box.pack(pady=10)

# add scrolled text widget to display chat history
output_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Helvetica", 14), bg="#333333", fg="#ffffff")
output_box.pack(pady=10)

# define the chatbot function
def chatbot_wrapper(input):
     
    def chatbot(input):
        chatbot.inp = input
        results = model.predict([bag_of_words(chatbot.inp, words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] >= 0.8:
            for tg in data["intents"]:
                #if tg["tag"]== tag:
                    responses = tg["responses"]
                    #chat.response = (random.choice(responses))
                    #print(chat.response)
                    #speak(chat.response)
                    return(chatbot.response)
            
            suggestion = suggest_song(tag)
            #print(suggestion)
            return(suggestion)
                    
        #workflow for tasks:

        if tag == "goodbye":
            exit()

        if tag == "classical":
            mood = random.choice("classical","guitar","piano")
            suggestion = suggest_song(mood)
            #print(suggestion)
            return(suggestion)

        else :
            return("sorry i was unable to hear you")
            
        
    result = chatbot(input)
    output_box.insert(tk.END, "Bot: " + result + "\n")

# define a function to get user input and show chatbot response
def get_response():
    # get user input
    user_input = input_box.get()

    # clear input box
    input_box.delete(0, tk.END)

    # show user input in output box
    output_box.insert(tk.END, "You: " + user_input + "\n")

    # get chatbot response
    chatbot_wrapper(user_input)

# define a function to run the chatbot function in a separate thread
def run_chatbot_thread():
    Thread(target=listen_and_chatbot).start()

# define a function to listen for microphone input and call chatbot
def listen_and_chatbot():
    while True:
        user_input = listen()
        chatbot_wrapper(user_input)

# add button to submit user input
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=get_response, bg="#555555", fg="#ffffff", activebackground="#777777", activeforeground="#ffffff")
submit_button.pack(pady=10)

# add button to start chatbot
start_button = tk.Button(root, text="Start Chatbot", font=("Helvetica", 14), command=run_chatbot_thread)
start_button.pack(pady=10)

# start the Tkinter event loop
root.mainloop()
