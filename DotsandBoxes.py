from tkinter import *
"""root=Tk()
root.resizable(width=False, height=False)
"""
class Example(Frame):
 
    def __init__(self, parent):
        Frame.__init__(self, parent)  
         
        self.parent = parent        
        self.initUI()
       
       
    def initUI(self):
     
        self.parent.title("Dots & Boxes")        
        self.pack(fill=BOTH, expand=1)
       
        canvas = Canvas(self)
        canvas.bind("<Key>", key)
        canvas.bind("<Button-1>", callback)
        for j in range(0,6):
            for i in range(0,6):
                canvas.create_oval(i*80+100, j*80+100, (i+1)*80, (j+1)*80, outline="blue",
                                fill="blue", width=2)

        canvas.pack(fill=BOTH, expand=1)
def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    print ("clicked at", event.x, event.y)


 
def main():
 
    root = Tk()
    ex = Example(root)
    root.geometry("600x600+30+30")
    root.mainloop()  
 
 
if __name__ == '__main__':

        main()
