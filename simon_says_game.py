import random as rn
import sys
import pygame

white = (255, 255, 255)
darkBlue = (0, 0, 150)
darkGreen = (0,150, 0)
darkRed = (150, 0, 0)
darkYellow =(180, 180, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)



class SimonSays:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((735, 850))
        pygame.display.set_caption("Simon Says")
        self.bgColor = (white)

        self.rSquare = pygame.Rect(10, 10, 350, 350) # default squares on screen
        self.bSquare = pygame.Rect(10, 375, 350, 350)
        self.gSquare = pygame.Rect(375, 375, 350, 350)
        self.ySquare = pygame.Rect(375, 10, 350, 350)

        self.level = Level()


    def run_ss(self):
        gameList = []
        userList = []
        indexV = 0
        keyPress = False

        while True:
            pygame.time.wait(40)
            
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                elif event.type == pygame.KEYDOWN: # this adds numbers which eventually will correspond to key presses and the squareson screen

                    if event.key == pygame.K_SPACE:
                        gameList += [rn.randrange(1,5)]
                        userList = []
                        indexV = 0
                        print(self.level.nextLevel()) # when you press space you "level up" (adds one number to gameList)

                    if event.key == pygame.K_q:
                        pygame.draw.rect(self.screen, red, self.rSquare)
                        userList += [1]
                        keyPress == True
                    elif event.key == pygame.K_w:
                        userList += [2]
                        pygame.draw.rect(self.screen, yellow, self.ySquare)
                        keyPress == True
                    elif event.key == pygame.K_a:
                        pygame.draw.rect(self.screen, blue, self.bSquare)
                        userList += [3]
                        keyPress == True
                    elif event.key == pygame.K_s:
                        pygame.draw.rect(self.screen, green, self.gSquare)
                        userList += [4]
                        keyPress == True

                elif event.type == pygame.KEYUP:
                    pygame.draw.rect(self.screen, darkRed, self.rSquare),
                    pygame.draw.rect(self.screen, darkBlue, self.bSquare),
                    pygame.draw.rect(self.screen, darkGreen, self.gSquare),
                    pygame.draw.rect(self.screen, darkYellow, self.ySquare)   
                
                print("gameList:", gameList)
                print("userList:", userList)
                
                pygame.display.update()
            if keyPress == True:
                keyPress = False
                if gameList[indexV] == userList[indexV]:
                    indexV += 1
                else:
                    sys.exit()


            # for index in range(len(userList)):          # this does what its supposed to but...
            #     if userList[index] != gameList[index]:  # im not sure how to make the userList reset after each level
            #         sys.exit()

                
                
                # if userList == gameList: 
                #     gameList += 
                #     userList = []     
            
                # if userList != gameList:
                    # sys.exit()
                # userList = []
            # if gameList != userList:
            #     sys.exit()
class Level:
    def __init__(self):
        self.levelNumber = 0

    def nextLevel(self):
        self.levelNumber += 1
        return self.levelNumber

    
ss = SimonSays()
ss.run_ss()



