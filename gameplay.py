from createBoard import Board


# CHECK KING HAS BEEN MURDERED TO WIN GAME

class Gameplay:

    def __init__(self):
        self.b = Board()
        self.b.printBoard()
        self.movecount = 0
        self.Ofirstval = 0
        self.Dfirstval = 0
        self.Dsecondval = 0
        self.Osecondval = 0
        self.origin = ''
        self.destination = ''

        self.white = True
        print("===== Whites turn =====")
        self.move()

    def moveCount(self):
        self.movecount = +1
        if (self.movecount % 2) == 0:
            self.white = True
            print("===== Whites turn =====")

        else:
            self.white = False
            print("===== Blacks turn =====")

    def move(self):
        """
        Moves a piece on the board
        """
        # A dictionary to convert the letter values to numbers for the board coordinates
        moveDic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

        self.origin = input("Which piece to move: ").lower()

        # Checks to see if the move entered is longer or less than 2 characters

        if self.origin == 'o-o' or self.origin == 'o-o-o':

            self.castling()

        elif len(self.origin) > 2 or len(self.origin) < 2:
            print("Enter a valid move")
            self.move()

        else:
            # Checks the move to see if the user has entered a valid location
            if self.origin[0] not in moveDic or int(self.origin[1]) > 8 or int(self.origin[1]) < 1:
                print("Enter a valid location")
                self.move()

            else:

                # Splits the origin into the first and second variable
                self.Ofirstval = moveDic[self.origin[0]]
                self.Osecondval = self.origin[1]

                # Checks the move
                if self.checkFirstVal():
                    return

                else:
                    # Prompts the user to input the desired location and repeats the same checks for the move
                    self.destination = input("Where to move to: ").lower()

                    if len(self.destination) > 2 or len(self.destination) < 2:
                        print("Enter a valid move")
                        self.move()
                    else:

                        if self.destination[0] not in moveDic or int(self.destination[1]) > 8:
                            print("Enter a valid location")
                            self.move()

                        else:
                            # Splits the second value and checks the move.
                            self.Dfirstval = moveDic[self.destination[0]]
                            self.Dsecondval = self.destination[1]
                            self.checkSecondVal()

    def checkFirstVal(self):
        """
        Checks the initial prompt to ensure the user has selected their own piece
        """
        if self.white:
            if self.b.board[int(self.Osecondval)][int(self.Ofirstval)] == '.' or \
                    self.b.board[int(self.Osecondval)][int(self.Ofirstval)].islower():
                print("Select a valid piece")
                self.move()

            else:
                pass

        else:
            if self.b.board[int(self.Osecondval)][int(self.Ofirstval)] == '.' or \
                    self.b.board[int(self.Osecondval)][int(self.Ofirstval)].isupper():
                print("Select a valid piece")
                self.move()
                return
            else:
                pass

    def checkSecondVal(self):
        """
        Checks the move to ensure the player is not targeting their own pieces
        :return:
        """

        if self.white:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)].isupper():
                print("Select a valid position")
                self.move()
                return
            else:
                if self.winstate():
                    if self.white:
                        print("White Wins")
                    else:
                        print("Black Wins")
                else:
                    self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                        int(self.Ofirstval)]
                    self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                    self.b.printBoard()
                    self.moveCount()

        else:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)].islower():
                print("Select a valid position")
                self.move()
                return
            else:

                if self.winstate():
                    return
                else:
                    self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                        int(self.Ofirstval)]
                    self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                    self.b.printBoard()
                    self.moveCount()

    def castling(self):

        if self.white:
            # king side
            if self.origin == 'o-o':
                if self.b.board[1][4] == 'K':
                    for i in range(2):
                        if self.b.board[1][i + 2] != '.':
                            print("Invalid move")
                            self.move()
                            return
                        elif self.b.board[1][1] == 'C':
                            self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = '.'
                            self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                            self.b.board[1][2] = 'K'
                            self.b.board[1][3] = 'C'
                            self.moveCount()
                        else:
                            print("Invalid move")
                            self.move()
                            return

            if self.origin == 'o-o-o':
                if self.b.board[1][4] == 'K':
                    for i in range(3):
                        if self.b.board[1][8 - 3] != '.':
                            print("Invalid move")
                            self.move()
                            return
                        elif self.b.board[1][8] == 'C':
                            self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = '.'
                            self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                            self.b.board[1][7] = 'K'
                            self.b.board[1][6] = 'C'
                        else:
                            print("Invalid move")
                            self.move()
                            return

            else:
                return

        elif self.white == False:
            if self.origin == 'o-o':
                if self.b.board[8][4] == 'k':
                    for i in range(2):
                        if self.b.board[8][i + 2] != '.':
                            print("Invalid move")
                            self.move()
                            return
                        elif self.b.board[8][1] == 'c':
                            self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = '.'
                            self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                            self.b.board[8][2] = 'k'
                            self.b.board[8][3] = 'c'
                            self.moveCount()
                        else:
                            print("Invalid move")
                            self.move()
                            return

            if self.origin == 'o-o-o':
                if self.b.board[8][4] == 'k':
                    for i in range(3):
                        if self.b.board[8][8 - 3] != '.':
                            print("Invalid move")
                            self.move()
                            return

                        elif self.b.board[8][8] == 'c':
                            self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = '.'
                            self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                            self.b.board[8][7] = 'k'
                            self.b.board[8][6] = 'c'
                        else:
                            print("Invalid move")
                            self.move()
                            return

    def winstate(self):
        if self.white:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] == 'k':
                self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                    int(self.Ofirstval)]
                self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                self.b.printBoard()
                return True
            else:
                return False
        else:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] == 'K':
                self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                    int(self.Ofirstval)]
                self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                self.b.printBoard()
                return True
            else:
                return False
