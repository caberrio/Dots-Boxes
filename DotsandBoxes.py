from tkinter import *
import dots


root=Tk() 
root.title("Dots & Boxes")
root.resizable(width=False, height=False)
root.geometry("600x600+30+30")


#LOGIC

class RC(object):
    def __init__(self):
        self.row1 = [False] * 6
        self.row2 = [False] * 6
        self.row3 = [False] * 6
        self.row4 = [False] * 6
        self.row5 = [False] * 6
        self.column1 = [False] * 6
        self.column2 = [False] * 6
        self.column3 = [False] * 6
        self.column4 = [False] * 6
        self.column5 = [False] * 6

class Board(object):
    def __init__(self, data):
        self.data = data
        self.gameboard =[[self.data.row1[0],self.data.row1[1],self.data.column1[0],self.data.column1[1]],
                         [self.data.row1[1],self.data.row1[2],self.data.column2[0],self.data.column2[1]],
                         [self.data.row1[2],self.data.row1[3],self.data.column3[0],self.data.column3[1]],
                         [self.data.row1[3],self.data.row1[4],self.data.column4[0],self.data.column4[1]],
                         [self.data.row1[4],self.data.row1[5],self.data.column5[0],self.data.column5[1]],
                         [self.data.row2[0],self.data.row2[1],self.data.column1[1],self.data.column1[2]],
                         [self.data.row2[1],self.data.row2[2],self.data.column2[1],self.data.column2[2]],
                         [self.data.row2[2],self.data.row2[3],self.data.column3[1],self.data.column3[2]],
                         [self.data.row2[3],self.data.row2[4],self.data.column4[1],self.data.column4[2]],
                         [self.data.row2[4],self.data.row2[5],self.data.column5[1],self.data.column5[2]],
                         [self.data.row3[0],self.data.row3[1],self.data.column1[2],self.data.column1[3]],
                         [self.data.row3[1],self.data.row3[2],self.data.column2[2],self.data.column2[3]],
                         [self.data.row3[2],self.data.row3[3],self.data.column3[2],self.data.column3[3]],
                         [self.data.row3[3],self.data.row3[4],self.data.column4[2],self.data.column4[3]],
                         [self.data.row3[4],self.data.row3[5],self.data.column5[2],self.data.column5[3]],
                         [self.data.row4[0],self.data.row4[1],self.data.column1[3],self.data.column1[4]],
                         [self.data.row4[1],self.data.row4[2],self.data.column2[3],self.data.column2[4]],
                         [self.data.row4[2],self.data.row4[3],self.data.column3[3],self.data.column3[4]],
                         [self.data.row4[3],self.data.row4[4],self.data.column4[3],self.data.column4[4]],
                         [self.data.row4[4],self.data.row4[5],self.data.column5[3],self.data.column5[4]],
                         [self.data.row5[0],self.data.row5[1],self.data.column1[4],self.data.column1[5]],
                         [self.data.row5[1],self.data.row5[2],self.data.column2[4],self.data.column2[5]],
                         [self.data.row5[2],self.data.row5[3],self.data.column3[4],self.data.column3[5]],
                         [self.data.row5[3],self.data.row5[4],self.data.column4[4],self.data.column4[5]],
                         [self.data.row5[4],self.data.row5[5],self.data.column5[4],self.data.column5[5]],]





def create_board(*state):
    if str(type("")) == "<class '__main__.RC'>":
        return Board(state)
    else:
        data = RC()
        return Board(data)
    
def update_board(state):
    return Board(state)
data = RC()
board = create_board(data)
#print (board.gameboard)
data.column1[2]=True
data.row2[3]=True        
board = update_board(data)
#print (board.gameboard)
print(board.gameboard[1][1])


def is_valid_move(data,d,dn,pos):
    if(d=='r'):
        direction=getattr(data,'row'+str(dn))
        return not direction[pos-1]
    else:
        direction=getattr(data,'column'+str(dn))
        return not direction[pos-1]

#LOGIC

canvas = Canvas(root)

for j in range(0,6):
            for i in range(0,6):
                canvas.create_oval(i*80+100, j*80+100, (i+1)*80, (j+1)*80, outline="blue",
                                fill="blue", width=2)


canvas.pack(fill=BOTH, expand=1)



def callback(event):
    print ("clicked at", event.x, event.y)
    if(event.x > 80 and event.x < 100 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,1)):
        canvas.create_line(90, 100, 90, 160, fill="red", width=10)
        print("row1")
    if(event.x > 80 and event.x < 100 and event.y > 180 and event.y < 240):
        canvas.create_line(90, 180, 90, 240, fill="red", width=10)
        
    if(event.x > 80 and event.x < 100 and event.y > 260 and event.y < 320):
        canvas.create_line(90, 260, 90, 320, fill="red", width=10)
        
    if(event.x > 80 and event.x < 100 and event.y > 340 and event.y < 400):
        canvas.create_line(90, 340, 90, 400, fill="red", width=10)
        
    if(event.x > 80 and event.x < 100 and event.y > 420 and event.y < 480):
        canvas.create_line(90, 420, 90, 480, fill="red", width=10)
        
    if(event.x > 160 and event.x < 180 and event.y > 100 and event.y < 160):
        canvas.create_line(170, 100, 170, 160, fill="red", width=10)
        
    if(event.x > 160 and event.x < 180 and event.y > 180 and event.y < 240):
        canvas.create_line(170, 180, 170, 240, fill="red", width=10)
        
    if(event.x > 160 and event.x < 180 and event.y > 260 and event.y < 320):
        canvas.create_line(170, 260, 170, 320, fill="red", width=10)
        
    if(event.x > 160 and event.x < 180 and event.y > 340 and event.y < 400):
        canvas.create_line(170, 340, 170, 400, fill="red", width=10)
        
    if(event.x > 160 and event.x < 180 and event.y > 420 and event.y < 480):
        canvas.create_line(170, 420, 170, 480, fill="red", width=10)
    
    if(event.x > 240 and event.x < 260 and event.y > 100 and event.y < 160):
        canvas.create_line(250, 100, 250, 160, fill="red", width=10)
        
    if(event.x > 240 and event.x < 260 and event.y > 180 and event.y < 240):
        canvas.create_line(250, 180, 250, 240, fill="red", width=10)
        
    if(event.x > 240 and event.x < 260 and event.y > 260 and event.y < 320):
        canvas.create_line(250, 260, 250, 320, fill="red", width=10)
    
    if(event.x > 240 and event.x < 260 and event.y > 340 and event.y < 400):
        canvas.create_line(250, 340, 250, 400, fill="red", width=10)
        
    if(event.x > 240 and event.x < 260 and event.y > 420 and event.y < 480):
        canvas.create_line(250, 420, 250, 480, fill="red", width=10)
        
    if(event.x > 320 and event.x < 340 and event.y > 100 and event.y < 160):
        canvas.create_line(330, 100, 330, 160, fill="red", width=10)
        
    if(event.x > 320 and event.x < 340 and event.y > 180 and event.y < 240):
        canvas.create_line(330, 180, 330, 240, fill="red", width=10)
        
    if(event.x > 320 and event.x < 340 and event.y > 260 and event.y < 320):
        canvas.create_line(330, 260, 330, 320, fill="red", width=10)
        
    if(event.x > 320 and event.x < 340 and event.y > 340 and event.y < 400):
        canvas.create_line(330, 340, 330, 400, fill="red", width=10)
    
    if(event.x > 320 and event.x < 340 and event.y > 420 and event.y < 480):
        canvas.create_line(330, 420, 330, 480, fill="red", width=10)
        
    if(event.x > 400 and event.x < 420 and event.y > 100 and event.y < 160):
        canvas.create_line(410, 100, 410, 160, fill="red", width=10)
        
    if(event.x > 400 and event.x < 420 and event.y > 180 and event.y < 240):
        canvas.create_line(410, 180, 410, 240, fill="red", width=10)
        
    if(event.x > 400 and event.x < 420 and event.y > 260 and event.y < 320):
        canvas.create_line(410, 260, 410, 320, fill="red", width=10)
        
    if(event.x > 400 and event.x < 420 and event.y > 340 and event.y < 400):
        canvas.create_line(410, 340, 410, 400, fill="red", width=10)
        
    if(event.x > 400 and event.x < 420 and event.y > 420 and event.y < 480):
        canvas.create_line(410, 420, 410, 480, fill="red", width=10)
        
    if(event.x > 480 and event.x < 500 and event.y > 100 and event.y < 160):
        canvas.create_line(490, 100, 490, 160, fill="red", width=10)
    
    if(event.x > 480 and event.x < 500 and event.y > 180 and event.y < 240):
        canvas.create_line(490, 180, 490, 240, fill="red", width=10)
    
    if(event.x > 480 and event.x < 500 and event.y > 260 and event.y < 320):
        canvas.create_line(490, 260, 490, 320, fill="red", width=10)
    
    if(event.x > 480 and event.x < 500 and event.y > 340 and event.y < 400):
        canvas.create_line(490, 340, 490, 400, fill="red", width=10)
        
    if(event.x > 480 and event.x < 500 and event.y > 420 and event.y < 480):
        canvas.create_line(490, 420, 490, 480, fill="red", width=10)
        
    if(event.x > 100 and event.x < 160 and event.y > 80 and event.y < 100):        
        canvas.create_line(100, 90, 160, 90, fill="red", width=10)
        
    if(event.x > 100 and event.x < 160 and event.y > 160 and event.y < 180):        
        canvas.create_line(100, 170, 160, 170, fill="red", width=10)
    
    if(event.x > 100 and event.x < 160 and event.y > 240 and event.y < 260):
        canvas.create_line(100, 250, 160, 250, fill="red", width=10)
        
    if(event.x > 100 and event.x < 160 and event.y > 320 and event.y < 340):
        canvas.create_line(100, 330, 160, 330, fill="red", width=10)
        
    if(event.x > 100 and event.x < 160 and event.y > 400 and event.y < 420):
        canvas.create_line(100, 410, 160, 410, fill="red", width=10)
        
    if(event.x > 100 and event.x < 160 and event.y > 480 and event.y < 500):
        canvas.create_line(100, 490, 160, 490, fill="red", width=10)
        
    if(event.x > 180 and event.x < 240 and event.y > 80 and event.y < 100):        
        canvas.create_line(180, 90, 240, 90, fill="red", width=10)
        
    if(event.x > 180 and event.x < 240 and event.y > 160 and event.y < 180):        
        canvas.create_line(180, 170, 240, 170, fill="red", width=10)
        
    if(event.x > 180 and event.x < 240 and event.y > 240 and event.y < 260):
        canvas.create_line(180, 250, 240, 250, fill="red", width=10)

    if(event.x > 180 and event.x < 240 and event.y > 320 and event.y < 340):
        canvas.create_line(180, 330, 240, 330, fill="red", width=10)

    if(event.x > 180 and event.x < 240 and event.y > 400 and event.y < 420):
        canvas.create_line(180, 410, 240, 410, fill="red", width=10)
        
    if(event.x > 180 and event.x < 240 and event.y > 480 and event.y < 500):
        canvas.create_line(180, 490, 240, 490, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 80 and event.y < 100):        
        canvas.create_line(260, 90, 320, 90, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 160 and event.y < 180):        
        canvas.create_line(260, 170, 320, 170, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 240 and event.y < 260):
        canvas.create_line(260, 250, 320, 250, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 320 and event.y < 340):
        canvas.create_line(260, 330, 320, 330, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 400 and event.y < 420):
        canvas.create_line(260, 410, 320, 410, fill="red", width=10)
        
    if(event.x > 260 and event.x < 320 and event.y > 480 and event.y < 500):
        canvas.create_line(260, 490, 320, 490, fill="red", width=10)
        
    if(event.x > 340 and event.x < 400 and event.y > 80 and event.y < 100):        
        canvas.create_line(340, 90, 400, 90, fill="red", width=10)
        
    if(event.x > 340 and event.x < 400 and event.y > 160 and event.y < 180):        
        canvas.create_line(340, 170, 400, 170, fill="red", width=10)
        
    if(event.x > 340 and event.x < 400 and event.y > 240 and event.y < 260):
        canvas.create_line(340, 250, 400, 250, fill="red", width=10)
        
    if(event.x > 340 and event.x < 400 and event.y > 320 and event.y < 340):
        canvas.create_line(340, 330, 400, 330, fill="red", width=10)
    
    if(event.x > 340 and event.x < 400 and event.y > 400 and event.y < 420):
        canvas.create_line(340, 410, 400, 410, fill="red", width=10)
        
    if(event.x > 340 and event.x < 400 and event.y > 480 and event.y < 500):
        canvas.create_line(340, 490, 400, 490, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 80 and event.y < 100):        
        canvas.create_line(420, 90, 480, 90, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 160 and event.y < 180):        
        canvas.create_line(420, 170, 480, 170, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 240 and event.y < 260):
        canvas.create_line(420, 250, 480, 250, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 320 and event.y < 340):
        canvas.create_line(420, 330, 480, 330, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 400 and event.y < 420):
        canvas.create_line(420, 410, 480, 410, fill="red", width=10)
        
    if(event.x > 420 and event.x < 480 and event.y > 480 and event.y < 500):
        canvas.create_line(420, 490, 480, 490, fill="red", width=10)
        


canvas.bind("<Button-1>", callback)



root.mainloop()
