import openai
import os
import tkinter as tk
from tkinter import ttk
#please run pip install openai in terminal before running the programe
#Git hub link :-https://github.com/VeerjyotSingh/ChatBot.git
x=0
openai.api_key = "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"
messages = []
system_msg = "talk like Friday from iron man"
messages.append({"role": "system", "content": system_msg})
os.system('cls' if os.name == 'nt' else 'clear')
print("Your assistant is ready!")
a = True
replied = ""
def request(message):
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply
def Justdoit():
    global x
    x += 2
    message = input_text.get("1.0", "end-1c")
    Label1 = tk.Label(w,text="You: "+message, justify="left", wraplength=1150)
    Label1.grid(row = x , column=0,sticky="w")
    reply = request(message=message)
    Label2 = tk.Label(w,text="Sarthi: "+reply, justify="left", wraplength=1150)
    Label2.grid(row = x+1 , column=0,sticky="w")


#UI worksing below :-
root = tk.Tk()
root.configure(bg="black")
root.title("Sarthi: The Chatbot")
root.geometry("1280x720")
w = tk.Frame (root,height = 540, bg="#242423" ,width = 1240)
w.grid(pady=(20,20), padx=(20,20))
w.grid_propagate(False)
v = tk.Frame (root,height = 120, bg="#242423" ,width = 1240)
v.grid(padx=(20,20))
v.grid_propagate(False)
input_btn = tk.Button(v,text="Send",width=20,height=6,command=Justdoit)
input_btn.grid(column=2,row=0,padx=(20,10))
input_text = tk.Text(v, height = 8, width = 140)
input_text.grid(column=1,row=0)

root.mainloop()