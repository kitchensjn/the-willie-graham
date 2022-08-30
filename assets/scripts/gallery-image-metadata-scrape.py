import glob
from PIL import Image, IptcImagePlugin

images = glob.glob("../images/gallery/*")
for image in images:
    img = Image.open(image)
    iptc = IptcImagePlugin.getiptcinfo(img)

    empty = "".encode()

    #date = None
    #if iptc.get((2, 55), "") != "":
    #    date = iptc[(2, 55)].decode()
    #    date = "-".join([date[:4], date[4:6], date[6:]])

    location=iptc.get((2, 92), empty).decode()
    headline=iptc.get((2, 105), empty).decode()
    description=iptc.get((2, 120), empty).decode()
    creator=iptc.get((2, 122), empty).decode()
    city=iptc.get((2, 90), empty).decode()
    state=iptc.get((2, 95), empty).decode()
    country=iptc.get((2, 101), empty).decode()
    copyright=iptc.get((2, 116), empty).decode()
    encoded_categories=iptc.get((2, 25), empty)
    categories = []
    for cat in encoded_categories:
        categories.append(cat.decode())

