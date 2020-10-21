from PIL import Image
import os


def convertation(prev_ext, new_ext, directory):
    change = 0
    for root, folders, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name.endswith('.' + prev_ext):
                name = os.path.splitext(file_name)[0]
                name = os.path.basename(name)
                change = 1
                im = Image.open(file_name)
                im.save(name + '.' + new_ext)
                os.remove(file_name)
    return change
