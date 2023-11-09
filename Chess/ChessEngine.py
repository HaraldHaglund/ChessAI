class GameState():
    def __init__(self):
        self.whiteToMove = True
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', ],
            ['_',   '_',  '_', '_',  '_',  '_',  '_',  '_'],
            ['_',   '_',  '_', '_',  '_',  '_',  '_',  '_'],
            ['_',   '_',  '_', '_',  '_',  '_',  '_',  '_'],
            ['_',   '_',  '_', '_',  '_',  '_',  '_',  '_'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', ],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        # For the future, this allows us to represent all pieces in 5 bit binary, first two digits represent colour, last three type.
        # ie 10110 (22 in decimal) would represent a black queen
        self.none = 0
        self.king = 1
        self.pawn = 2
        self.knight = 3
        self.bishop = 4
        self.rook = 5
        self.queen = 6
        self.white = 8
        self.black = 16
