import os
import shutil

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def main():
    source_path = "./Data/lernwelt/"
    target_path = "./classes_lw/"
    classes = os.listdir(source_path)
    for file in classes:
        taste = file.split("_")[0]
        print(taste)
        if file.endswith("wav"):
            create_directory(target_path + taste)
            if not os.path.exists(target_path + file):
                shutil.copy(source_path + file, target_path + taste + "/" + file)

if __name__ == "__main__":
    main()