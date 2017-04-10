from tkinter import *
import heuristic


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
        self.painted = [False,False,False,False,False,False,False,False,False,False
                        ,False,False,False,False,False,False,False,False,False,False
                        ,False,False,False,False,False]



def create_board(*state):
    if str(type("")) == "<class '__main__.RC'>":
        return Board(state)
    else:
        data = RC()
        return Board(data)
    
def update_board(state):
    print('Change')
    return Board(state)


def make_a_move(data,d,dn,pos):
    if(d=='r'):
        direction=getattr(data,'row'+str(dn))
        direction[pos-1]=True
        setattr(data, 'row'+str(dn), direction)   
    else:
        direction=getattr(data,'column'+str(dn))
        direction[pos-1]=True
        setattr(data, 'column'+str(dn), direction)  
        
      
    return update_board(data)


def is_valid_move(data,d,dn,pos):
    if(d=='r'):
        direction=getattr(data,'row'+str(dn))
        return not direction[pos-1]
    else:
        direction=getattr(data,'column'+str(dn))
        return not direction[pos-1]

data = RC()
board = create_board(data)
boxes = heuristic.count_filled_boxes(board.gameboard)
turno_jugador = True

#LOGIC

canvas = Canvas(root)

for j in range(0,6):
            for i in range(0,6):
                canvas.create_oval(i*80+100, j*80+100, (i+1)*80, (j+1)*80, outline="blue",
                                fill="blue", width=2)


canvas.pack(fill=BOTH, expand=1)

def paint(x,y,d,dn,pos):
    global board    
    if(((x > 80 and x < 100 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 1)) and is_valid_move(data,"r",1,1)):
        board = make_a_move(data,"r",1,1)            
        canvas.create_line(90, 100, 90, 160, fill="red", width=10)
        
    elif(((x > 80 and x < 100 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 1)) and is_valid_move(data,"r",2,1)):
        board = make_a_move(data,"r",2,1)            
        canvas.create_line(90, 180, 90, 240, fill="red", width=10)        
        
    elif(((x > 80 and x < 100 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 1)) and is_valid_move(data,"r",3,1)):
        board = make_a_move(data,"r",3,1)            
        canvas.create_line(90, 260, 90, 320, fill="red", width=10)
        
    elif(((x > 80 and x < 100 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 1)) and is_valid_move(data,"r",4,1)):
        board = make_a_move(data,"r",4,1)            
        canvas.create_line(90, 340, 90, 400, fill="red", width=10)
        
    elif(((x > 80 and x < 100 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 1)) and is_valid_move(data,"r",5,1)):
        board = make_a_move(data,"r",5,1)            
        canvas.create_line(90, 420, 90, 480, fill="red", width=10)
        
    elif(((x > 160 and x < 180 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 2)) and is_valid_move(data,"r",1,2)):
        board = make_a_move(data,"r",1,2)            
        canvas.create_line(170, 100, 170, 160, fill="red", width=10)
        
    elif(((x > 160 and x < 180 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 2)) and is_valid_move(data,"r",2,2)):
        board = make_a_move(data,"r",2,2)            
        canvas.create_line(170, 180, 170, 240, fill="red", width=10)
        
    elif(((x > 160 and x < 180 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 2)) and is_valid_move(data,"r",3,2)):
        board = make_a_move(data,"r",3,2)            
        canvas.create_line(170, 260, 170, 320, fill="red", width=10)
        
    elif(((x > 160 and x < 180 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 2)) and is_valid_move(data,"r",4,2)):
        board = make_a_move(data,"r",4,2)            
        canvas.create_line(170, 340, 170, 400, fill="red", width=10)
        
    elif(((x > 160 and x < 180 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 2)) and is_valid_move(data,"r",5,2)):
        board = make_a_move(data,"r",5,2)        
        canvas.create_line(170, 420, 170, 480, fill="red", width=10)
    
    elif(((x > 240 and x < 260 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 3)) and is_valid_move(data,"r",1,3)):
        board = make_a_move(data,"r",1,3)
        canvas.create_line(250, 100, 250, 160, fill="red", width=10)
        
    elif(((x > 240 and x < 260 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 3)) and is_valid_move(data,"r",2,3)):
        board = make_a_move(data,"r",2,3)
        canvas.create_line(250, 180, 250, 240, fill="red", width=10)
        
    elif(((x > 240 and x < 260 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 3)) and is_valid_move(data,"r",3,3)):
        board = make_a_move(data,"r",3,3)
        canvas.create_line(250, 260, 250, 320, fill="red", width=10)
    
    elif(((x > 240 and x < 260 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 3)) and is_valid_move(data,"r",4,3)):
        board = make_a_move(data,"r",4,3)
        canvas.create_line(250, 340, 250, 400, fill="red", width=10)
        
    elif(((x > 240 and x < 260 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 3)) and is_valid_move(data,"r",5,3)):
        board = make_a_move(data,"r",5,3)
        canvas.create_line(250, 420, 250, 480, fill="red", width=10)
        
    elif(((x > 320 and x < 340 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 4)) and is_valid_move(data,"r",1,4)):
        board = make_a_move(data,"r",1,4)
        canvas.create_line(330, 100, 330, 160, fill="red", width=10)
        
    elif(((x > 320 and x < 340 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 4)) and is_valid_move(data,"r",2,4)):
        board = make_a_move(data,"r",2,4)
        canvas.create_line(330, 180, 330, 240, fill="red", width=10)
        
    elif(((x > 320 and x < 340 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 4)) and is_valid_move(data,"r",3,4)):
        board = make_a_move(data,"r",3,4)
        canvas.create_line(330, 260, 330, 320, fill="red", width=10)
        
    elif(((x > 320 and x < 340 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 4)) and is_valid_move(data,"r",4,4)):
        board = make_a_move(data,"r",4,4)
        canvas.create_line(330, 340, 330, 400, fill="red", width=10)
    
    elif(((x > 320 and x < 340 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 4)) and is_valid_move(data,"r",5,4)):
        board = make_a_move(data,"r",5,4)
        canvas.create_line(330, 420, 330, 480, fill="red", width=10)
        
    elif(((x > 400 and x < 420 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 5)) and is_valid_move(data,"r",1,5)):
        board = make_a_move(data,"r",1,5)
        canvas.create_line(410, 100, 410, 160, fill="red", width=10)
        
    elif(((x > 400 and x < 420 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 5)) and is_valid_move(data,"r",2,5)):
        board = make_a_move(data,"r",2,5)
        canvas.create_line(410, 180, 410, 240, fill="red", width=10)
        
    elif(((x > 400 and x < 420 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 5)) and is_valid_move(data,"r",3,5)):
        board = make_a_move(data,"r",3,5)
        canvas.create_line(410, 260, 410, 320, fill="red", width=10)
        
    elif(((x > 400 and x < 420 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 5)) and is_valid_move(data,"r",4,5)):
        board = make_a_move(data,"r",4,5)
        canvas.create_line(410, 340, 410, 400, fill="red", width=10)
        
    elif(((x > 400 and x < 420 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 5)) and is_valid_move(data,"r",5,5)):
        board = make_a_move(data,"r",5,5)
        canvas.create_line(410, 420, 410, 480, fill="red", width=10)
        
    elif(((x > 480 and x < 500 and y > 100 and y < 160) or (d == 'r' and dn == 1 and pos == 6)) and is_valid_move(data,"r",1,6)):
        board = make_a_move(data,"r",1,6)
        canvas.create_line(490, 100, 490, 160, fill="red", width=10)
    
    elif(((x > 480 and x < 500 and y > 180 and y < 240) or (d == 'r' and dn == 2 and pos == 6)) and is_valid_move(data,"r",2,6)):
        board = make_a_move(data,"r",2,6)
        canvas.create_line(490, 180, 490, 240, fill="red", width=10)
    
    elif(((x > 480 and x < 500 and y > 260 and y < 320) or (d == 'r' and dn == 3 and pos == 6)) and is_valid_move(data,"r",3,6)):
        board = make_a_move(data,"r",3,6)
        canvas.create_line(490, 260, 490, 320, fill="red", width=10)
    
    elif(((x > 480 and x < 500 and y > 340 and y < 400) or (d == 'r' and dn == 4 and pos == 6)) and is_valid_move(data,"r",4,6)):
        board = make_a_move(data,"r",4,6)
        canvas.create_line(490, 340, 490, 400, fill="red", width=10)
        
    elif(((x > 480 and x < 500 and y > 420 and y < 480) or (d == 'r' and dn == 5 and pos == 6)) and is_valid_move(data,"r",5,6)):
        board = make_a_move(data,"r",5,6)
        canvas.create_line(490, 420, 490, 480, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 80 and y < 100) or (d == 'c' and dn == 1 and pos == 1)) and is_valid_move(data,"c",1,1)):
        board = make_a_move(data,"c",1,1)
        canvas.create_line(100, 90, 160, 90, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 160 and y < 180) or (d == 'c' and dn == 1 and pos == 2)) and is_valid_move(data,"c",1,2)):
        board = make_a_move(data,"c",1,2)
        canvas.create_line(100, 170, 160, 170, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 240 and y < 260) or (d == 'c' and dn == 1 and pos == 3)) and is_valid_move(data,"c",1,3)):
        board = make_a_move(data,"c",1,3)
        canvas.create_line(100, 250, 160, 250, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 320 and y < 340) or (d == 'c' and dn == 1 and pos == 4)) and is_valid_move(data,"c",1,4)):
        board = make_a_move(data,"c",1,4)
        canvas.create_line(100, 330, 160, 330, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 400 and y < 420) or (d == 'c' and dn == 1 and pos == 5)) and is_valid_move(data,"c",1,5)):
        board = make_a_move(data,"c",1,5)
        canvas.create_line(100, 410, 160, 410, fill="red", width=10)
        
    elif(((x > 100 and x < 160 and y > 480 and y < 500) or (d == 'c' and dn == 1 and pos == 6)) and is_valid_move(data,"c",1,6)):
        board = make_a_move(data,"c",1,6)
        canvas.create_line(100, 490, 160, 490, fill="red", width=10)
        
    elif(((x > 180 and x < 240 and y > 80 and y < 100) or (d == 'c' and dn == 2 and pos == 1)) and is_valid_move(data,"c",2,1)):
        board = make_a_move(data,"c",2,1)
        canvas.create_line(180, 90, 240, 90, fill="red", width=10)
        
    elif(((x > 180 and x < 240 and y > 160 and y < 180) or (d == 'c' and dn == 2 and pos == 2)) and is_valid_move(data,"c",2,2)):
        board = make_a_move(data,"c",2,2)
        canvas.create_line(180, 170, 240, 170, fill="red", width=10)
        
    elif(((x > 180 and x < 240 and y > 240 and y < 260) or (d == 'c' and dn == 2 and pos == 3)) and is_valid_move(data,"c",2,3)):
        board = make_a_move(data,"c",2,3)
        canvas.create_line(180, 250, 240, 250, fill="red", width=10)

    elif(((x > 180 and x < 240 and y > 320 and y < 340) or (d == 'c' and dn == 2 and pos == 4)) and is_valid_move(data,"c",2,4)):
        board = make_a_move(data,"c",2,4)
        canvas.create_line(180, 330, 240, 330, fill="red", width=10)

    elif(((x > 180 and x < 240 and y > 400 and y < 420) or (d == 'c' and dn == 2 and pos == 5)) and is_valid_move(data,"c",2,5)):
        board = make_a_move(data,"c",2,5)
        canvas.create_line(180, 410, 240, 410, fill="red", width=10)
        
    elif(((x > 180 and x < 240 and y > 480 and y < 500) or (d == 'c' and dn == 2 and pos == 6)) and is_valid_move(data,"c",2,6)):
        board = make_a_move(data,"c",2,6)
        canvas.create_line(180, 490, 240, 490, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 80 and y < 100) or (d == 'c' and dn == 3 and pos == 1)) and is_valid_move(data,"c",3,1)):
        board = make_a_move(data,"c",3,1)
        canvas.create_line(260, 90, 320, 90, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 160 and y < 180) or (d == 'c' and dn == 3 and pos == 2)) and is_valid_move(data,"c",3,2)):
        board = make_a_move(data,"c",3,2)
        canvas.create_line(260, 170, 320, 170, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 240 and y < 260) or (d == 'c' and dn == 3 and pos == 3)) and is_valid_move(data,"c",3,3)):
        board = make_a_move(data,"c",3,3)
        canvas.create_line(260, 250, 320, 250, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 320 and y < 340) or (d == 'c' and dn == 3 and pos == 4)) and is_valid_move(data,"c",3,4)):
        board = make_a_move(data,"c",3,4)
        canvas.create_line(260, 330, 320, 330, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 400 and y < 420) or (d == 'c' and dn == 3 and pos == 5)) and is_valid_move(data,"c",3,5)):
        board = make_a_move(data,"c",3,5)
        canvas.create_line(260, 410, 320, 410, fill="red", width=10)
        
    elif(((x > 260 and x < 320 and y > 480 and y < 500) or (d == 'c' and dn == 3 and pos == 6)) and is_valid_move(data,"c",3,6)):
        board = make_a_move(data,"c",3,6)
        canvas.create_line(260, 490, 320, 490, fill="red", width=10)
        
    elif(((x > 340 and x < 400 and y > 80 and y < 100) or (d == 'c' and dn == 4 and pos == 1)) and is_valid_move(data,"c",4,1)):
        board = make_a_move(data,"c",4,1)
        canvas.create_line(340, 90, 400, 90, fill="red", width=10)
        
    elif(((x > 340 and x < 400 and y > 160 and y < 180) or (d == 'c' and dn == 4 and pos == 2)) and is_valid_move(data,"c",4,2)):
        board = make_a_move(data,"c",4,2)
        canvas.create_line(340, 170, 400, 170, fill="red", width=10)
        
    elif(((x > 340 and x < 400 and y > 240 and y < 260) or (d == 'c' and dn == 4 and pos == 3)) and is_valid_move(data,"c",4,3)):
        board = make_a_move(data,"c",4,3)
        canvas.create_line(340, 250, 400, 250, fill="red", width=10)
        
    elif(((x > 340 and x < 400 and y > 320 and y < 340) or (d == 'c' and dn == 4 and pos == 4)) and is_valid_move(data,"c",4,4)):
        board = make_a_move(data,"c",4,4)
        canvas.create_line(340, 330, 400, 330, fill="red", width=10)
    
    elif(((x > 340 and x < 400 and y > 400 and y < 420) or (d == 'c' and dn == 4 and pos == 5)) and is_valid_move(data,"c",4,5)):
        board = make_a_move(data,"c",4,5)
        canvas.create_line(340, 410, 400, 410, fill="red", width=10)
        
    elif(((x > 340 and x < 400 and y > 480 and y < 500) or (d == 'c' and dn == 4 and pos == 6)) and is_valid_move(data,"c",4,6)):
        board = make_a_move(data,"c",4,6)
        canvas.create_line(340, 490, 400, 490, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 80 and y < 100) or (d == 'c' and dn == 5 and pos == 1)) and is_valid_move(data,"c",5,1)):
        board = make_a_move(data,"c",5,1)
        canvas.create_line(420, 90, 480, 90, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 160 and y < 180) or (d == 'c' and dn == 5 and pos == 2)) and is_valid_move(data,"c",5,2)):
        board = make_a_move(data,"c",5,2)
        canvas.create_line(420, 170, 480, 170, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 240 and y < 260) or (d == 'c' and dn == 5 and pos == 3)) and is_valid_move(data,"c",5,3)):
        board = make_a_move(data,"c",5,3)
        canvas.create_line(420, 250, 480, 250, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 320 and y < 340) or (d == 'c' and dn == 5 and pos == 4)) and is_valid_move(data,"c",5,4)):
        board = make_a_move(data,"c",5,4)
        canvas.create_line(420, 330, 480, 330, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 400 and y < 420) or (d == 'c' and dn == 5 and pos == 5)) and is_valid_move(data,"c",5,5)):
        board = make_a_move(data,"c",5,5)
        canvas.create_line(420, 410, 480, 410, fill="red", width=10)
        
    elif(((x > 420 and x < 480 and y > 480 and y < 500) or (d == 'c' and dn == 5 and pos == 6)) and is_valid_move(data,"c",5,6)):
        board = make_a_move(data,"c",5,6)
        canvas.create_line(420, 490, 480, 490, fill="red", width=10)
    else:
        return False
    return True

def paint_box(boxes,painted,jugador):    
    for box in boxes:
        if(not painted[box]):
            if(box==0):                
                if(jugador):
                    canvas.create_rectangle(100, 100, 160, 160, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(100, 100, 160, 160, 
                outline="yellow", fill="yellow")
            if(box==1):
                if(jugador):
                    canvas.create_rectangle(180, 100, 240, 160, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(180, 100, 240, 160, 
                outline="yellow", fill="yellow")
            if(box==2):
                if(jugador):
                    canvas.create_rectangle(260, 100, 320, 160, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(260, 100, 320, 160, 
                outline="yellow", fill="yellow")
            if(box==3):
                if(jugador):
                    canvas.create_rectangle(340, 100, 400, 160, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(340, 100, 400, 160, 
                outline="yellow", fill="yellow")
            if(box==4):
                if(jugador):
                    canvas.create_rectangle(420, 100, 480, 160, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(420, 100, 480, 160, 
                outline="yellow", fill="yellow")
            if(box==5):
                if(jugador):
                    canvas.create_rectangle(100, 180, 160, 240,
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(100, 180, 160, 240,
                outline="yellow", fill="yellow")
            if(box==6):
                if(jugador):
                    canvas.create_rectangle(180, 180, 240, 240, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(180, 180, 240, 240, 
                outline="yellow", fill="yellow")
            if(box==7):
                if(jugador):
                    canvas.create_rectangle(260, 180, 320, 240, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(260, 180, 320, 240, 
                outline="yellow", fill="yellow")
            if(box==8):
                if(jugador):
                    canvas.create_rectangle(340, 180, 400, 240, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(340, 180, 400, 240, 
                outline="yellow", fill="yellow")
            if(box==9):
                if(jugador):
                    canvas.create_rectangle(420, 180, 480, 240,
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(420, 180, 480, 240, 
                outline="yellow", fill="yellow")
            if(box==10):
                if(jugador):
                    canvas.create_rectangle(100, 260, 160, 320,
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(100, 260, 160, 320, 
                outline="yellow", fill="yellow")
            if(box==11):
                if(jugador):
                    canvas.create_rectangle(180, 260, 240, 320, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(180, 260, 240, 320, 
                outline="yellow", fill="yellow")
            if(box==12):
                if(jugador):
                    canvas.create_rectangle(260, 260, 320, 320, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(260, 260, 320, 320, 
                outline="yellow", fill="yellow")
            if(box==13):
                if(jugador):
                    canvas.create_rectangle(340, 260, 400, 320, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(340, 260, 400, 320,
                outline="yellow", fill="yellow")
            if(box==14):
                if(jugador):
                    canvas.create_rectangle(420, 260, 480, 320, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(420, 260, 480, 320, 
                outline="yellow", fill="yellow")
            if(box==15):
                if(jugador):
                    canvas.create_rectangle(100, 340, 160, 400, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(100, 340, 160, 400, 
                outline="yellow", fill="yellow")
            if(box==16):
                if(jugador):
                    canvas.create_rectangle(180, 340, 240, 400, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(180, 340, 240, 400, 
                outline="yellow", fill="yellow")
            if(box==17):
                if(jugador):
                    canvas.create_rectangle(260, 340, 320, 400, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(260, 340, 320, 400, 
                outline="yellow", fill="yellow")
            if(box==18):
                if(jugador):
                    canvas.create_rectangle(340, 340, 400, 400, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(340, 340, 400, 400, 
                outline="yellow", fill="yellow")
            if(box==19):
                if(jugador):
                    canvas.create_rectangle(420, 340, 480, 400, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(420, 340, 480, 400, 
                outline="yellow", fill="yellow")
            if(box==20):
                if(jugador):
                    canvas.create_rectangle(100, 420, 160, 480, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(100, 420, 160, 480, 
                outline="yellow", fill="yellow")
            if(box==21):
                if(jugador):
                    canvas.create_rectangle(180, 420, 240, 480, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(180, 420, 240, 480, 
                outline="yellow", fill="yellow")
            if(box==22):
                if(jugador):
                    canvas.create_rectangle(260, 420, 320, 480, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(260, 420, 320, 480, 
                outline="yellow", fill="yellow")
            if(box==23):
                if(jugador):
                    canvas.create_rectangle(340, 420, 400, 480, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(340, 420, 400, 480, 
                outline="yellow", fill="yellow")
            if(box==24):
                if(jugador):
                    canvas.create_rectangle(420, 420, 480, 480, 
                outline="green", fill="green")
                else:
                    canvas.create_rectangle(420, 420, 480, 480, 
                outline="yellow", fill="yellow")
                    
def callback(event):
    global data
    global board
    global boxes
    global turno_jugador    
    jugada = True
    print ("clicked at", event.x, event.y)        
    if(turno_jugador):
        jugada = paint(event.x,event.y,"",0,0)
        if(boxes == heuristic.count_filled_boxes(board.gameboard) and jugada):
            turno_jugador = False
            play = (heuristic.first_approach(data, board.gameboard))
            paint(0,0,play[0],play[1],play[2])
            while(boxes != heuristic.count_filled_boxes(board.gameboard)):
                boxes = heuristic.count_filled_boxes(board.gameboard)
                paint_box(boxes,board.painted,False)
                play = (heuristic.first_approach(data, board.gameboard))
                paint(0,0,play[0],play[1],play[2])                
            turno_jugador = True
        else:
            boxes = heuristic.count_filled_boxes(board.gameboard)
            paint_box(boxes,board.painted,True)            

canvas.bind("<Button-1>", callback)



root.mainloop()
