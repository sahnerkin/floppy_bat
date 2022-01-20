import pygame
from bat import Bat
from constants import CLOCK_FREQUENCY

class ScoreCollider():
    def __init__(self, left, top, width, height, velocity):
        self._collider = pygame.Rect(left, top, width, height)
        self._velocity = velocity
        self._left = left

    def tick(self):
        self._left -= self._velocity/CLOCK_FREQUENCY

        if self._collider is None:
            return
        self._collider.left = self._left

        if self._collider.colliderect(Bat.getInstance().coll_rect):
            print("Score!")
            self._collider = None
