import tkinter as tk

root = tk.Tk()
root.title("My GUI")

label = tk.Label(root,text="Hello Asit",bg='white',)
label.pack()

entry = tk.Entry(root,textvariable="hello")
entry.pack()

button= tk.Button(root,text='click here')
button.pack()

root.mainloop()