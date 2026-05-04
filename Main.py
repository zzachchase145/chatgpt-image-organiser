from pathlib import Path
import shutil

# === CONFIG ===
#SOURCE_FOLDER = str(Path.home() / 'Downloads')
#DEST_FOLDER = str(Path.home() / 'Pictures' / 'ChatGPT Images')

SOURCE_FOLDER = str(Path.home() / 'Downloads')
DEST_FOLDER = r"D:\AI Receptionist Photos"

downloads_folder = Path(SOURCE_FOLDER)
destination_folder = Path(DEST_FOLDER)

if not downloads_folder.exists():
    print(f'Source folder does not exist {downloads_folder}')
    exit()

destination_folder.mkdir(parents=True, exist_ok=True)

image_extentions = ['.png', '.jpg', '.jpeg', '.webp']

for file in downloads_folder.iterdir():
    if file.suffix.lower() in image_extentions:
        print(file)


        new_path = destination_folder / file.name
        counter = 1

        while new_path.exists():
            new_name = f"{file.stem}_{counter}{file.suffix}"
            new_path = destination_folder / new_name
            counter += 1

        print(new_path)

        shutil.move(file, new_path)