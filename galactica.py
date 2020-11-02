import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

HEIGHT = 850
WIDTH = 1000

HSFile = "scores.txt"

class Galactica:
    def __init__ (self, width, height):
        
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Galactica-y")
        self.bgColor = (BLACK)
        self.timer = 0 # keeps track of time
        self.difficulty = 5
        self.difficultyTimer = 0
        self.enemyList = []
        self.dead = False

    def displayScore(self, text):
        """
        displays the score on screen
        """
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 60)
        textsurface = font.render(text, False, (44, 0, 62) )
        self.screen.blit(textsurface, (0, 0))
        
        #text for winning and losing
    def displayText(self, text):
        """
        displays text like "game over" or "you win"
        """
        pygame.font.init()
        font = pygame.font.SysFont('Calibri', 60)
        textsurface = font.render(text, False, (44, 0, 62) )
        self.screen.blit(textsurface, (600, 160))
        

    def checkCollision(self, sprite1, sprite2):  # moved this to the main game class

        """
        checks if two specified sprite objects collided
        """
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            self.dead = True
        
    

    def ScoreToFile(self):  

        """
        if this is the first time you play, a new file called "scores.txt" will 
        be created and your score will be written to it.
        Otherwise, your high score will be written to that file
        """
        try:
            with open(HSFile, "r") as f:
                if self.score > int(f.read()):
                    with open(HSFile, "w") as f:
                        f.write(str(self.score))

        except:
            with open(HSFile, "w") as f:
                f.write(str(self.score))
        f.close()
        
    def enemySpawn(self):
        """
        creates a new instance of Enemy.
        frequency of spawn is based off of the relationsip of the timer and difficulty variables.

        difficulty gradually counts down which increases the frequency
        """
        if not self.timer % self.difficulty: 
                xPos = random.randrange(0, 1000)
                yPos = random.randrange(-300, -100)
                e = Enemy(g.screen, GREY,  xPos, yPos, 50, 50 )
                self.enemyList.append(e)

    def increaseDifficulty(self):

        """
        when the difficulty timer reaches 300, the game gets harder and the difficulty timer resets
        and the difficulty variable gets smaller, increasing the frequency of enemies spawning
        """
        if self.difficultyTimer == 300: 
            self.difficultyTimer = 0
            if self.difficulty > 1:
                self.difficulty -= 1
            
       
    def run_game (self):
        # enemyList = []
        # dead = False

        while not self.dead:
            self.score = self.timer // 20
            pygame.time.wait(40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #self.displayText("You Won")

            # Moves the hero infinitely when key is held down
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                hero.rect.x += 10
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                hero.rect.x -= 10
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                hero.rect.y -= 10
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                hero.rect.y += 10
                #self.displayText("You Won") #placed this here for testing

                

            # self.hero.move(self.hero.x, self.hero.y)
            # print(self)self.checkCollision(hero, enemy)
            self.screen.fill(self.bgColor)
            hero.draw()
            #drawing of the screen starts here
            #which is why i had to put this here
            
            
            # self.displayScore(("Score: " + str(self.score)))
            self.enemySpawn()
            
            for enemy in self.enemyList: # draws each enemy in enemyList and tests for collisions
                enemy.move(5)
                enemy.draw()
                self.checkCollision(hero, enemy)
    
 
                
            hero.inBounds()
            # self.displayText("you lose")
            self.displayScore(("Score: " + str(self.score)))

            pygame.display.update()


            self.timer += 1
            self.difficultyTimer += 1
            self.increaseDifficulty()
            
            
            
        self.ScoreToFile() 
        


class Character(pygame.sprite.Sprite):
    def __init__ (self, screen, color, x, y, w, h):
        super().__init__()
        
        self.screen = screen
        # self.points = points
        self.color = color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        # self.rect = pygame.Rect(x, y, w, h)

    def move(self, dx, dy): 
        self.x, self.y = self.x + dx, self.y + dy

    def draw (self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # self.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))


class Enemy(Character):
    def __init__(self, screen, color, x, y, w, h):
        super().__init__(screen, color, x, y, w, h)
        self.enemy_pos = [random.randint(0, w), 0]
        
        
        
    # Enemy moves straight down at a constant velocity
    def move(self, vel):
        self.rect.y += vel

   

class Hero(Character):
    def __init__ (self, screen, color, x, y, w, h):
        super().__init__(screen, color, x, y, w, h)
    
    
    def inBounds(self): # makes the hero stay in the window
        if self.rect.x == 0:
            self.rect.x += 10
        elif self.rect.x + 10 == WIDTH:
            self.rect.x -= 10
        elif self.rect.y == 0:
            self.rect.y += 10
        elif self.rect.y + 10 == HEIGHT:
            self.rect.y -= 10



            
g = Galactica(WIDTH, HEIGHT)
hero = Hero(g.screen, RED, 500, 700, 10, 10)
g.run_game()