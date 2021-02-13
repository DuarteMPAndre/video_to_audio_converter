#imports
import moviepy.editor
from tkinter.filedialog import*
import tkinter as tk
def openfile():
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    file = audio.write_audiofile("audio.mp3")
    labelsave = tk.Button(canvas, text = "File saved as 'audio.mp3'")
    labelsave.pack()

canvas = tk.Tk()
canvas.title = ("Video to Audio Converter")
canvas.geometry = ("500x600")

btn_open = tk.Button(canvas, text = "Open File", command = openfile)
btn_open.pack()

canvas.mainloop()
