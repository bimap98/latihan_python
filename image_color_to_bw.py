from PIL import Image
from PIL import ImageFilter

gambar = Image.open("japan.jpg")
gambar_bw = gambar.convert("L")
gambar_bw.save("bw.jpg")
