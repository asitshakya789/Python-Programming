import tkinter as tk

win = tk.Tk()

win.title("Hey asit")
frame1 = tk.Frame(master=win, width=200,height=200,bg="yellow")
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame2= tk.Frame(master=win,width=100,height=100,bg="pink")
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame3 = tk.Frame(master=win,height=50 ,width=50,bg="red")
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

win.mainloop()