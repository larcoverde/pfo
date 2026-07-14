import os
import shutil

FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png"],
    "videos": [".mp4", ".mov", ".mkv"],
    "docs": [".txt", ".pdf", ".md", ".doc", ".docx", "ppt", "pptx", "xls", "xlsx"],
    "audio": [".mp3", ".flac", ".wav"],
    "archives": [".rar", ".zip", ".7z"],
    "data": [".json", ".csv", ".xml"],
    "others": []
}

def organize_file(dir):
    if not os.path.isdir(dir):
        print(f"{dir} is not a valid directory.")
        return


    # create a new folder for each category
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(dir, category)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)

        if os.path.isdir(file_path):
            continue

        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions:
                   shutil.move(file_path, os.path.join(
                       dir, category, filename))
                   file_moved = True
                   break
        if not file_moved:
        shutil.move(file_path, os.path.join(dir, "others", filename))
        
def main():
    dir = input("directory path to organize: ")
    organize_file(dir)
    return

if __name__ == "__main__":
    main()
