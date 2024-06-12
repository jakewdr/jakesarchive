from PIL import Image
import pathlib
import os
import ntpath

def pathLeaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

imageFiles = [
        str(entry).replace(os.sep, "/")  # Appends a string of the file path with forward slashes
        for entry in pathlib.Path("./sourceImages").iterdir()  # For all the file entries in the directory
        if ".webp" or ".jpeg" or ".jpg" or ".png" in str(pathlib.Path(entry))
    ]

for images in imageFiles:
    image = Image.open(images)
    crop = (500, 500)
    left = round((image.size[0] - crop[0])/2)
    top = round((image.size[1] - crop[1])/2)
    image = image.crop((left, top, crop[0]+left, crop[1] + top))
    image.save(f"./images/{pathLeaf(images)}", 'webp', optimize = True, quality = 90)