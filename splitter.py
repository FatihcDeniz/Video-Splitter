import csv
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from tkinter import *
from tkinter import filedialog as fd
import subprocess

window = Tk()
window.title("Video Splitter")


def file_selector(label, select=None):
    filetypes = (
        ('Video files', '*.mp4'),
        ('All files', '*.*')
    )

    if select == "file":
        fn = fd.askopenfilename(title='Select a video file',
                                initialdir='/',
                                filetypes=filetypes)

        label.config(text=fn)
    if select == "directory":
        fn = fd.askdirectory(title="Select a directory", initialdir="/")
        label.config(text=fn)


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)


def splitter(choose_location, save_location, second):
    if choose_location:
        print("None")
    length = get_length(choose_location)
    time = open("timers.txt", "w")
    timer = [x for x in range(0, int(length), second)]
    for i in range(len(timer)):
        if i + 1 < len(timer):
            time.write(f"{timer[i]} - {timer[i + 1]}\n")

    time.close()

    video_csv = open("video.csv", "w")
    writer = csv.writer(video_csv, delimiter=";")

    with open("timers.txt") as f:
        times = f.readlines()

    times = [x.strip() for x in times]
    count = 0
    os.chdir(save_location)
    for time in times:
        starttime = int(time.split("-")[0])
        endtime = int(time.split("-")[1])
        ffmpeg_extract_subclip(choose_location, starttime, endtime, targetname=str(times.index(time) + 1) + ".mp4")
        writer.writerow([count, save_location + "/" + str(times.index(time) + 1) + ".mp4"])
        count += 1
    video_csv.close()


def main():
    filename = Label(text=" ", height=5, width=40, underline=True)
    filename.grid(row=0, column=0)
    filebutton = Button(text="Select File", height=5, width=10, command=lambda: file_selector(filename, "file"))
    filebutton.grid(row=0, column=1)

    location = Label(text=" ", height=5, width=40)
    location.grid(row=1, column=0)
    apply_location = Button(text="Save Location", height=2, width=10,
                            command=lambda: file_selector(location, "directory"))
    apply_location.grid(row=1, column=1)

    seconds = Text(window, height=5, width=10)
    apply_seconds = Button(text="Save", height=2, width=10,
                           command=lambda: splitter(filename.cget("text"), location.cget("text"),
                                                    int(seconds.get("1.0", "end"))))
    apply_seconds.grid(row=2, column=1)
    seconds.grid(row=2, column=0)

    window.mainloop()


if __name__ == "__main__":
    main()
