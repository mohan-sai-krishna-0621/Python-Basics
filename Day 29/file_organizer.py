import os

folder_path = "Practice_Files"

if os.path.exists(folder_path):
    files = os.listdir(folder_path)

    print("Files inside Practice_Files:")

    for filename in files:
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            print(filename)

    print("\nFile listing completed!")

else:
    print("Practice folder not found!")
    print("Please create the Practice_Files folder.")