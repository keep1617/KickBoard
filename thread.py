from tkinter import *
import subprocess
import random




def event():
    while(True):
        boolean_value = random.choice([True, False])
        if boolean_value == True:
            result_label.config(text=f'반납완료')
            break
tk = Tk()

button = Button(tk,text = '반납시작', command = event)
result_label = Label(tk, text='Boolean 값: None')

button.pack( padx = 10, pady = 10)
result_label.pack()


tk.mainloop()