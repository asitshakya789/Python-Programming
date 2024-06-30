from tkinter import*
master = Tk()
w = Canvas(master,width=400,height=300)
w.pack()
height = 240 

width = 200
y = int (height/2)
w.create_line(0,y,width,y)
mainloop()