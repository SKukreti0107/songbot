from model import model , bag_of_words , words , labels , data, np , nltk
import random

from mic_input import listen

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from songbot import suggest_song
from speech import speak





def chatbot():
    print("Hello there")
    #importing user input from mic getting response from data
    while True:
        #chatbot.inp = listen()
        chatbot.inp = input("you:")
        results = model.predict([bag_of_words(chatbot.inp, words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] >= 0.9:
            for tg in data["intents"]:
                if tg["tag"]== tag:
                    responses = tg["responses"]
                    #chat.response = (random.choice(responses))
                    #print(chatbot.response)
                    #speak(chat.response)
                    #return(chatbot.response)
            print(f"tag={tag}") 
                               
        #workflow for tasks:

            if tag == "goodbye":
                chatbot.response = (random.choice(responses))
                print(chatbot.response)
                speak(chatbot.response)
                exit()

            elif tag == "study":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "work-out":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "Groovy":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "classical":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "happy":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "sad":
                suggestion = suggest_song(tag)
                print(suggestion)

            elif tag == "dance":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "chill":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "party":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "sleep":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "romance":
                suggestion = suggest_song(tag)
                print(suggestion)
                speak(suggestion)

            elif tag == "greetings":
                chatbot.response = (random.choice(responses))
                print(chatbot.response)
                speak(chatbot.response)
        
            elif tag == "thanks":
                chatbot.response = (random.choice(responses))
                print(chatbot.response)
                speak(chatbot.response)

            elif tag == "about":
                chatbot.response = (random.choice(responses))
                print(chatbot.response)
                speak(chatbot.response)

        else :
            print("sorry i was unable to understand")
           
             
             
           
chatbot()