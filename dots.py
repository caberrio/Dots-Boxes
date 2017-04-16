
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

#data = RC()
#board = create_board(data)
#print (board.gameboard)
#board=make_a_move(data,'r',1,3)    
#print (board.gameboard)
#board=make_a_move(data,'r',2,3)    
#print (board.gameboard)
