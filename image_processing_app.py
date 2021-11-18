import os
from tkinter import filedialog, Image, Toplevel, Label
import tkinter as tk
from PIL import ImageTk
import cv2.cv2 as cv
import cv2 as cv
from PIL import Image
import image_processing_filters

class App:

    def __init__(self, root):
        self.root = root
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=subMenu)
        subMenu.add_command(label='Load image', command=self.load_image)
        subMenu.add_command(label='New image', command=self.open_new_image)
        subMenu.add_command(label='Duplicate', command=self.duplicate)
        subMenu.add_command(label='Save file', command=self.save_file)
        subMenu.add_command(label='Exit', command=exit)

        editMenu = tk.Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Histogram', command=self.histogram)
        editMenu.add_command(label='Histogram equalization', command=self.histogram_equalization)
        editMenu.add_command(label='Rozciąganie histogramu', command=self.rozciaganie_histogramu)
        editMenu.add_command(label='Median blur', command=self.median_blur)

    def load_image(self):
        '''
        Function used to load image
        '''
        global my_image
        global path
        path = os.getcwd()
        self.root.filename = filedialog.askopenfilename(initialdir=path,
                                                         title="Select image",
                                                         filetypes=[
                                                             ("image", ".jpeg"),
                                                             ("image", ".png"),
                                                             ("image", ".jpg"),
                                                             ("image", ".bmp"),
                                                             ("image", ".tif"),
                                                         ])
        path = self.root.filename.replace ('/', '\\')
        global imgopen, my_image
        # imgopen = cv.imread(path)
        my_image = ImageTk.PhotoImage(Image.open(self.root.filename))
        Label(image=my_image).pack()

    def duplicate(self):
        '''
        Function used to duplicate image
        '''
        new_window = Toplevel(self.root)
        new_window.title('Nowy duplikat')
        img_clone = ImageTk.PhotoImage(Image.open(path))
        lbl2 = Label(new_window, image=img_clone)
        lbl2.pack()

        menu = tk.Menu(new_window)
        new_window.config(menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=subMenu)
        subMenu.add_command(label='Load image', command=self.load_image)
        subMenu.add_command(label='New image', command=self.open_new_image)
        subMenu.add_command(label='Duplicate', command=self.duplicate)
        subMenu.add_command(label='Exit', command=exit)

        editMenu = tk.Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Histogram for grayscale', command=self.histogram)
        editMenu.add_command (label='Histogram equalization', command=self.histogram_equalization)
        editMenu.add_command(label='Median blur', command=self.median_blur)
        new_window.mainloop()

    def load_image_internal(self):
        '''
        Function used to load image in a new window
        :return: image
        '''
        global internal_path
        count = 0
        internal_path = os.getcwd()
        name_of_path = []
        filename = filedialog.askopenfilename(initialdir=internal_path,
                                               title="Select image",
                                               filetypes=[
                                                   ("image", ".jpeg"),
                                                   ("image", ".png"),
                                                   ("image", ".jpg"),
                                                   ("image", ".bmp"),
                                                   ("image", ".tif"),
                                               ])
        if filename is not None:
            name_of_path.append(filename)
            count += 1
        print(name_of_path)
        count = count - 1
        print(count)
        if len(name_of_path) >= 1:
            internal_path = name_of_path[count]
        print(f' internal_path: {internal_path}')
        return ImageTk.PhotoImage(Image.open(name_of_path[count]))

    def open_new_image(self):
        '''
        Function used to load a new image
        '''
        new_image_window = Toplevel(self.root)
        new_image_window.title('New window')
        new_image_window.geometry("700x500")
        lbl2 = Label(new_image_window)
        lbl2.pack()

        def onClick():
            self.img = self.load_image_internal()
            lbl2.configure(image=self.img)
            new_image_window.update()

        load_image = tk.Button(new_image_window, text='Load image',
                                    command=onClick)
        load_image.pack()
        internal_menu = tk.Menu(new_image_window)
        new_image_window.config(menu=internal_menu)

        subMenu = tk.Menu(internal_menu)
        internal_menu.add_cascade(label='File', menu=subMenu)
        subMenu.add_command(label='New image', command=self.open_new_image)
        subMenu.add_command(label='Duplicate', command=self.duplicate)
        subMenu.add_command(label='Exit', command=exit)

        editMenu = tk.Menu(internal_menu)
        internal_menu.add_cascade(label='Edit', menu=editMenu)


    #metoda na zapisywanie plików
    def save_file(self):
        '''
        Function thanks to which image can be save with a chosen extension
        '''
        img = cv.imread(path)
        RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        edge = Image.fromarray(RGB_img)
        filename = filedialog.asksaveasfile(mode='wb', title="image", filetypes=(
            ("Image", "*.jpeg"),
            ("Image", "*.png"),
            ("Image", "*.jpg"),
            ("Image", "*.bmp"),
            ("Image", "*.tif")))
        if not filename:
            return
        edge.save(filename)

    def histogram(self):
        img = cv.imread(path)
        image_processing_filters.histogram(self.root, img)

    def histogram_equalization(self):
        img = cv.imread(path)
        image_processing_filters.histogram_equlization(self.root, img)

    def median_blur(self):
        img = cv.imread(path)
        image_processing_filters.median_blur(self.root, img)

    def rozciaganie_histogramu(self):
        img = cv.imread(path)
        image_processing_filters.rozciaganie_histogramu(self.root, img)


def main():
    root = tk.Tk()
    root.title('Program for image processing')
    root.geometry("500x500")
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()

