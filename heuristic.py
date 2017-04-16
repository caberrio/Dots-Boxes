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

""
def alphaBeta(data, board, alpha, beta, deep,numbox):
        """ Implements a minimax algorithm with alpha-beta pruning. """
        if deep == 0:
            return heuristic_value1(board, data,numbox)
        
        datacopy=copy.deepcopy(data)
        boardcopy=copy.deepcopy(board)
        cf=count_filled_boxes(board)
        for i in range(1,6):
                for j in range(1,7):
                    if(dots.is_valid_move(datacopy,'r',i,j)):
                        board =dots.make_a_move(datacopy,'r',i,j)
                        if(cf<count_filled_boxes(board.gameboard)):
                            deep=deep+1
                        if(count_filled_boxes==25):
                            deep=1
                        current_eval = -alphaBeta(datacopy, board.gameboard, float('-infinity'), alpha, deep - 1,numbox)
                        datacopy=copy.deepcopy(data)

                        if current_eval >= beta:
                            return beta
            
                        if current_eval > alpha:
                            alpha = current_eval
                            
        for i in range(1,6):
            for j in range(1,7):
                if(dots.is_valid_move(datacopy,'c',i,j)):
                    board =dots.make_a_move(datacopy,'c',i,j)
                    current_eval = -alphaBeta(data, board.gameboard, float('-infinity'), alpha, deep - 1,numbox)
                    datacopy=copy.deepcopy(data)

                    if current_eval >= beta:
                        return beta
        
                    if current_eval > alpha:
                        alpha = current_eval

        return alpha

def rootAlphaBeta(board, data, deep):
    """ Makes a call to the alphaBeta function. Returns the optimal move for a player at given deep. """
    best_move = None
    max_eval = float('-infinity')
    datacopy=copy.deepcopy(data)
    boardcopy=copy.deepcopy(board)
    numbox=count_filled_boxes(board)
    alpha = float('infinity')
    for i in range(1,6):
        for j in range(1,7):
            if(dots.is_valid_move(datacopy,'r',i,j)):
                board =dots.make_a_move(datacopy,'r',i,j)
                alpha = alphaBeta(datacopy, board.gameboard, float('-infinity'), alpha, deep - 1,numbox)
                datacopy=copy.deepcopy(data)
    
                if alpha > max_eval:
                    max_eval = alpha
                    best_move = ['r',i,j]
    datacopy=copy.deepcopy(data)               
    for i in range(1,6):
        for j in range(1,7):
            if(dots.is_valid_move(datacopy,'c',i,j)):
                board =dots.make_a_move(datacopy,'c',i,j)
                alpha = alphaBeta(data, board.gameboard, float('-infinity'), alpha, deep - 1,numbox)
                datacopy=copy.deepcopy(data)
    
                if alpha > max_eval:
                    max_eval = alpha
                    best_move = ['c',i,j]
    return best_move
""
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
    i=0
    cont=0
    while 20:
        a=randint(1,5)
        b=randint(1,6)
        c=randint(0,1)
        if(len(num3)>0):
            datacopy=copy.deepcopy(datas)
            if(gameboard[num3[0]].index(False)<2):
                d='r'
                board=dots.make_a_move(datacopy,d,num3[0]//5+1,num3[0]%5+gameboard[num3[0]].index(False)+1)
                move=['r',num3[0]//5+1,num3[0]%5+gameboard[num3[0]].index(False)+1]
                break
            else:
                d='c'
                board=dots.make_a_move(datacopy,d,num3[0]%5+1,num3[0]//5+gameboard[num3[0]].index(False)-1)
                move=['c',num3[0]%5+1,num3[0]//5+gameboard[num3[0]].index(False)-1]
                break
            
        if(c==0):
            datacopy=copy.deepcopy(datas)
            if(dots.is_valid_move(datacopy,'r',a,b)):
                board =dots.make_a_move(datacopy,'r',a,b)
                if(len(numthree(board.gameboard))>len(num3) and cont<15):
                    cont=cont+1;
                    continue
                move=['r',a,b]
                break
        else:
            datacopy=copy.deepcopy(datas)
            if(dots.is_valid_move(datacopy,'c',a,b)):
                board =dots.make_a_move(datacopy,'c',a,b)
                if(len(numthree(board.gameboard))>len(num3) and cont<15):
                    cont=cont+1;
                    continue
                move=['c',a,b]
                break
                
    datacopy=copy.deepcopy(datas)    
    return move
    
def heuristic_value1(gameboard,datas,boxes):
    states=board_states(gameboard)
    k=5
    c=10
    if(boxes<count_filled_boxes(gameboard)):
        k=(abs(k)+10)*len(count_filled_boxes(gameboard))
    if(len(numthree(gameboard))>0):
        k=k-50
    h=[x*c for x in states]
    return (1/(sum(h)+0.1)*board_available(gameboard)+k)*randint(1,6)
    
import dots
import copy
from random import randint
