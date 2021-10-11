from tkinter import *
from tkinter import ttk
import pyqrcode
from PIL import Image, ImageTk

root = Tk()
root.title("Abhiram B S")


def generateQR():
    name_website = name.get()
    url_website = url.get()
    file = name_website + ".png"
    qrcode = pyqrcode.create(url_website)
    qrcode.png(file, scale=8)
    img = ImageTk.PhotoImage(Image.open(file))
    image_label = ttk.Label(image=img)
    image_label.img = img
    canvas.create_window(200, 400, window=image_label)


canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = ttk.Label(root, text="QR Code Generators",
                      foreground="red", font="Arial 20")
canvas.create_window(200, 20, window=app_label)

name_label = ttk.Label(root, text="Name of The Website")
canvas.create_window(200, 80, window=name_label)

name = ttk.Entry(root)
canvas.create_window(200, 100, window=name)

url_label = ttk.Label(root, text="URL of The Website")
canvas.create_window(200, 130, window=url_label)

url = ttk.Entry(root)
canvas.create_window(200, 150, window=url)

btn = ttk.Button(text="Generate QR Code", command=generateQR)
canvas.create_window(200, 200, window=btn)

root.mainloop()
