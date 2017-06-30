# Breakout
# By: daemoz

import pygame, random, sys, levels
from pygame.locals import *

FPS = 30
SCREENWIDTH = 300
SCREENHEIGHT = 400
BALLSIZE = 1
# Colors
WHITE = (255, 255, 255)
RED   = (255,   0, 255)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PADDLECOLOR = WHITE
BALLCOLOR  = WHITE
def initPaddle():
    paddle = Paddle()
    return paddle
def initBricks(layout):
    bricks = []
    for brick in layout:
        # For each brick in layout, add new brick object with x and y
        bricks.append(Brick(brick[0], brick[1], brick[2], brick[3], brick[4]))
    return bricks
def initBalls(paddle):
    balls = []
    for x in xrange(1):
        balls.append( Ball(balls, paddle) )
    return balls
def main():
    global SCREENWIDTH, display
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    paddle = initPaddle()
    bricks = initBricks(levels.level2())
    balls = initBalls(paddle)
    while True:
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    paddle.move('left', True)
                elif event.key == K_RIGHT:
                    paddle.move('right', True)
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    paddle.move('left', False)
                elif event.key == K_RIGHT:
                    paddle.move('right', False)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        paddle.drawPaddle()
        drawBricks(bricks)
        drawBalls(balls, bricks)
       # ball.moveBall(bricks)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def drawBricks(bricks):
    for brick in bricks:
        brick.drawBrick()
def drawBalls(balls, bricks):
    for ball in balls:
        ball.moveBall(bricks)
class Paddle(object):
    def __init__(self):
        self.color = PADDLECOLOR
        self.x = SCREENWIDTH/2
        self.y = SCREENHEIGHT-10
        self.movingLeft = False
        self.movingRight = False
        self.width = 70
        self.height = 7
    def move(self, key, state):
        if key == 'left':
            self.movingLeft = state
        elif key == 'right':
            self.movingRight = state
    def movePaddle(self):
        if self.movingLeft == True:
            self.x -= 5
        if self.movingRight == True:
            self.x += 5
    def drawPaddle(self):
        self.movePaddle()
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height)) 
class Brick(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def drawBrick(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
class Ball(object):
    def __init__(self, balls, paddle):
        self.x = SCREENWIDTH/2
        self.y = SCREENHEIGHT/2 - ( random.randint(1,700))
        self.size = BALLSIZE
        self.xVec = random.randint(-3,3)
        self.yVec = 4
        self.balls = balls
        self.paddle = paddle
    def bounceX(self):
        self.xVec = -self.xVec
    def bounceY(self):
        self.yVec = -self.yVec
    def bouncePaddle(self):
        paddleCenter = self.paddle.x + self.paddle.width/2.0
        bounceDir = ( self.x - paddleCenter ) / self.paddle.width/2.0
        self.yVec = -self.yVec
        self.xVec += bounceDir
        print( bounceDir )
    def checkWalls(self):
        #Side walls
        if self.x + BALLSIZE >= SCREENWIDTH: 
            self.x = SCREENWIDTH - BALLSIZE
            self.bounceX()
        if self.x - BALLSIZE <= 0:
            self.x = 1 + BALLSIZE
            self.bounceX()
        #Top
        if self.y-BALLSIZE <= 0:
            self.bounceY()
        #Paddle zone
        if self.y+BALLSIZE >= self.paddle.y:
            self.bounceY()
           # if self.x+BALLSIZE >= self.paddle.x and self.x-BALLSIZE <= self.paddle.x+self.paddle.width:
            #    self.bouncePaddle()
        #Bottom
        if self.y+BALLSIZE >= SCREENHEIGHT:
            if len(self.balls) == 1:
                gameOver()
            else:
                self.balls.remove(self)
    def checkCollisions(self, bricks):
        for brick in bricks:
            if self.x+BALLSIZE >= brick.x and self.x-BALLSIZE <= brick.x+brick.width:
                if self.y+BALLSIZE >= brick.y and self.y-BALLSIZE <= brick.y+brick.height:
                    bricks.remove(brick)
                    self.bounceY()
    def moveBall(self, bricks):
        self.checkWalls() 
        self.x += self.xVec
        self.x = int(self.x)
        self.y += self.yVec
        self.y = int(self.y)
        self.checkCollisions(bricks)
        self.drawBall()
    def drawBall(self):
        pygame.draw.circle(display, BALLCOLOR, (self.x, self.y), BALLSIZE)
def gameOver():
    print("You lose!")
if __name__ == '__main__':
    main()
