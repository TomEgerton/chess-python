class Save:

    def __init__(self):
        self.filename = 'chess.txt'


    #Saves the board
    def save(self, board):
        '''
        Saves an initial state of the gameboard
        :param board:
        :return:
        '''
        try:
            with open(self.filename, mode='w') as f:
                f.write(str(board))

        except:
            print("Error writing to file.")

    def update(self, val, r, c):
        '''

        :param val: The value that will be inserted
        :param r: The row reference
        :param c: The column reference
        :return:
        '''
        try:
            with open(self.filename, mode='r+') as f:
                pos = (r-1) * 8 + (c-1)
                f.seek(pos)
                f.write(val)
        except:
            print("Errors saving the file.")
