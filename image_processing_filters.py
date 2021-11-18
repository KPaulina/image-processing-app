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

def rozciaganie_histogramu(root, img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    copied_image = img.copy()

    dlg = tk.Toplevel (master=root)
    dlg.geometry("600x300")
    dlg.title("Rozciąganie histogramu")
    dlg.transient(root)
    dlg.grab_set()

    win_h = tk.Toplevel (master=root)
    win_h.geometry("600x300")
    win_h.title("Rozciąganie histogramu")
    win_h.transient(root)
    win_h.grab_set()


    img_w = tk.Toplevel (master=root)
    img_w.geometry("600x500")
    img_w.title("Rozciąganie histogramu")
    img_w.transient(root)
    img_w.grab_set()

    def lut_table(img):
        """tworzenie tablicy lut"""
        #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        row = img.shape[0]
        col = img.shape[1]
        # algortym do tworzenia histogramu
        y = [0] * 256
        for n in range (0, row):
            for r in range (0, col):
                y[img[n, r]] += 1
        return y
    lut = lut_table(img)

    min_value = 0
    max_value = 0

    for i, element in enumerate(lut):
        if element != 0:
            min_value = i
    print(min_value)
    lut_reversed = reversed(lut)
    for i, element in enumerate(lut_reversed):
        if element != 0:
            max_value = i
    print(max_value)
    con = 255 / max_value - min_value
    rlen = len(img)  # wielkosc w pionie
    clen = len(img[0])  # wielkosc w poziomie
    for r in range(0, rlen):
        for c in range(0, clen):
            img[r][c] = (img[r][c] - min_value) * 255/max_value - min_value

    cv.imwrite('Stretched.png', img)
    img_big = ImageTk.PhotoImage(Image.open('Stretched.png'))
    img_label_3 = tk.Label(img_w, image=img_big)
    img_label_3.pack()

    plt.hist(img.ravel(), 256, [0, 256])
    plt.savefig('hist.jpg', dpi=100)
    plt.close()

    hist = ImageTk.PhotoImage(Image.open("hist.jpg"))
    lbl2 = tk.Label(dlg, image=hist)
    lbl2.pack()

    plt.hist(copied_image.ravel(), 256, [0, 256])
    plt.savefig('hist_original.jpg', dpi=100)
    plt.close()

    hist_or = ImageTk.PhotoImage(Image.open("hist_original.jpg"))
    lbl2 = tk.Label(win_h, image=hist_or)
    lbl2.pack()

    def close_window():
        img_w.destroy()

    img_w.protocol("WM_DELETE_WINDOW", close_window)

    root.wait_window(img_w)

    def close_window():
        dlg.destroy()

    dlg.protocol("WM_DELETE_WINDOW", close_window)

    root.wait_window(dlg)

    def close_window():
        win_h.destroy()

    win_h.protocol("WM_DELETE_WINDOW", close_window)

    root.wait_window(win_h)
