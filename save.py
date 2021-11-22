class Save:

    def __init__(self):
        self.filename = 'chess.txt'

    def save(self, board):
        try:
            with open(self.filename, mode='w') as f:
                f.write(str(board))

        except:
            print("Error writing to file.")

    def update(self, val, r, c):
        try:
            with open(self.filename, mode='r+') as f:
                pos = (r-1) * 8 + (c-1)
                f.seek(pos)
                f.write(val)
                print(self)
        except:
            print("Errors saving the file.")
