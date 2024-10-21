import os
import shutil
import filePathes

source_dir = filePathes.source_dir
raw_dest_dir = filePathes.raw_dest_dir

dest_dir = {
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi']
}

# Organize files
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()
        for dir_name, extensions in dest_dir.items():
            if file_ext in extensions:
                dest_path = os.path.join(
                    raw_dest_dir, dir_name, filename)
                print(f"Moving {file_path} to {dest_path}")
                try:
                    shutil.move(file_path, dest_path)
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                break
    else:
        print(f"Skipping {file_path}, not a file.")

print("File organization complete.")
