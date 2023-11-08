import pygame as p
import pygame.draw

from Chess import ChessEngine

WIDTH = HEIGHT = 512.0
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

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
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # Load images (only done once)
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within the game
'''


def drawGameState(screen, gs):
    # Add piece highlight or piece suggestion
    drawBoard(screen)
    drawPieces(screen, gs.board)


'''
Draw the squares on the board
'''

# TODO: Draw grid
def drawBoard(screen):
    blockSize = 20
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            rect = pygame.Rect(row, col, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)


'''
Draw the pieces on the board using the current game state
'''


def drawPieces(screen, board):
    pass


'''
Standard python convention
'''

if __name__ == "__main__":
    main()