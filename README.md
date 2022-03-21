# Video-Splitter
This is video splitter created using Tkinter.

This program allows users to select a video file, the location where the video will be saved, and how many seconds periods you want it to split. It will separate videos into indicated seconds and save these videos to the selected file, also it will create a CSV file showing the number of each video and their location.

![This is an image](https://github.com/FatihcDeniz/Video-Splitter/blob/main/Screen%20Shot%202022-03-13%20at%2020.37.52.png)

You can this program by writing `python splitter.py` in the terminal.

`moviepy` and `ffmpeg` libraries are required.


Currently, it is only allowed to select `mp4` files. 
```
filetypes = (
        ('Video files', '*.mp4'),
        ('All files', '*.*')
            )
``` 
If you want to change it `.mp4` in here to whatever you want to select.
