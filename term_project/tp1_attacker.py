import pygame, math, random, copy, time

class Virus(object):
    def __init__(self, AI, x, y):
        self.AI = AI
        self.x, self.y = x, y
        # green
        self.color = (0,255,0)
        self.r = 10
        self.velocity = 3
        self.isMoving = False
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r*2, self.r*2)

        self.health = 4
        self.movingDir = (0, 0)

    def __eq__(self, other):
        return type(self) == type(other) \
            and (abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2)

    def move(self):
        pass

    def getAttacked(self):
        self.health -= 1
        print('virus ouch')
        if self.health <= 0:
            self.AI.viruses.remove(self)
            print('virus died')

    def drawHealthBar(self,screen):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,\
                (int(self.x), int(self.y)), self.r)

class AI(object):
    def __init__(self, app):
        self.app = app
        self.viruses = [ ]
        self.initialNumOfVirus = 3
        self.initializeViruses()

    def initializeViruses(self):
        for i in range(self.initialNumOfVirus):
            newVirus = Virus(self, self.app.width*.8, self.app.height*(4+i)/16)
            self.viruses.append(newVirus)

    def draw(self,screen):
        for virus in self.viruses:
            virus.draw(screen)
        