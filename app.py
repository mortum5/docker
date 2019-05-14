import speech_recognition as sr
import csv

# obtain path to "1.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "1.wav")


# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
        print("Sphinx: " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
        print("Sphinx could not understand audio")
except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition

try:
        print("Google: " + r.recognize_google(audio))
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;
        {0}".format(e))
