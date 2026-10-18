import os
import shutil

source_folder = "Practice_Files"
destination_folder = os.path.join(source_folder, "PDFs")

filename = "report.pdf"

source_path = os.path.join(source_folder, filename)
destination_path = os.path.join(destination_folder, filename)

# Check 1: Does the source file exist?
if not os.path.isfile(source_path):
    print("Source file not found!")

# Check 2: Does the destination folder exist?
elif not os.path.isdir(destination_folder):
    print("Destination folder does not exist!")

# Check 3: Does the destination file already exist?
elif os.path.exists(destination_path):
    print("A file with this name already exists!")

# Check 4: Is it safe to move?
else:
    print("File is safe to move!")