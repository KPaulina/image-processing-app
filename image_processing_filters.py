import cv2 as cv
import cv2.cv2 as cv
import tkinter as tk
import matplotlib as plt
from matplotlib import pyplot as plt
from PIL import ImageTk
import numpy as np
from PIL import Image


def histogram(root, img):
    '''
    Function made to create histogram and show it in the app
    :param root:
    :param img:
    '''
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


def histogram_equlization(root, img):
    '''
    function made to create histogram equalization
    '''
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    equ = cv.equalizeHist(img)
    res = np.hstack((img, equ))
    cv.imwrite('result_img.png', res)

    window = tk.Toplevel(master=root)
    window.title("Histogram equalization")
    window.transient(root)
    window.grab_set()

    img_res = ImageTk.PhotoImage(Image.open("result_img.png"))
    lbl2 = tk.Label(window, image=img_res)
    lbl2.pack()

    def close_window():
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", close_window)
    root.wait_window(window)

def median_blur(root, img):
    '''
    Median filter for images
    '''
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_rst = cv.medianBlur(img, 5)
    cv.imwrite('result_img_1.png', img_rst)

    window = tk.Toplevel(master=root)
    window.title("Median blur")
    window.transient(root)
    window.grab_set()

    img_res = ImageTk.PhotoImage(Image.open("result_img_1.png"))
    lbl2 = tk.Label(window, image=img_res)
    lbl2.pack()
    lbl2.imnage = img_res

    def close_window():
        window.destroy()

        window.protocol("WM_DELETE_WINDOW", close_window)
        root.wait_window(window)
