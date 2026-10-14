import os

filenames = [
    "report.pdf",
    "photo.jpg",
    "notes.txt",
    "program.py",
    "music.mp3"
]

for filename in filenames:
    name, extension = os.path.splitext(filename)
    print(f"{filename} -> {extension}")