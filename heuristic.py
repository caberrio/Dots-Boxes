
def available_moves(datas):
    columns=[datas.column1,datas.column2,datas.column3,datas.column4,datas.column5]
    available_cols = [abs(6-sum(b)) for b in columns]
    rows=[datas.row1,datas.row2,datas.row3,datas.row4,datas.row5]
    available_rows = [abs(6-sum(b)) for b in rows]
    return(sum(available_cols)+sum(available_rows))
    

def board_available(gameboard):
    states=sum([abs(4-sum(x)) for x in gameboard])
    return states
    
    
def count_filled_boxes(gameboard):
    states=[sum(x) for x in gameboard]
    filleds=[i for i,v in enumerate(states) if v == 4]
    return (filleds)
    
def board_states(gameboard):
    states=[sum(x) for x in gameboard]
    almost =filter(lambda x : x <=3 and x>=1 , states)
    return list(almost)
    
def numthree(gameboard):
    states=[sum(x) for x in gameboard]
    almost =[i for i,v in enumerate(states) if v == 3]
    return almost 

""" def alpha_beta_prunning1(datas,gameboard):
    datacopy=copy.deepcopy(datas)
    boardcopy=copy.deepcopy(gameboard)
    heuristic_values=[]
    moves=[]
    for i in range(1,6):
        for j in range(1,7):
            if(dots.is_valid_move(datacopy,'r',i,j)):
                board =dots.make_a_move(datacopy,'r',i,j)
                heuristic_values.append(heuristic_value1(board.gameboard,datacopy))
                moves.append(['r',i,j])
            datacopy=copy.deepcopy(datas)
    for i in range(1,6):
        for j in range(1,7):
            if(dots.is_valid_move(datacopy,'c',i,j)):
                board =dots.make_a_move(datacopy,'c',i,j)
                heuristic_values.append(heuristic_value1(board.gameboard,datacopy))
                moves.append(['c',i,j])
            datacopy=copy.deepcopy(datas)
            
    return heuristic_values"""
            
def first_approach(datas,gameboard):
    boardcopy=copy.deepcopy(gameboard)
    num3=numthree(gameboard)
    while True:
        a=randint(1,5)
        b=randint(1,6)
        c=randint(0,1)
        if(c==0):
            datacopy=copy.deepcopy(datas)
            if(dots.is_valid_move(datacopy,'r',a,b)):
                board =dots.make_a_move(datacopy,'r',a,b)
                if(numthree(board.gameboard)>num3):
                    continue
                move=['r',a,b]
                break
        else:
            datacopy=copy.deepcopy(datas)
            if(dots.is_valid_move(datacopy,'c',a,b)):
                board =dots.make_a_move(datacopy,'c',a,b)
                if(numthree(board.gameboard)>num3):
                    continue
                move=['c',a,b]
                break
                
    datacopy=copy.deepcopy(datas)    
    return move
    
def heuristic_value1(gameboard,datas):
    states=board_states(gameboard)
    k=0
    if(len(count_filled_boxes(gameboard))>0):
        k=100
    c=available_moves(datas)
    h=[x*c for x in states]
    return sum(h)/board_available(gameboard)+k
    
import dots
import copy
from random import randint

"""rcs=dots.RC();
board = dots.create_board(rcs)          
board =dots.make_a_move(rcs,'r',1,3)
board =dots.make_a_move(rcs,'r',1,2)
board =dots.make_a_move(rcs,'c',1,1)
board =dots.make_a_move(rcs,'c',1,2)
print(board_available(board.gameboard))
print(first_approach(rcs,board.gameboard))"""
