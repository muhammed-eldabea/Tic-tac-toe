#===========================================================
#   Author  : Muhammed Eldabea HAshem 
#   Date    : 22 AUG 2020 
#   Version : V01 
# ===========================================================



#used to init the game board and player definition 
def Tick_init() : 
    #this function is used to init the board at which the game will run 
    Tick = [0,0,0,0,0,0,0,0,0] 
    #definition for the possible input that user can input 
    X=1 
    O=2
    return Tick,X,O 

#EOF

#this function will print the current state of the game 
def Tick_print(tick_board_r=[]) :
    
    tick_board=tick_board_r.copy() 
    #decoding the game board  
    for i in range(9) : 
        if(tick_board[i]==0) : 
            tick_board[i] = " "
        elif (tick_board[i] ==1) : 
            tick_board[i] = "X"   
        elif(tick_board[i]==2) : 
            tick_board[i] = "O"

    #print the decoding game board
    print("#####<0>#####<1>#######<2>#######") 
    print("##   {}  ##   {}  ##    {}  ##".format(tick_board[0],tick_board[1],tick_board[2])) 
    print("#####<3>#########<4>######<5>#####")
    print("##   {}  ##   {}  ##    {}   #####".format(tick_board[3],tick_board[4],tick_board[5])) 
    print("######<6>#######<7>#######<8>#####")
    print("##   {}  ##   {}  ##    {}   ##".format(tick_board[6],tick_board[7],tick_board[8])) 
    print("##################################") 
    print("") 
    print("")
#EOF


#this function will give the player all available positions 
def Tick_CheckForAvilableGames(tick_board=[]) : 
    Available_Games=[]
#check for all available position  
    for i in range(0,9) : 
        if(tick_board[i]!=X ) and (tick_board[i]!=O ) :
            Available_Games.append(i)

#print all avaliable position at which player can take action 
    print("available games are in position ")
    for i in Available_Games : 
        print("{} \t" .format(i) , end=" ") 
    print("") 
    print("") 

    
#EOF 


def Tick_CheckForaWinner(tick_board=[],Player=0) :
    
    Possible_winning_position=[[0,3,6] , [1,4,7] , [6,7,8] , [0,1,2] , [3,4,5] , [7,8,9] , [0,4,8] , [2,4,6] ]
    
    #get all of  the position of player 
    for lis_in in Possible_winning_position  : 
        if tick_board[ lis_in[0]] ==Player : 
            if tick_board[ lis_in[1]] ==Player : 
                if tick_board[ lis_in[2]] ==Player : 
                    if(Player==1) : 
                        print("Player (X) is Winning !!")
                    elif(Player==2) : 
                        print("Player (O) is Winning !!")
                    return  1 

#EOF 


def Tick_play(tick_board=[],Player_role=0,position=0) : 
    tick_board [position] = Player_role 
    return tick_board



#start main code 

tick,X,O = Tick_init() 

for i in range(1,11) : 
    
    #this part is for play X 
    if(i%2 == 0 ) : 
        
        #print the board
        Tick_print(tick) 
        #give the player all available postion 
        Tick_CheckForAvilableGames(tick) 
        #take the position from the player 
        postion_played=int(input("Enter the position FOR player X ")) 
        #take an action depending on the given postion
        tick=Tick_play(tick,X,postion_played)
        #print the board again 
        Tick_print(tick) 
        #check if the player won 
        if (Tick_CheckForaWinner(tick,X) ==1) : 
            break 
        
    
    else : 
        #print the board
        Tick_print(tick) 
        #give the player all available postion 
        Tick_CheckForAvilableGames(tick) 
        #take the position from the player 
        postion_played=int(input("Enter the position FOR player O ")) 
        #take an action depending on the given postion
        tick = Tick_play(tick,O,postion_played)
        #print the board again 
        Tick_print(tick)
        #check if the player won 
        if (Tick_CheckForaWinner(tick,O) ==1) :
            break  
    


           