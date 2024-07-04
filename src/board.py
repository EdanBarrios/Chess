from square import Square  # Importing Square class from square.py
from piece import *  # Importing all pieces (Pawn, Knight, Bishop, Rook, Queen, King)
from const import *  # Importing constants (ROWS, COLS)
from move import Move


class Board:

    def __init__(self):
        self.squares = [
            [0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)
        ]  # Initializing the squares attribute
        self._create()  # Creating the board
        self._add_pieces("white")  # Adding white pieces
        self._add_pieces("black")  # Adding black pieces

    def calc_moves(self, piece, row, col):
        """
        Calculate and describr all possible (valid) moves of a specific piece from its respective position
        """

        def knight_moves():
            # Maximum of eight possible moves
            possible_moves = [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row + 2, col - 1),
                (row + 2, col + 1),
                (row - 1, col + 2),
                (row - 1, col - 2),
                (row + 1, col + 2),
                (row + 1, col - 2),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][
                        possible_move_col
                    ].isempty_or_rival(piece.color):
                        # Create squares of new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create new move
                        move = Move(initial, final)
                        # Append new valid move
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass

    def _create(self):
        """
        Create the board with squares initialized to Square objects.
        """
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        """
        Add pieces of the specified color to their starting positions.
        """
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        # Create all pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_pawn, 1, Knight(color))
        self.squares[row_other][6] = Square(row_pawn, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_pawn, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_pawn, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_pawn, 0, Rook(color))
        self.squares[row_other][7] = Square(row_pawn, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_pawn, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_pawn, 4, King(color))
