from const import *
from game import Game

import pygame
import sys


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQUARE_SIZE
                    clicked_col = dragger.mouseX // SQUARE_SIZE

                    # Check if clicked row has piece
                    if board.squares[clicked_row][clicked_col].has_piece():

                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)

                        # Save initial position in case invalid move is made
                        dragger.save_inital(event.pos)
                        dragger.drag_piece(piece)

                        # Show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    # Check to see if piece is dragged
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # Show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # Quit application
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
