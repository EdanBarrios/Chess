from const import *

import pygame


class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.inital_row = 0
        self.inital_col = 0

    # Blit Methods

    def update_blit(self, surface):
        # Texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # Image
        img = pygame.image.load(texture)
        # Rectangle
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # Blit
        surface.blit(img, self.piece.texture_rect)

    # Other methods

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos  # Tuple for coordinates (xcor, ycor)

    def save_inital(self, pos):
        self.initial_row = pos[1] // SQUARE_SIZE
        self.initial_col = pos[0] // SQUARE_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
