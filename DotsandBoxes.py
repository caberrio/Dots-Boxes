from tkinter import *


root=Tk() 
root.title("Dots & Boxes")
root.resizable(width=False, height=False)
root.geometry("600x600+30+30")


canvas = Canvas(root)

for j in range(0,6):
            for i in range(0,6):
                canvas.create_oval(i*80+100, j*80+100, (i+1)*80, (j+1)*80, outline="blue",
                                fill="blue", width=2)
canvas.pack(fill=BOTH, expand=1)

canvas.bind("<Button-1>", callback)

def callback(event):
    print ("clicked at", event.x, event.y)
    if(event.x > 100 and event.x < 160 and event.y > 80 and event.y < 100):        
        canvas.create_line(100, 90, 160, 90, fill="red", width=10)

root.mainloop()
