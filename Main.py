from pathlib import Path
import shutil

downloads_folder = Path.home() / 'Downloads'
destination_folder = Path("D:/AI Receptionist Photos")

destination_folder.mkdir(exist_ok=True)

image_extentions = ['.png', '.jpg', '.jpeg', '.webp']

for file in downloads_folder.iterdir():
    if file.suffix.lower() in image_extentions:
        print(file)


        new_path = destination_folder / file.name
        print(new_path)

        shutil.move(file, new_path)