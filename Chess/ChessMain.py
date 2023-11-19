import pygame as p
import pygame.draw

from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
playerClicks = []

'''
Initialize a dictionary for the images that will be called once in main
'''


def loadImages():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
Main driver, handles input and updates the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode(size=(WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    loadImages()  # Load images (only done once)
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                selectAndMovePieces(gs)
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics within the game
'''


def drawGameState(screen, gs):
    # Possible to add piece highlight here
    drawBoard(screen)
    drawHighlight(screen)
    drawPieces(screen, gs.board)


'''
Draw the squares on the board
'''


def drawBoard(screen):
    light = [237, 210, 175]
    dark = [173, 129, 90]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = light if (row + col) % 2 == 0 else dark
            pygame.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawHighlight(screen):
    if len(playerClicks) != 0:
        darkHighlight = [58, 118, 49]
        lightHighlight = [114, 165, 106]
        color = lightHighlight if (playerClicks[0][1] + playerClicks[0][0]) % 2 == 0 else darkHighlight
        pygame.draw.rect(screen, color, p.Rect(playerClicks[0][1] * SQ_SIZE, playerClicks[0][0] * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using the current game state
'''


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != '_':
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Selects the move on the game board, and fills playerClicks with these (legal) coordinates.
The board then gets updated.
'''


def selectAndMovePieces(gs):
    col_pos = int(p.mouse.get_pos()[0] / SQ_SIZE)
    row_pos = int(p.mouse.get_pos()[1] / SQ_SIZE)
    if len(playerClicks) == 0:  # First click
        firstClick(gs, row_pos, col_pos)
    elif len(playerClicks) == 1:  # Second click
        secondClick(row_pos, col_pos)
        updateGameBoard(gs)


'''
Select the first click
'''


def firstClick(gs, row_pos, col_pos):
    if legalFirstMove(gs, row_pos, col_pos):
        pieceCoord = (row_pos, col_pos)
        playerClicks.append(pieceCoord)


'''
Select the second click
'''


def secondClick(row_pos, col_pos):
    if legalSecondMove():
        pieceCoord = (row_pos, col_pos)
        playerClicks.append(pieceCoord)


'''
Updates the game board based on the state of playerClicks
'''


def updateGameBoard(gs):
    # Update game board
    piece1 = gs.board[playerClicks[0][0]][playerClicks[0][1]]
    gs.board[playerClicks[0][0]][playerClicks[0][1]] = "_"
    gs.board[playerClicks[1][0]][playerClicks[1][1]] = piece1
    playerClicks.clear()  # Empty playerClicks


'''
Ensure that the first click is legal
'''


def legalFirstMove(gs, row_pos, col_pos):
    return gs.board[row_pos][col_pos] != "_"


'''
Ensure that the second click is legal
'''


def legalSecondMove():
    return True


'''
Standard python convention, this just runs main
'''

if __name__ == "__main__":
    main()
