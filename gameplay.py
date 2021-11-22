from createBoard import Board
from save import Save

s = Save()

class Gameplay:

    def __init__(self):
        self.b = Board()
        s.save(str(self.b))

        print("======= TOM'S CHESS GAME WOW ======="
              "\n-Type desired location via grid coordinates eg - a5"
              "\n-This is a prototype and assumes all players will follow the rules, no pieces have logic so don't cheat lol"
              "\n-Castling is called with the command o-o or king side, or o-o-o for queen side.")
        self.b.printBoard()
        self.movecount = 0
        self.Ofirstval = 0
        self.Dfirstval = 0
        self.Dsecondval = 0
        self.Osecondval = 0
        self.location = 1
        self.king = 'K'
        self.castle = 'C'
        self.moveDic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.origin = ''
        self.destination = ''

        self.white = True
        print("===== Whites turn =====")
        self.move()

    def moveCount(self):
        self.movecount = self.movecount + 1
        if (self.movecount % 2) == 0:
            self.white = True
            self.location = 1
            self.king = 'K'
            self.castle = 'C'
            print("===== Whites turn =====")

        else:
            self.white = False
            self.location = 8
            self.king = 'k'
            self.castle = 'c'
            print("===== Blacks turn =====")

    def move(self):
        """
        Moves a piece on the board
        """
        # A dictionary to convert the letter values to numbers for the board coordinates

        self.origin = input("Which piece to move: ").lower()

        # Checks to see if the move entered is longer or less than 2 characters

        if self.castling() is True:
            self.b.printBoard()
            print("Castling complete")
            self.moveCount()
            return

        elif len(self.origin) > 2 or len(self.origin) < 2:
            print("Enter a valid move")
            self.move()

        else:
            # Checks the move to see if the user has entered a valid location
            if self.origin[0] not in self.moveDic or int(self.origin[1]) > 8 or int(self.origin[1]) < 1:
                print("Enter a valid location")
                self.move()

            else:

                # Splits the origin into the first and second variable
                self.Ofirstval = self.moveDic[self.origin[0]]
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
                        return
                    else:

                        if self.destination[0] not in self.moveDic or int(self.destination[1]) > 8:
                            print("Enter a valid location")
                            self.move()
                            return

                        else:
                            # Splits the second value and checks the move.
                            self.Dfirstval = self.moveDic[self.destination[0]]
                            self.Dsecondval = self.destination[1]
                            if self.checkSecondVal():

                                self.b.printBoard()
                                self.moveCount()

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

        elif not self.white:
            if self.b.board[int(self.Osecondval)][int(self.Ofirstval)] == '.' or \
                    self.b.board[int(self.Osecondval)][int(self.Ofirstval)].isupper():
                print("Select a valid piece")
                self.move()
            else:
                pass

    def checkSecondVal(self):
        """
        Checks the move to ensure the player is not targeting their own pieces
        :return:
        """
        if self.winstate():
            if self.white:
                print("White Wins")
                quit()
            else:
                print("Black Wins")
                quit()
        if self.white:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)].isupper():
                print("Select a valid position")
                self.move()
            else:

                s.update(self.b.board[int(self.Osecondval)][int(self.Ofirstval)], int(self.Dsecondval), int(self.Dfirstval))
                s.update('.', int(self.Osecondval), int(self.Ofirstval))
                self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                    int(self.Ofirstval)]

                self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                return True

        else:
            if self.b.board[int(self.Dsecondval)][int(self.Dfirstval)].islower():
                print("Select a valid position")
                self.move()
            else:
                s.update(self.b.board[int(self.Osecondval)][int(self.Ofirstval)], int(self.Dsecondval), int(self.Dfirstval))
                s.update('.', int(self.Osecondval), int(self.Ofirstval))
                self.b.board[int(self.Dsecondval)][int(self.Dfirstval)] = self.b.board[int(self.Osecondval)][
                    int(self.Ofirstval)]
                self.b.board[int(self.Osecondval)][int(self.Ofirstval)] = '.'
                return True

    def castling(self):

        if self.origin == 'o-o':
            if self.b.board[self.location][4] == self.king:
                if self.b.board[self.location][2] != '.' or self.b.board[self.location][3] != '.':
                    print("Invalid move")
                    self.move()
                    return False
                elif self.b.board[self.location][1] == self.castle:

                    s.update('.', self.location, 4)
                    s.update('.', self.location, 1)
                    s.update(self.king, self.location, 2)
                    s.update(self.castle, self.location, 3)



                    self.b.board[self.location][4] = '.'
                    self.b.board[self.location][1] = '.'
                    self.b.board[self.location][2] = self.king
                    self.b.board[self.location][3] = self.castle

                    return True
                else:
                    print("Invalid move")
                    self.move()
                    return

        # Queen side
        elif self.origin == 'o-o-o':
            if self.b.board[self.location][4] == self.king:
                for i in range(3):
                    if self.b.board[self.location][5] != '.' or self.b.board[self.location][6] != '.' or \
                            self.b.board[self.location][7] != '.':
                        print("Invalid move")

                        return False
                    elif self.b.board[self.location][8] == self.castle:

                        s.update('.', self.location, 8)
                        s.update('.', self.location, 4)
                        s.update(self.king, self.location, 6)
                        s.update(self.castle, self.location, 7)

                        self.b.board[self.location][8] = '.'
                        self.b.board[self.location][4] = '.'
                        self.b.board[self.location][6] = self.king
                        self.b.board[self.location][7] = self.castle
                        return True
                    else:
                        print("Invalid move")
                        return False

        else:
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
