from player import Humanplayer, RandomComputerPlayer, SmartComputerPlayer
import math
import time

class TicTacToe:
    def __int__(self):
        self.board = [' ' for _ in range(9)] #3*3 board
        self.current_winner = None  #Keep track of winner

    def print_board(self):
        #Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')
    @staticmethod
    def print_board_nums():
        #what number correspond to the box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    

    
    def make_move(self, square, letter):
        #if valid.. then make the move (assign square to letter)
        #Then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        #winner if 3 in a row anywhere.. we have to check all of these!
        #first for the row
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind +1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_ind = square % 3
        column = [self.board[col_ind +i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #the only move to win diagonal possibly is (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all of these fail
        return False
    def empty_square(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')
    def available_moves(self):
        return [i for i , x in enumerate(self.board) if x == ' ']

def play(game, x_player, o_player, print_game = True): # the winner of the game or none for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #Starting letter, the winner will break the loop at the end
    while game.empty_squares():
        #get move from the player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just an empty line
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
                    
            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' #switches player
            #if letter == 'X':
            #    letter = 'O'
            #else:
             #   letter = 'X'
             

        
        if print_game:
            print("It's a tie")
if __name__ == '__main__':

    x_player = SmartComputerPlayer('X')
    o_player = Humanplayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game= True)




