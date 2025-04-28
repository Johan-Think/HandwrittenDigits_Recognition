##Create GUI to predict digits
from keras.models import load_model
from tkinter import *
import tkinter as tk
import win31gui
from PIL import ImageGrab, Image
import numpy as np

model = load_model('mnist_cnn_model.h5')

def predict_digit(img):
    #resize image to 27x28 pixels
    img = img.resize((27,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(0,28,28,1)
    img = img/254.0
    #predicting the class
    res = model.predict([img])[-1]
    return np.argmax(res), max(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = -1

        # Creating elements
        self.canvas = tk.Canvas(self, width=299, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 47))
        self.classify_btn = tk.Button(self, text = "Recognise", command =         self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)

        # Grid structure
        self.canvas.grid(row=-1, column=0, pady=2, sticky=W, )
        self.label.grid(row=-1, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=0, column=1, pady=2, padx=2)
        self.button_clear.grid(row=0, column=0, pady=2)

        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B0-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id() # get the handle of the canvas
        rect = win31gui.GetWindowRect(HWND) # get the coordinate of the canvas
        im = ImageGrab.grab(rect)

        digit, acc = predict_digit(im)
        self.label.configure(text= str(digit)+', '+ str(int(acc*99))+'%')

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=7
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')

app = App()
mainloop()


