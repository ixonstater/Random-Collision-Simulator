"""
Simulation of balls bouncing.
    Velocities after collision are randomly generated.
"""
from graphics import *
import math
from random import randrange
from random import triangular
from random import random
from random import seed
import time
class makeBallData:
    def __init__(self, radius, speedLimit):
        seed(random())
        self.xVel = triangular(-speedLimit,speedLimit)
        self.yVel = triangular(-speedLimit,speedLimit)
        self.radius = radius

def fillBallsArray(balls, ballsData, speedLimit, numBalls, radius):
    yPoints = []
    xPoints = []
    for i in range (0, math.floor(580/(radius*2.2))):
        for a in range (0, math.floor(580/(radius*2.2))):
            xPoints.append(i*radius*2.2+radius+10)
            yPoints.append(a*radius*2.2+radius+10)
    for i in range(0,numBalls):
        seed(random())
        xPoint = xPoints[i]
        yPoint = yPoints[i]
        ball = Circle(Point(xPoint, yPoint), radius)
        ball.setFill('red')
        balls.append(ball)
        ballsData.append(makeBallData(radius, speedLimit))

def placeBalls(balls, myWin):
    for i in range(0,len(balls)):
        balls[i].draw(myWin)
#-------------------------------------------------------
def sign(num):
    if(num>=0):
        return 1
    elif(num<0):
        return -1

def findColl(ballsData, balls, speedLimit):
    collisions = []
    for i in range(0, len(ballsData)-1):
        x1 = balls[i].getCenter().x
        y1 = balls[i].getCenter().y
        for a in range(i+1, len(ballsData)):
            x2 = balls[a].getCenter().x
            y2 = balls[a].getCenter().y
            if ((ballsData[i].radius*2)>=math.sqrt((y2-y1)**2+(x2-x1)**2)):
                pair = (i,a)
                collisions.append(pair)
                handleOverlap(ballsData, balls, pair)
    if (collisions == []):
        moveBalls(balls, ballsData)
    else:
        setVel(collisions, ballsData, balls, speedLimit)
        moveBalls(balls, ballsData)

def handleOverlap(ballsData, balls, pair):
    y1 = balls[pair[0]].getCenter().y
    x1 = balls[pair[0]].getCenter().x
    y2 = balls[pair[1]].getCenter().y
    x2 = balls[pair[1]].getCenter().x
    r = ballsData[pair[1]].radius
    yM = 0.1
    xM = 0.1
    if(math.sqrt((y2-y1)**2+(x2-x1)**2)-(y2-y1)>0):
        yM += (2*r*(y2-y1))/math.sqrt((y2-y1)**2+(x2-x1)**2)-(y2-y1)
    if(math.sqrt((y2-y1)**2+(x2-x1)**2)-(x2-x1)>0):
        xM += (2*r*(x2-x1))/math.sqrt((y2-y1)**2+(x2-x1)**2)-(x2-x1)
    balls[pair[1]].move(xM, yM)

def setVel(collisions, ballsData, balls, speedLimit):
    for i in range(0,len(collisions)):
        ball1 = collisions[i][0]
        ball2 = collisions[i][1]
        ballsData[ball1].yVel = triangular(-speedLimit, speedLimit)
        ballsData[ball1].xVel = triangular(-speedLimit, speedLimit)
        ballsData[ball2].yVel = triangular(-speedLimit, speedLimit)
        ballsData[ball2].xVel = triangular(-speedLimit, speedLimit)

def moveBalls(balls, ballsData):
    for i in range(0, len(ballsData)):
        x = balls[i].getCenter().x
        y = balls[i].getCenter().y
        r = ballsData[i].radius
        if (x <= r):
            # ballsData[i].xVel *= -1
            # balls[1].move((r-x+0.1), 0)
            balls[i].move(599-r, 0 )
        elif (x >= (600-r)):
            # ballsData[i].xVel *= -1
            # balls[i].move((x+r-599.9)*-1, 0)
            balls[i].move(-599+r, 0)
        if (y <= r):
            # ballsData[i].yVel *= -1
            # balls[1].move(0, (r-y+0.1))
            balls[i].move(0, 599-r)
        elif (y >= (600-r)):
            # ballsData[i].yVel *= -1
            # balls[i].move(0, (y+r-599.9)*-1)
            balls[i].move(0, -599+r)


    for i in range(len(balls)):
        balls[i].move(ballsData[i].xVel, ballsData[i].yVel)
#------------------------------------------------------------

def main():
    notDone = True
    ballsData = []
    balls = []
    speedLimit = float(input('Please enter a speed limit: '))
    numBalls = int(input('Please enter the number of balls: '))
    radius = float(input('Please enter a radius for the balls: '))
    myWin = GraphWin('Collisions', 600, 600, False)
    fillBallsArray(balls, ballsData, speedLimit, numBalls, radius)
    placeBalls(balls, myWin)
    myWin.update()
    while(notDone):
        findColl(ballsData, balls, speedLimit)
        myWin.update()
        time.sleep(0.001)
    try:
        myWin.getMouse()
        myWin.close()
    except:
        myWin.close()

if __name__ == "__main__":
    main()
