import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# HEIGHT = 850
# WIDTH = 1000

##Jeremy's inspo >>> https://itnext.io/creating-space-invaders-clone-in-pygame-ea0f5336c677

class Galactica:
    ##inspo code to change later
    screen = None
    enemies = []
    lazers = []
    lost = False
    ##
    
    def __init__ (self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Galactica")
        self.bgColor = (BLACK)

        ##inspo code needs to be changed (marked by double ##s)
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        endGalactica = False #does not end the session with these terms
        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        lazer = None
        
        while not endGalactica:
            if len(self.enemies) == 0:
                self.displayTest("You Won")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x < width - 20 else 0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endGalactica = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.lazers.append(Lazer(self, hero.x, hero.y))
            
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for enemy in self.enemies:
                enemy.draw()
                enemy.checkCollision(self)
                if (enemy.y > height):
                    self.lost = True
                    self.displayText("You Are Out of Here")
                
                for lazer in self.lazers:
                    lazer.draw()
                if not self.lost: hero.draw()

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))
        ###################################################
        
        # self.check = self.hero.checkCollision(self.hero, self.enemy1)
"""    
    def run_game (self):
        while True:
            pygame.time.wait(40)
            for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    sys.exit()

            # Moves the hero infinitely when key is held down
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                hero.x += 10
            if keys[pygame.K_LEFT]:
                hero.x -= 10
            if keys[pygame.K_UP]:
                hero.y -= 10
            if keys[pygame.K_DOWN]:
                hero.y += 10
                # hero.move(10, 0)
                print("move")
                print(hero.y)
                # hero.draw()

            # self.hero.move(self.hero.x, self.hero.y)
            # print(self)
            self.screen.fill(self.bgColor)
            hero.draw()
            enemy1.draw()
            # self.hero.move(1,1)
            # self.hero.move(10)
            # self.enemy1.checkCollision(self.hero, self.enemy1)
            # self.hero.inBounds()
            # if isinstance(self.enemy1, pygame.sprite.Rect):
            #     print("True")
            pygame.display.update()
"""
"""
class Character(pygame.sprite.Sprite):
    def __init__ (self, color, x, y): ##taling y, w, h for testing purposes
        super().__init__()
        self.rect = pygame.Rect(x, y)
        #self.screen = screen
        self.points = points
        self.color = color
        #self.w = w
        #self.h = h
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x)
"""

    #def move(self, dx, dy): 
        #self.x, self.y = self.x + dx, self.y + dy

    #def draw (self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        # self.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))


class Enemy:
    def __init__(self, galactica, x, y): ##taking out y, w, h for testing purposes
        #super().__init__(screen, color, x)
        #self.enemy_pos = [random.randint(0), 0]

        ##this code will need to be edited later to make it our own >> Jeremy
        self.x = x
        self.galactica = galactica
        self.y = y
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.galactica.screen, (81, 43, 88), pygame.Rect(self.x, self.y, self.size, self.size)) 
        self.y += 0.05

    def checkCollision(self, galactica):
        for lazer in galactica.lazers:
            if ( lazer.x < self.x + self.size and lazer.x > self.x - self.size and lazer.y < self.y + self.size and lazer.y > self.y - self.size ):
                galactica.lazers.remove(lazer)
        ##
        
    
"""   
    # Enemy moves straight down at a constant velocity
    def move(self, vel):
        self.y += vel

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            sys.exit()
            print(col)
"""
class Hero:
    def __init__ (self, galactica, x, y): 
        #super().__init__(self, screen, color, x, y)
    
        ##inspo code that needs to be changed
        self.x = x
        self.galactica = galactica
        self.y = y
    def draw(self):
        pygame.draw.rect(self.galactica.screen, (210, 250, 251), pygame.Rect(self.x, self.y, 8, 5))
        ##

""" 
    def inBounds(self): # makes the hero stay in the window
        if self.x == 0:
            self.move(10,0)
        elif self.x + 50 == 1000:
            self.move(-10,0)
        elif self.y == 0:
            self.move(0, 10)
        elif self.y + 50 == 850:
            self.move(0, -10)
"""

##Inspo code that needs to be changed
class Generator:
    def __init__(self, galactica):
        margin = 30
        width = 50
        for x in range(margin, galactica.width - margin, width):
            for y in range(margin, int(galactica.height / 2), width):
                galactica.enemies.append(Enemy(galactica, x, y))
class Lazer:
    def __init__(self, galactica, x, y):
        self.x = x
        self.y = y
        self.galactica = galactica
    def draw(self):
        pygame.draw.rect(self.galactica.screen, (254, 52, 110), pygame.Rect(self.x, self.y, 2, 4)  )
        self.y -= 2
                
##


            
#g = Galactica(1000, 800)
#hero = Hero(g.screen, RED, 500, 700, 50, 50)
#enemy1 = Enemy(g.screen, BLUE, 500, 100, 80, 80)

#g.run_game()
if __name__ == '__main__':
    galactica = Galactica(600, 400)
    #hero = Hero(galactica.screen, RED, 500, 700, 50, 50)
    #enemy1 = Enemy(galactica.screen, BLUE, 500, 100, 80, 80 )