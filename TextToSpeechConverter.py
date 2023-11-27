from gtts import gTTS
import os
from tkinter import *

def generating_audio(string:str):
    """
    Generating Audio From Text Data
    """
    output = gTTS(text=string,lang="en",slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


def converting_data_to_audio():
    """
    Converting particular contents of the file into speech
    """
    text = open("test.txt","r").read()
    language = "en"
    output = gTTS(text= text,lang=language,slow=False)
    output.save("fileoutput.mp3")
    os.system("start fileoutput.mp3")


def text_To_Speech():
    """
    Helper function for converting user input to speech
    """
    text = entry.get()
    language = "en"
    output = gTTS(text=text,lang=language,slow=False)
    output.save("outputTest.mp3")
    os.system("Start outputTest.mp3")

def converting_user_input_to_speech():
    """
    Accepting text from the user and converts it into speech
    :return:
    """
    global entry
    root = Tk()
    canvas = Canvas(root,width=400,height=300)
    canvas.pack()
    entry = Entry(root)
    canvas.create_window(200,180,window=entry)
    button = Button(root,text="Start",command=text_To_Speech)
    canvas.create_window(200,230,window=button)

    root.mainloop()



