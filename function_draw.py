from PIL import Image, ImageDraw
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
                im_size = im.size
                im_draw = ImageDraw.Draw(im)
                im_draw.rectangle([(im_size[0]/2-im.size[0]/6, im_size[1]/2-im.size[0]/6),
                                   (im_size[0]/2+im.size[0]/6, im_size[1]/2+im.size[0]/6)], fill='black')
                im.save(name + '.' + new_ext)
                del im_draw
                os.remove(file_name)
    return change
