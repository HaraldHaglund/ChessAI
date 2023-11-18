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
