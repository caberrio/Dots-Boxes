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
cuadros = len(heuristic.count_filled_boxes(board.gameboard))
turno_jugador = True

#LOGIC

canvas = Canvas(root)

for j in range(0,6):
            for i in range(0,6):
                canvas.create_oval(i*80+100, j*80+100, (i+1)*80, (j+1)*80, outline="blue",
                                fill="blue", width=2)


canvas.pack(fill=BOTH, expand=1)



def callback(event):
    global board
    global turno_jugador    
    jugada = True
    print ("clicked at", event.x, event.y)        
    if(turno_jugador):
        if(event.x > 80 and event.x < 100 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,1)):        
            board = make_a_move(data,"r",1,1)            
            canvas.create_line(90, 100, 90, 160, fill="red", width=10)        
            
        elif(event.x > 80 and event.x < 100 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,1)):
            board = make_a_move(data,"r",2,1)            
            canvas.create_line(90, 180, 90, 240, fill="red", width=10)        
            
        elif(event.x > 80 and event.x < 100 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,1)):
            board = make_a_move(data,"r",3,1)            
            canvas.create_line(90, 260, 90, 320, fill="red", width=10)
            
        elif(event.x > 80 and event.x < 100 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,1)):
            board = make_a_move(data,"r",4,1)            
            canvas.create_line(90, 340, 90, 400, fill="red", width=10)
            
        elif(event.x > 80 and event.x < 100 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,1)):
            board = make_a_move(data,"r",5,1)            
            canvas.create_line(90, 420, 90, 480, fill="red", width=10)
            
        elif(event.x > 160 and event.x < 180 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,2)):
            board = make_a_move(data,"r",1,2)            
            canvas.create_line(170, 100, 170, 160, fill="red", width=10)
            
        elif(event.x > 160 and event.x < 180 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,2)):
            board = make_a_move(data,"r",2,2)            
            canvas.create_line(170, 180, 170, 240, fill="red", width=10)
            
        elif(event.x > 160 and event.x < 180 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,2)):
            board = make_a_move(data,"r",3,2)            
            canvas.create_line(170, 260, 170, 320, fill="red", width=10)
            
        elif(event.x > 160 and event.x < 180 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,2)):
            board = make_a_move(data,"r",4,2)            
            canvas.create_line(170, 340, 170, 400, fill="red", width=10)
            
        elif(event.x > 160 and event.x < 180 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,2)):
            board = make_a_move(data,"r",5,2)        
            canvas.create_line(170, 420, 170, 480, fill="red", width=10)
        
        elif(event.x > 240 and event.x < 260 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,3)):
            board = make_a_move(data,"r",1,3)
            canvas.create_line(250, 100, 250, 160, fill="red", width=10)
            
        elif(event.x > 240 and event.x < 260 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,3)):
            board = make_a_move(data,"r",2,3)
            canvas.create_line(250, 180, 250, 240, fill="red", width=10)
            
        elif(event.x > 240 and event.x < 260 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,3)):
            board = make_a_move(data,"r",3,3)
            canvas.create_line(250, 260, 250, 320, fill="red", width=10)
        
        elif(event.x > 240 and event.x < 260 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,3)):
            board = make_a_move(data,"r",4,3)
            canvas.create_line(250, 340, 250, 400, fill="red", width=10)
            
        elif(event.x > 240 and event.x < 260 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,3)):
            board = make_a_move(data,"r",5,3)
            canvas.create_line(250, 420, 250, 480, fill="red", width=10)
            
        elif(event.x > 320 and event.x < 340 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,4)):
            board = make_a_move(data,"r",1,4)
            canvas.create_line(330, 100, 330, 160, fill="red", width=10)
            
        elif(event.x > 320 and event.x < 340 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,4)):
            board = make_a_move(data,"r",2,4)
            canvas.create_line(330, 180, 330, 240, fill="red", width=10)
            
        elif(event.x > 320 and event.x < 340 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,4)):
            board = make_a_move(data,"r",3,4)
            canvas.create_line(330, 260, 330, 320, fill="red", width=10)
            
        elif(event.x > 320 and event.x < 340 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,4)):
            board = make_a_move(data,"r",4,4)
            canvas.create_line(330, 340, 330, 400, fill="red", width=10)
        
        elif(event.x > 320 and event.x < 340 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,4)):
            board = make_a_move(data,"r",5,4)
            canvas.create_line(330, 420, 330, 480, fill="red", width=10)
            
        elif(event.x > 400 and event.x < 420 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,5)):
            board = make_a_move(data,"r",1,5)
            canvas.create_line(410, 100, 410, 160, fill="red", width=10)
            
        elif(event.x > 400 and event.x < 420 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,5)):
            board = make_a_move(data,"r",2,5)
            canvas.create_line(410, 180, 410, 240, fill="red", width=10)
            
        elif(event.x > 400 and event.x < 420 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,5)):
            board = make_a_move(data,"r",3,5)
            canvas.create_line(410, 260, 410, 320, fill="red", width=10)
            
        elif(event.x > 400 and event.x < 420 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,5)):
            board = make_a_move(data,"r",4,5)
            canvas.create_line(410, 340, 410, 400, fill="red", width=10)
            
        elif(event.x > 400 and event.x < 420 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,5)):
            board = make_a_move(data,"r",5,5)
            canvas.create_line(410, 420, 410, 480, fill="red", width=10)
            
        elif(event.x > 480 and event.x < 500 and event.y > 100 and event.y < 160 and is_valid_move(data,"r",1,6)):
            board = make_a_move(data,"r",1,6)
            canvas.create_line(490, 100, 490, 160, fill="red", width=10)
        
        elif(event.x > 480 and event.x < 500 and event.y > 180 and event.y < 240 and is_valid_move(data,"r",2,6)):
            board = make_a_move(data,"r",2,6)
            canvas.create_line(490, 180, 490, 240, fill="red", width=10)
        
        elif(event.x > 480 and event.x < 500 and event.y > 260 and event.y < 320 and is_valid_move(data,"r",3,6)):
            board = make_a_move(data,"r",3,6)
            canvas.create_line(490, 260, 490, 320, fill="red", width=10)
        
        elif(event.x > 480 and event.x < 500 and event.y > 340 and event.y < 400 and is_valid_move(data,"r",4,6)):
            board = make_a_move(data,"r",4,6)
            canvas.create_line(490, 340, 490, 400, fill="red", width=10)
            
        elif(event.x > 480 and event.x < 500 and event.y > 420 and event.y < 480 and is_valid_move(data,"r",5,6)):
            board = make_a_move(data,"r",5,6)
            canvas.create_line(490, 420, 490, 480, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 80 and event.y < 100 and is_valid_move(data,"c",1,1)):
            board = make_a_move(data,"c",1,1)
            canvas.create_line(100, 90, 160, 90, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 160 and event.y < 180 and is_valid_move(data,"c",1,2)):        
            board = make_a_move(data,"c",1,2)
            canvas.create_line(100, 170, 160, 170, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 240 and event.y < 260 and is_valid_move(data,"c",1,3)):
            board = make_a_move(data,"c",1,3)
            canvas.create_line(100, 250, 160, 250, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 320 and event.y < 340 and is_valid_move(data,"c",1,4)):
            board = make_a_move(data,"c",1,4)
            canvas.create_line(100, 330, 160, 330, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 400 and event.y < 420 and is_valid_move(data,"c",1,5)):
            board = make_a_move(data,"c",1,5)
            canvas.create_line(100, 410, 160, 410, fill="red", width=10)
            
        elif(event.x > 100 and event.x < 160 and event.y > 480 and event.y < 500 and is_valid_move(data,"c",1,6)):
            board = make_a_move(data,"c",1,6)
            canvas.create_line(100, 490, 160, 490, fill="red", width=10)
            
        elif(event.x > 180 and event.x < 240 and event.y > 80 and event.y < 100 and is_valid_move(data,"c",2,1)):
            board = make_a_move(data,"c",2,1)
            canvas.create_line(180, 90, 240, 90, fill="red", width=10)
            
        elif(event.x > 180 and event.x < 240 and event.y > 160 and event.y < 180 and is_valid_move(data,"c",2,2)):
            board = make_a_move(data,"c",2,2)
            canvas.create_line(180, 170, 240, 170, fill="red", width=10)
            
        elif(event.x > 180 and event.x < 240 and event.y > 240 and event.y < 260 and is_valid_move(data,"c",2,3)):
            board = make_a_move(data,"c",2,3)
            canvas.create_line(180, 250, 240, 250, fill="red", width=10)
    
        elif(event.x > 180 and event.x < 240 and event.y > 320 and event.y < 340 and is_valid_move(data,"c",2,4)):
            board = make_a_move(data,"c",2,4)
            canvas.create_line(180, 330, 240, 330, fill="red", width=10)
    
        elif(event.x > 180 and event.x < 240 and event.y > 400 and event.y < 420 and is_valid_move(data,"c",2,5)):
            board = make_a_move(data,"c",2,5)
            canvas.create_line(180, 410, 240, 410, fill="red", width=10)
            
        elif(event.x > 180 and event.x < 240 and event.y > 480 and event.y < 500 and is_valid_move(data,"c",2,6)):
            board = make_a_move(data,"c",2,6)
            canvas.create_line(180, 490, 240, 490, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 80 and event.y < 100 and is_valid_move(data,"c",3,1)):
            board = make_a_move(data,"c",3,1)
            canvas.create_line(260, 90, 320, 90, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 160 and event.y < 180 and is_valid_move(data,"c",3,2)):
            board = make_a_move(data,"c",3,2)
            canvas.create_line(260, 170, 320, 170, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 240 and event.y < 260 and is_valid_move(data,"c",3,3)):
            board = make_a_move(data,"c",3,3)
            canvas.create_line(260, 250, 320, 250, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 320 and event.y < 340 and is_valid_move(data,"c",3,4)):
            board = make_a_move(data,"c",3,4)
            canvas.create_line(260, 330, 320, 330, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 400 and event.y < 420 and is_valid_move(data,"c",3,5)):
            board = make_a_move(data,"c",3,5)
            canvas.create_line(260, 410, 320, 410, fill="red", width=10)
            
        elif(event.x > 260 and event.x < 320 and event.y > 480 and event.y < 500 and is_valid_move(data,"c",3,6)):
            board = make_a_move(data,"c",3,6)
            canvas.create_line(260, 490, 320, 490, fill="red", width=10)
            
        elif(event.x > 340 and event.x < 400 and event.y > 80 and event.y < 100 and is_valid_move(data,"c",4,1)):
            board = make_a_move(data,"c",4,1)
            canvas.create_line(340, 90, 400, 90, fill="red", width=10)
            
        elif(event.x > 340 and event.x < 400 and event.y > 160 and event.y < 180 and is_valid_move(data,"c",4,2)):
            board = make_a_move(data,"c",4,2)
            canvas.create_line(340, 170, 400, 170, fill="red", width=10)
            
        elif(event.x > 340 and event.x < 400 and event.y > 240 and event.y < 260 and is_valid_move(data,"c",4,3)):
            board = make_a_move(data,"c",4,3)
            canvas.create_line(340, 250, 400, 250, fill="red", width=10)
            
        elif(event.x > 340 and event.x < 400 and event.y > 320 and event.y < 340 and is_valid_move(data,"c",4,4)):
            board = make_a_move(data,"c",4,4)
            canvas.create_line(340, 330, 400, 330, fill="red", width=10)
        
        elif(event.x > 340 and event.x < 400 and event.y > 400 and event.y < 420 and is_valid_move(data,"c",4,5)):
            board = make_a_move(data,"c",4,5)
            canvas.create_line(340, 410, 400, 410, fill="red", width=10)
            
        elif(event.x > 340 and event.x < 400 and event.y > 480 and event.y < 500 and is_valid_move(data,"c",4,6)):
            board = make_a_move(data,"c",4,6)
            canvas.create_line(340, 490, 400, 490, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 80 and event.y < 100 and is_valid_move(data,"c",5,1)):
            board = make_a_move(data,"c",5,1)
            canvas.create_line(420, 90, 480, 90, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 160 and event.y < 180 and is_valid_move(data,"c",5,2)):
            board = make_a_move(data,"c",5,2)
            canvas.create_line(420, 170, 480, 170, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 240 and event.y < 260 and is_valid_move(data,"c",5,3)):
            board = make_a_move(data,"c",5,3)
            canvas.create_line(420, 250, 480, 250, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 320 and event.y < 340 and is_valid_move(data,"c",5,4)):
            board = make_a_move(data,"c",5,4)
            canvas.create_line(420, 330, 480, 330, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 400 and event.y < 420 and is_valid_move(data,"c",5,5)):
            board = make_a_move(data,"c",5,5)
            canvas.create_line(420, 410, 480, 410, fill="red", width=10)
            
        elif(event.x > 420 and event.x < 480 and event.y > 480 and event.y < 500 and is_valid_move(data,"c",5,6)):
            board = make_a_move(data,"c",5,6)
            canvas.create_line(420, 490, 480, 490, fill="red", width=10)
        else:
            jugada = False
        if(cuadros == len(heuristic.count_filled_boxes(board.gameboard)) and jugada):            
            turno_jugador = False


canvas.bind("<Button-1>", callback)



root.mainloop()
