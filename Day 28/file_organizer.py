import os

filenames = [
    "report.pdf",
    "photo.jpg",
    "notes.txt",
    "program.py"
]

for filename in filenames:
    name, extension = os.path.splitext(filename)

    if extension == ".pdf":
        folder = "PDFs"

    elif extension in [".jpg", ".png"]:
        folder = "Images"

    elif extension == ".txt":
        folder = "Text_Files"

    elif extension == ".py":
        folder = "Python_Files"

    else:
        folder = "Others"

    os.makedirs(folder, exist_ok=True)

    print(f"{filename} -> {folder}/")

print("\nFolders created successfully!")