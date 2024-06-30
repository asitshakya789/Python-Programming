import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(master=win,width=100,height=100,bg="orange")
frame1.pack()

frame2 = tk.Frame(master=win,width=50,height=50,bg="black")
frame2.pack()

frame3 = tk.Frame(master=win,height=25,width=25,bg="green")
frame3.pack()

win.mainloop()