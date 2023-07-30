import os
import time
import pyaudio
import speech_recognition as sr
import playsound 
from gtts import gTTS
import openai
import uuid


api_key = "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"

lang ='en'

openai.api_key = api_key

system_msg = "talk like jarvis from ironman"
guy = ""

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy 
                guy = said
                

                if "Jarvis" in said or "jarvis" in said:
                    new_string = said.replace("Jarvis", "")
                    new_string = new_string.strip()
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": new_string}])
                    text = completion.choices[0].message.content
                    print(text)
                    speech = gTTS(text=text, lang=lang, slow=False, tld="co.uk")
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=False)
                    
            except Exception:
                print("Exception")


        return said

    if "stop" in guy:
        break


    get_adio()