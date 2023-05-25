import win32com.client
import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
import random
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("Hello i am TARS, how may i help you")

chatstr = ""
def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for prompt: {prompt} \n **************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside try catch block
    text += response["choices"][0]["text"]
    print(text)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1,10083745)}", "w") as f:
         f.write(text)
    # with open("Openai/test.txt", "w") as f:
    #     f.write(text)


def chat(query):
    openai.api_key = apikey
    global chatstr
    chatstr += f"YOU: {query}\n TARS:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside try catch block
    speaker.Speak(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}"
    return response["choices"][0]["text"]

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Trouble recognizing voice."


while True:
    print("Listening...")
    query = takecommand()
    sites = [["youtube","https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            speaker.Speak(f"opening {site[0]}")
            webbrowser.open(site[1])
    if "open music" in query:
        musicpath = "C:/Users/malle/Music/MUSIC/bad.mp3"
        speaker.Speak("enjoy the song")
        os.system(musicpath)
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.Speak(f"the time is {time} motherfucker")
    elif "email".lower() in query.lower():
        ai(prompt=query)
    elif "reset chat".lower() in query.lower():
        chatstr = ""
    elif "go to sleep".lower() in query.lower():
        exit()
    else:
        chat(query)