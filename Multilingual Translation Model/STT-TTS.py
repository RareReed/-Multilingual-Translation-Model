# pip install SpeechRecognition
# pip install pyaudio

import tensorflow as tf
import speech_recognition as s_r
print(s_r.__version__) # just to print the version not required
print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
print(r.recognize_google(audio)) #to print voice into text