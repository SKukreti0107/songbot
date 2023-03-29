import speech_recognition as sr

def listen ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try :
        print("recognizing")
        query = r.recognize_google(audio,language="en-in")    
    except:
        return""

    query = str(query)
    return query.lower()

