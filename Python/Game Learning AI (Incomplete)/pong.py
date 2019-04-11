import pygame
import random

FPS = 60

window_width = 400
window_height = 400

paddle_width = 10
paddle_height = 60

ball_width = 10
ball_height = 10

paddle_speed = 2
ball_x_speed = 3
ball_y_speed = 2

PADDLE_BUFFER = 10 #distance from edge of the window

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.setmode(window_width, window_height)

def drawBall(ballXpos, ballYpos):
    ball = pygame.rect(ballXpos, ballYpos, ball_width, ball_height)
    pygame.draw.rect(screen, white, ball)

def drawPaddleMe(paddle2Ypos):
    paddleMe = pygame.rect(PADDLE_BUFFER, paddle2Ypos, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, paddleMe)

def AIPaddle(paddle1Ypos):
    AI = pygame.rect(window_width-PADDLE_BUFFER-paddle_width, paddle1Ypos, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, AI)

def updateBall(paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection):
    ballXpos = ballXpos + ballXDirection*ball_x_speed
    ballYpos = ballYpos + ballYDirection*ball_y_speed
    score = 0

    if(ballXpos <= PADDLE_BUFFER + paddle_width and ballYpos + ball_height >= paddle1Ypos and ballYpos-ball_height<=paddle2Ypos+paddle_height):
        ballXDirection = -1
    elif(ballXpos<=0):
        ballXDirection = 1
        score = -1
        return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]

    if(ballXpos >= window_width - paddle_width - PADDLE_BUFFER and ballYpos + ball_height >= paddle2Ypos and ballYpos - ball_height <= paddle2Ypos + paddle_height):
        ballXDirection = -1
    elif(ballXpos >= window_width-ball_width):
        ballXDirection = -1
        score = 1
        return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]

    if(ballYpos <= 0):
        ballYpos = 0
        ballYDirection = 1
    elif(ballYpos>=window_height-ball_height):
        ballYpos = window_height - ball_height
        ballYDirection = -1
    return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]

def updateAIPaddle(action, paddle1Ypos):
    if(action[1] == 1):
        paddle1Ypos = paddle1Ypos - paddle_speed
    if(action[2] == 1):
        paddle1Ypos = paddle1Ypos + paddle_speed

    if(paddle1Ypos<0):
        paddle1Ypos = 0
    if(paddle1Ypos > window_height-paddle_height):
        paddle1Ypos = window_height - paddle_height
    return paddle1Ypos

def updateAIPaddle(action, ballYpos):
    if(action[1] ==1):
        paddle2Ypos = paddle2Ypos - paddle_speed
    if(action[2] == 1):
        paddle2Ypos = paddle2Ypos + paddle_speed

    if(paddle2Ypos<0):
        paddle2Ypos = 0
    if(paddle2Ypos > window_height-paddle_height):
        paddle2Ypos = window_height - paddle_height
    return paddle2Ypos

class PongGame:
    def __init__(self):
        num = random.randInt(0, 9)
        self.tally = 0
        #Initialize pos of paddle
        self.paddle1Ypos = window_height/2 - paddle_height/2
        self.paddle2Ypos = window_height/2 - paddle_height/2

        self.ballXDirection = 1
        self.ballYDirection = 1

        self.ballXpos = window_height/2 - ball_width/2

    def getPresentFrame(self):
        pygame.event.pump()
        screen.fill(BLACK)
        drawPaddleMe(self.paddle2Ypos)
        AIPaddle(self.paddle1Ypos)

        drawBall(self.ballXpos, self.ballYpos)

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())

        pygame.display.flip()

        return image_data

    def getNextFrame(self, action):
            pygame.event.pump()
            score = 0
            screen.fill(BLACK)
            #update our paddle
            self.paddle1YPos = updatePaddle1(action, self.paddle1YPos)
            drawPaddle1(self.paddle1YPos)
            #update evil AI paddle
            self.paddle2YPos = updatePaddle2(self.paddle2YPos, self.ballYPos)
            drawPaddle2(self.paddle2YPos)
            #update our vars by updating ball position
            [score, self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection] = updateBall(self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection)
            #draw the ball
            drawBall(self.ballXPos, self.ballYPos)
            #get the surface data
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            #update the window
            pygame.display.flip()
            #record the total score
            self.tally = self.tally + score
            print "Tally is " + str(self.tally)
            #return the score and the surface data
            return [score, image_data]
