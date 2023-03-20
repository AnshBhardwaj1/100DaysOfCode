from click import clear

def print_board (board_of_fn):
    print (f"{board_of_fn[0]}|{board_of_fn[1]}|{board_of_fn[2]}")
    print("------")
    print (f"{board_of_fn[3]}|{board_of_fn[4]}|{board_of_fn[5]}")
    print("------")
    print (f"{board_of_fn[6]}|{board_of_fn[7]}|{board_of_fn[8]}")


board_fin=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
board_cord=[j for j in range(1,10)]
board=board_cord.copy()
inp=[]
turn=1
where=10

while True:
    for i in [0,3,6]:#horizontal check
        if board[i]==board[i+1]==board[i+2]!=' ':
            print_board(board_fin)
            print (f"{board[i]} is the winner")   
            exit()
    for i in [0,1,2]:#vertical check
        if board[i]==board[i+3]==board[i+6] and board[i]!=' ':
            print_board(board_fin)
            print (f"{board[i]} is the winner")
            exit()
    if board[0]==board[4]==board[8]!=" " or board[2]==board[4]==board[6]!=" ":#diagonal check
        print_board(board_fin)
        print (f"{board[4]} is the winner")
        exit()
    elif len(inp)==9:
        print_board(board_fin)
        print ("Its a DRAW")
        exit()
#    print_board(board_cord)
    print_board(board)    
    while True:
        if turn==1:
            XO='X'
        else :
            XO='0'
        where=int(input(f"Where do you want {XO} to be : "))
        if where in inp :
            print(f"You already have {board[(where-1)]} at {where}")
        elif where >9:
            print("please write a position from 1 to 9")    
        else:
            if turn==1:
                inp.append(where)
                board[(where-1)]='X'
                board_fin[(where-1)]='X'
                turn=0
                clear()
                break
            else:
                inp.append(where)
                board[(where-1)]='0'
                board_fin[(where-1)]='0'
                turn=1
                clear()    
                break