

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
def alphaBeta(self, board, alpha, beta, deep):
        """ Implements a minimax algorithm with alpha-beta pruning. """
        if deep == 0:
            return self.positionEvaluation(board, player)

        move_list = board.generateMoves(rules, player)
        for move in move_list:
            board.makeMove(move, player)
            current_eval = -self.alphaBeta(board, rules, -beta, -alpha, deep - 1)
            board.unmakeMove(move, player)

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

    alpha = float('infinity')
    for i in range(1,6):
        for j in range(1,7):
            if(dots.is_valid_move(datacopy,'r',i,j)):
                board =dots.make_a_move(datacopy,'r',i,j)
                alpha = -alphaBeta(board, rules, float('-infinity'), alpha, deep - 1, board.getOtherPlayer(player))
                board.unmakeMove(move, player)
    
                if alpha > max_eval:
                    max_eval = alpha
                    best_move = move

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
            print("ohshit")
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
    
def heuristic_value1(gameboard,datas):
    states=board_states(gameboard)
    k=0
    if(len(count_filled_boxes(gameboard))>0):
        k=100
    c=10
    h=[x*c for x in states]
    return (1/(sum(h)/board_available(gameboard))+k)
    
import dots
import copy
from random import randint
