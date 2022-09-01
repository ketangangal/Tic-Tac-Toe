import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10

    def display_board(self):
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    @staticmethod
    def player_input():
        marker = ''

        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'

    def place_marker(self, marker, position):
        self.board[position] = marker

    def win_check(self, mark):
        if self.board[7] == mark and self.board[8] == mark and self.board[9] == mark:
            # Horizontal Top
            return True

        elif self.board[4] == mark and self.board[5] == mark and self.board[6] == mark:
            # Horizontal Middle
            return True

        elif self.board[1] == mark and self.board[2] == mark and self.board[3] == mark:
            # Horizontal Bottom
            return True

        elif self.board[7] == mark and self.board[4] == mark and self.board[1] == mark:
            # Vertical Left
            return True

        elif self.board[8] == mark and self.board[5] == mark and self.board[2] == mark:
            # Vertical Middle
            return True

        elif self.board[9] == mark and self.board[6] == mark and self.board[3] == mark:
            # Vertical Right
            return True

        elif self.board[7] == mark and self.board[5] == mark and self.board[3] == mark:
            # Vertical Diagonal
            return True
        elif self.board[9] == mark and self.board[5] == mark and self.board[1] == mark:
            # Vertical Diagonal
            return True
        else:
            return False

    @staticmethod
    def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    def space_check(self, position):
        return self.board[position] == ' '

    def full_board_check(self):
        for i in range(1, 10):
            if self.space_check(i):
                return

    def player_choice(self):
        position = 0

        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(position):
            position = int(input('Choose your next position: (1-9) '))
            if position == -1:
                break

        return position

    @staticmethod
    def replay():
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')