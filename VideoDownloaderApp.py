from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading....")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    # Code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile("audio.mp3")
    audio_file.close()
    shutil.move("audio.mp3", file_path)
    # Code for mp4
    video_clip.close()
    shutil.move(mp4,file_path)
    print("Download Complete")

def path_select():
    path = filedialog.askdirectory()
    path_label.config(text=path)




root = Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=400,height=300)
canvas.pack()

# app label
app_label = Label(root,text="Video Downloader",fg='blue',font=("Ariel",20))
canvas.create_window(200,20,window=app_label)

# app entry
url_label = Label(root,text="Enter Video URL")
canvas.create_window(200,80,window=url_label)
url_entry = Entry(root)
canvas.create_window(200,100,window=url_entry)

# Path for Download the Videos
path_label = Label(root,text="Select Path To Download")
path_button = Button(root,text="Select",command=path_select)
canvas.create_window(200,130,window=path_label)
canvas.create_window(200,155,window=path_button)

# Download Button

download_button = Button(root,text="Download",command=download)
canvas.create_window(200,220,window=download_button)



















root.mainloop()