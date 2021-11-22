class Board:

    def __init__(self):
        self.board = self.createB()

    def __str__(self):
        '''
        Prints the board in a single string for saving
        :return: The string value for saving
        '''
        value = ""
        for row in self.board[1:9]:
            for pos in row[1:9]:
                value += pos

        return value

    def printBoard(self):
        '''
        Prints out the board in the correct chess layout
        :return:
        '''
        string = ''
        for i in (range(10).__reversed__()):
            string += str(self.board[i]) + '\n'

        print(string.replace(',', '').replace("'", ""))

    def createB(self):
        '''
        Creates the initial board
        :return: The board
        '''
        board = [list(['.'] * 10) for _ in range(10)]

        # Creates the board layout
        board[0][0] = 'WH |'
        board[9][9] = '| BL'
        board[0][9] = '| WH'
        board[9][0] = 'BL |'
        board[0][1] = 'A'
        board[0][2] = 'B'
        board[0][3] = 'C'
        board[0][4] = 'D'
        board[0][5] = 'E'
        board[0][6] = 'F'
        board[0][7] = 'G'
        board[0][8] = 'H'
        board[1][0] = ' 1 |'
        board[2][0] = ' 2 |'
        board[3][0] = ' 3 |'
        board[4][0] = ' 4 |'
        board[5][0] = ' 5 |'
        board[6][0] = ' 6 |'
        board[7][0] = ' 7 |'
        board[8][0] = ' 8 |'
        board[9][1] = 'A'
        board[9][2] = 'B'
        board[9][3] = 'C'
        board[9][4] = 'D'
        board[9][5] = 'E'
        board[9][6] = 'F'
        board[9][7] = 'G'
        board[9][8] = 'H'
        board[1][9] = '| 1 '
        board[2][9] = '| 2 '
        board[3][9] = '| 3 '
        board[4][9] = '| 4 '
        board[5][9] = '| 5 '
        board[6][9] = '| 6 '
        board[7][9] = '| 7 '
        board[8][9] = '| 8 '

        # Creates the black side
        board[1][1] = 'C'
        board[1][8] = 'C'
        board[1][2] = 'N'
        board[1][7] = 'N'
        board[1][3] = 'B'
        board[1][6] = 'B'
        board[1][4] = 'K'
        board[1][5] = 'Q'

        # Creates the white side
        board[8][1] = 'c'
        board[8][8] = 'c'
        board[8][2] = 'n'
        board[8][7] = 'n'
        board[8][3] = 'b'
        board[8][6] = 'b'
        board[8][4] = 'k'
        board[8][5] = 'q'

        # Sets the pawns
        for i in range(8):
            board[2][i + 1] = 'P'
            board[7][i + 1] = 'p'

        return board
