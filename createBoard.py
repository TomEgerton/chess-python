class Board:

    def __init__(self):
        self.board = self.createB()


    def printBoard(self):
        string = ''
        for i in (range(8)):  # It is reversed so that white is at the bottom
            string += str(self.board[i]) + '\n'
        print(string)

    def createB(self):
        board = [list(['.'] * 8) for _ in range(8)]

        ## Creates the black side
        board[0][0] = 'C'
        board[0][7] = 'C'
        board[0][1] = 'KN'
        board[0][6] = 'KN'
        board[0][2] = 'B'
        board[0][5] = 'B'
        board[0][3] = 'K'
        board[0][4] = 'Q'

        ## Creates the white side
        board[7][0] = 'c'
        board[7][7] = 'c'
        board[7][1] = 'kn'
        board[7][6] = 'kn'
        board[7][2] = 'b'
        board[7][5] = 'b'
        board[7][3] = 'k'
        board[7][4] = 'q'

        ##sets the pawns
        print ('|  1   |  2  |  3  |  4  |  5  |  6  |  7  |  8  |')
        for i in range(8):
            board[1][i] = 'P'
            board[6][i] = 'p'

        return board
