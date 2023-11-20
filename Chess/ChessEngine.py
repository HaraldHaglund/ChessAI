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

    '''
    Generates all valid moves CONSIDERING pins.
    '''
    def getValidMoves(self):
        pass

    '''
    Generates all "syntax" possible moves, NOT considering pins.
    '''

    def getPossibleMoves(self):
        pass

