from sys import argv
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

try:
    img = Image.open(argv[1])
except IndexError:
    print('Usage: python metadata.py /path/to/file.jpg')
    exit(1)

exifdata = img.getexif()

for tagid in exifdata:
    tagname = TAGS.get(tagid, tagid)
    value = exifdata.get(tagid)

    print(f"{tagname:25}: {value}")
