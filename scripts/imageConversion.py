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
    width, height = image.size
    print(width, height)
    if width != height:
        image = image.crop(((width - min(image.size)) // 2,
                            (height - min(image.size)) // 2,
                            (width + min(image.size)) // 2,
                            (height + min(image.size)) // 2))

    image = image.resize((500,500))
    if ".png" in images:
        image.save(f"./images/{pathLeaf(images)}".replace(".png", ".webp"), 'webp', optimize = True, quality = 90)
    else:
        image.save(f"./images/{pathLeaf(images)}", 'webp', optimize = True, quality = 90)