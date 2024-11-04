import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand = random.uniform(20, 50)
        a = self.velocity.rotate(rand)
        b = self.velocity.rotate(-rand)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2