import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# say("Hello, How can i help You.")


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

# def say(text):
#     os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
        

if __name__ == '__main__':
    video_file_path = 'C:/Users/shash/OneDrive/Desktop/NITK/Virtual Assistant/videoplayback.mp4'
    os.system(f"open {video_file_path}")

    print('Welcome to Socio Coders')
    say("Welcome to Socio Coders")
    say("How can i help You today.")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [
    ["youtube", "https://www.youtube.com"],
    ["wikipedia", "https://www.wikipedia.com"],
    ["google", "https://www.google.com"],
    ["facebook", "https://www.facebook.com"],
    ["twitter", "https://www.twitter.com"],
    ["amazon", "https://www.amazon.com"],
    ["reddit", "https://www.reddit.com"],
    ["instagram", "https://www.instagram.com"],
    ["linkedin", "https://www.linkedin.com"],
    ["ebay", "https://www.ebay.com"],
    ["netflix", "https://www.netflix.com"],
    ["stackoverflow", "https://www.stackoverflow.com"],
    ["github", "https://www.github.com"],
    ["bbc", "https://www.bbc.com"],
    ["cnn", "https://www.cnn.com"],
    ["nytimes", "https://www.nytimes.com"],
    ["apple", "https://www.apple.com"],
    ["bing", "https://www.bing.com"],
    ["yahoo", "https://www.yahoo.com"],
    ["wordpress", "https://www.wordpress.com"],
    ["pinterest", "https://www.pinterest.com"],
    # Add more sites as needed
    ["imdb", "https://www.imdb.com"],
    ["spotify", "https://www.spotify.com"],
    ["nasa", "https://www.nasa.gov"],
    ["hulu", "https://www.hulu.com"],
    ["espn", "https://www.espn.com"],
    ["craigslist", "https://www.craigslist.org"],
    ["alibaba", "https://www.alibaba.com"],
    ["weather", "https://www.weather.com"],
    ["quora", "https://www.quora.com"],
    ["microsoft", "https://www.microsoft.com"],
    ["target", "https://www.target.com"],
    ["walmart", "https://www.walmart.com"],
    ["paypal", "https://www.paypal.com"],
    ["booking", "https://www.booking.com"],
    ["tripadvisor", "https://www.tripadvisor.com"],
    ["zillow", "https://www.zillow.com"],
    ["etsy", "https://www.etsy.com"],
    ["steam", "https://www.steampowered.com"],
    ["khanacademy", "https://www.khanacademy.org"],
    ["coursera", "https://www.coursera.org"],
    ["ted", "https://www.ted.com"],
    ["nationalgeographic", "https://www.nationalgeographic.com"],
    ["vimeo", "https://www.vimeo.com"],
    ["buzzfeed", "https://www.buzzfeed.com"],
    ["forbes", "https://www.forbes.com"],
    ["businessinsider", "https://www.businessinsider.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["huffpost", "https://www.huffpost.com"],
    ["foxnews", "https://www.foxnews.com"],
    ["cbc", "https://www.cbc.ca"],
    ["techcrunch", "https://www.techcrunch.com"],
    ["mashable", "https://www.mashable.com"],
    ["vice", "https://www.vice.com"],
    ["lifehacker", "https://www.lifehacker.com"],
    ["dailymotion", "https://www.dailymotion.com"],
    ["theguardian", "https://www.theguardian.com"],
    ["bloomberg", "https://www.bloomberg.com"],
    ["npr", "https://www.npr.org"],
    ["reuters", "https://www.reuters.com"],
    # Additional sites
    ["usatoday", "https://www.usatoday.com"],
    ["abcnews", "https://www.abcnews.go.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    # ... Add more sites here
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    ["usatoday", "https://www.usatoday.com"],
    # Total: 100 sites
    ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        # say(query)