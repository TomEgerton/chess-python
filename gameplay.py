from createBoard import Board


class Gameplay:

    def __init__(self):
        self.b = Board()
        self.b.printBoard()
        self.movecount = 0
        self.Ofirstval = 0
        self.Dfirstval = 0
        self.Dsecondval = 0
        self.Osecondval = 0

        self.white = True
        print("Whites turn")
        self.move()


    def moveCount(self):
        self.movecount = +1
        if (self.movecount % 2) == 0:
            self.white = True
            print("Whites turn")


        else:
            self.white = False
            print("Blacks turn")


    def move(self):
        """
        Moves a piece on the board
        """
        # A dictionary to convert the letter values to numbers for the board coordinates
        moveDic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        origin = input("Which piece to move: ").lower()

        # Checks to see if the move entered is longer or less than 2 characters
        if len(origin) > 2 or len(origin) < 2:
            print("Enter a valid move")
            self.move()
        else:

            # Checks the move to see if the user has entered a valid location
            if origin[0] not in moveDic or int(origin[1]) > 8 or int(origin[1]) < 1:
                print("Enter a valid location")
                self.move()

            else:

                # Splits the origin into the first and second variable
                self.Ofirstval = moveDic[origin[0]]
                self.Osecondval = origin[1]

                # Checks the move
                if self.checkFirstVal():
                    return

                else:
                    # Prompts the user to input the desired location and repeats the same checks for the move
                    destination = input("Where to move to: ").lower()

                    if len(destination) > 2 or len(destination) < 2:
                        print("Enter a valid move")
                        self.move()
                    else:

                        if destination[0] not in moveDic or int(destination[1]) > 8:
                            print("Enter a valid location")
                            self.move()

                        else:
                            # Splits the second value and checks the move.
                            self.Dfirstval = moveDic[destination[0]]
                            self.Dsecondval = destination[1]
                            self.checkSecondVal()





    def checkFirstVal(self):
        """
        Checks the initial prompt to ensure the user has selected their own piece
        """
        if self.white:
            if self.b.board[int(self.Osecondval)][int(self.Ofirstval)] == '.' or\
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
                self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                    int(self.Ofirstval)]
                self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                self.b.printBoard()
                self.moveCount()

    def castling(self):
        pass
