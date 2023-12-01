from flask import Flask, request, jsonify
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

chatStr = ""

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
  # todo: Wrap this inside of a  try catch block
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
  # todo: Wrap this inside of a  try catch block
  # print(response["choices"][0]["text"])
  text += response["choices"][0]["text"]
  if not os.path.exists("Openai"):
    os.mkdir("Openai")

  # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
  with open(f"Openai/{prompt.strip()}.txt", "w") as f:
    f.write(text)

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 0.6
    audio = r.listen(source)
    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language="en-in")
      print(f"User said: {query}")
      return query
    except Exception as e:
      return "Some Error Occurred. Sorry from Jarvis"

app = Flask(__name__)

@app.route('/takeCommand', methods=['POST'])
def takeCommand():
    query = request.get_json()['query']
    recognized_text = takeCommand()
    return jsonify({'text': recognized_text})

@app.route('/chat', methods=['POST'])
def chat():
    query = request.get_json()['query']
    response = chat(query)
    return jsonify({'response': response})

@app.route('/ai', methods=['POST'])
def ai():
    prompt = request.get_json()['prompt']
    response = ai(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)