from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from moviepy import *
from pytube import YouTube
import shutil


# Functions
def path_selector():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def File_Downloader():
    # Get path
    get_link = link_field.get()
    # Get the user selected Path
    user_path = path_label.cget('text')
    screen.title('Downloading...')
    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    clip = VideoFileClip(mp4_video)
    clip.close()
    # move to selected path
    shutil.move(mp4_video, user_path)
    screen.title(f'Done! Video is waiting in {user_path}')


# GUI
screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.configure(bg='white')
canvas.pack()

# logo import
img = PhotoImage(file='Logo.png')
# logo size
img = img.subsample(12, 12)
canvas.create_image(250, 80, image=img)

# Enter Link
link_field = Entry(screen, width=50, bg='white', bd=5, fg='green')
link_label = Label(screen, text='Enter Video Link:', font=('Comic Sans MS', 40), fg='black', bg='white')

# Select Location for the video
path_label = Label(screen, text='Select Path', font=('Comic Sans MS', 30), fg='black', bg='white')
select_btn = Button(screen, text='Select', font=('Comic Sans MS', 15), fg='green', bd=1,
                    command=path_selector)

# Add to screen
canvas.create_window(250, 290, window=path_label)
canvas.create_window(250, 340, window=select_btn)

# Add widgets
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 230, window=link_field)

# Download buttons
download_btn = Button(screen, text='Download!', font=('Comic Sans MS', 20), fg='red', bd=1, command=File_Downloader)
canvas.create_window(250, 410, window=download_btn)

#Made By
made_by = Label(screen, text='Made by: Shon Ben Shimon', font=('Comic Sans MS', 15), fg='black', bg='white')
canvas.create_window(100, 480, window=made_by)

screen.mainloop()
