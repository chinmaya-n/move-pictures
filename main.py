# Move all Photos from a directory recursively to another directory
import os
from random import randrange
from pathlib import Path

PICTURE_FILE_EXTENSIONS = ('jpg', 'jpeg', 'png', 'gif')


def scan_for_pictures(source_dir):
    """
    Scan for photos in a directory recursively
    """
    input_dir = Path(source_dir)
    pictures = set()
    for ext in PICTURE_FILE_EXTENSIONS:
        pattern = "*." + ext
        pictures.update(list(map(str, input_dir.rglob(pattern))))
    return pictures


def move_pictures(pictures, destination_dir):
    """
    Move given pictures into destination directory
    """
    for picture in pictures:
        try:
            new_name = os.path.join(destination_dir, os.path.basename(picture))
            if os.path.exists(new_name):
                random_number = str(randrange(1, 1000000))
                new_name = os.path.join(destination_dir, random_number+'-'+os.path.basename(picture))
                if os.path.exists(new_name):
                    print(f"ERROR: {picture} already exists at destination")
                    continue
            
            os.rename(picture, new_name)
            print(f"{picture} --> {new_name}")
        except Exception as ex:
            print(f"Exception with file: {picture}")
            raise ex


if __name__ == "__main__":
    source_dir = "/Users/chinmaya/Downloads/pictures"
    destination_dir = "/Users/chinmaya/Downloads/dest-pictures"
    move_pictures(scan_for_pictures(source_dir), destination_dir)
