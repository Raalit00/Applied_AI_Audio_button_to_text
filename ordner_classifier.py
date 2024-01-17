import os
import shutil

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def main():
    classes = os.listdir("./Data")
    for file in classes:
        if file.endswith("wav"):
            create_directory("./classes/" + file[:1])
            if not os.path.exists("./classes/" + file):
                shutil.copy("./Data/" + file, "./classes/" + file[:1] + "/" + file)

if __name__ == "__main__":
    main()