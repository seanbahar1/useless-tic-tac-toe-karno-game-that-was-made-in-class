#-- this game is a weird tic tac toe hybrid with karno map
#-- this trash code is copyrighted by me sean...... useless class time hahahaha....
import os
clear = lambda: os.system('cls')
class gameBoard:
    def __init__(self):
        self.__board = (["█","█","█","█"],
                        ["█","█","█","█"],
                        ["█","█","█","█"],
                        ["█","█","█","█"])
        self.turn = True
        self.gameOn = True
        self.loc = {
            0 :  (0,0),
            1 :  (0,1),
            2 :  (0,3),
            3 :  (0,2),
            4 :  (1,0),
            5 :  (1,1),
            6 :  (1,3),
            7 :  (1,2),
            8 :  (3,0),
            9 :  (3,1),
            10 : (3,3),
            11 : (3,2), 
            12 : (2,0),
            13 : (2,1),
            14 : (2,3),
            15 : (2,2)
            }
    def place(self, loc):
        locx,locy = self.loc[loc]
        if(self.__board[locy][locx] == 1 or self.__board[locy][locx] == 0):
            print('place is already taken\n please choose again')
            self.get_inp()
        else:
            if self.turn:
                self.__board[locy][locx] = 1
                w = self.checkWin()
                if(w):
                    print('player 1 won')
                    self.gameOn = False
                self.turn = False
            else:
                self.__board[locy][locx] = 0
                w = self.checkWin()
                if(w):
                    print('player 2 won')
                    self.gameOn = False
                self.turn = True
       
    def printboard(self):
        for y in range(0,4):
            printLn = ''
            for x in range(0,4):
                if(self.__board[y][x] != -1):
                    printLn += str(self.__board[y][x]) + "   "
                else:
                     printLn += str(self.__board[y][x]) + "   "  
            print(printLn)    
            print("\n")
    
    def get_inp(self):
        currentTurn = self.turn
        player = '1' if currentTurn else '2'
        print(' << player:{}: please enter a placing location 0-15\n'.format(player))
        inp = int(input())
        while(inp > 15 or inp < 0):
            print(' >> {ERROR} invalid, please enter between 0-15\n')
            inp = int(input())
        self.place(inp)

    def checkWin(self):
        win = False
        checks = 1 if self.turn else 0
        #check win in ----
        for y in range(0,4):
               if self.__board[y][0] == self.__board[y][1] == self.__board[y][2] == self.__board[y][3] == checks:
                    win = True
                    print('line')
                    return win
  
        #cheks | win
        for y in range(0,4):
               if self.__board[0][y] == self.__board[1][y] == self.__board[2][y] == self.__board[3][y] == checks:
                    win = True
                    print('|')
                    return win

        #checks group of 4 in an x
        for a in range(0,3):
            for b in range(0,3):
                if(self.__board[a][b] == self.__board[a+1][b]  == self.__board[a][b+1] == self.__board[a+1][b+1] == checks):
                    win = True
                    print('4x')
                    return win
        
        #checks for corners
        if(self.__board[0][0] == self.__board[3][3] == self.__board[0][3] == self.__board[3][0] == checks ):
            win = True
            print('corners 1')
            return win
        #checks x corners
        for x in range(0,3):
            if(self.__board[0][x] == self.__board[3][x] == self.__board[0][x+1] == self.__board[3][x+1] == checks):
                win = True
                print('corners 2')
                return win

        #checks x corners
        for x in range(0,3):
            if(self.__board[x][0] == self.__board[x][3] == self.__board[x+1][0] == self.__board[x+1][3] == checks):
                win = True
                print('c3')
                return win

        tie = True
        for y in range(0,4):
            for x in range(0,4):
                if self.__board[y][x] == "█":
                    tie = False
                
        if tie:

            self.gameOn = False
            print("the game is a tie")
            return False

        return False

game = gameBoard()
print('please enter a num between 0-15, you must know how to work with karno map to play  this game cause it works with the rules of karno\n gl learning how to play')
while(game.gameOn):
    #-- game is running
    game.printboard()
    game.get_inp()
    #clear()
        
game.printboard()
