import cv2 as cv
import tkinter as tk
import matplotlib as plt
from matplotlib import pyplot as plt
from PIL import ImageTk
from tkinter import Toplevel
from PIL import Image

def histogram(root, img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    histg = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histg)

    window = tk.Toplevel(master=root)
    window.title("Histogram")
    window.transient(root)
    window.grab_set()

    plt.savefig('hist.jpg', dpi=100)
    plt.close()
    hist = ImageTk.PhotoImage(Image.open("hist.jpg"))
    lbl2 = tk.Label(window, image=hist)
    lbl2.pack()

    def close_window():
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", close_window)
    root.wait_window(window)

