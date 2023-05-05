import pygame, sys
import math
import random

pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Circle(): # this is a node that has a next pointer
    def __init__(self,pX,pY,alpha,radius):
        self.pX = pX # previous node's x
        self.pY = pY # previous node's y
        self.x = 1
        self.y = 1
        self.radius = radius
        self.alpha = alpha
        self.weight = 10
        self.radian = 0
        self.next = None
    
    def update_cordinates(self):
        self.x = self.pX + math.cos(self.radian) * self.radius #If you increase the radian, the circle will rotate faster.
        self.y = self.pY - math.sin(self.radian) * self.radius
        self.radian += self.alpha


class CircleList():
    def __init__(self, screen):
        self.screen = screen
        self.circles = []
        self.head = None
    
    def add_circle(self, alpha, radius):
        if self.head == None:
            self.head = Circle(WIDTH/2, HEIGHT/2, alpha, radius)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next

            temp.next = Circle(temp.x,temp.y,alpha,radius)
    
    def draw(self):
        self.screen.fill((0,0,0))
        temp = self.head
        while(temp.next != None):
            temp.update_cordinates()
            temp.next.pX = temp.x
            temp.next.pY = temp.y
            pygame.draw.circle(self.screen,(255,0,0),(temp.x,temp.y),4,0)
            pygame.draw.aaline(self.screen, (255,255,255), (temp.pX,temp.pY), (temp.x,temp.y))
            temp = temp.next

        # at the end we cannot update the last circle bacuse it has not next node, so we are updating and drawing it outside of the loop
        temp.update_cordinates() 
        pygame.draw.circle(self.screen,(255,0,0),(temp.x,temp.y),4,0)
        pygame.draw.aaline(self.screen, (255,255,255), (temp.pX,temp.pY), (temp.x,temp.y))


circles = CircleList(screen)
circles.add_circle(0.05,10)
circles.add_circle(0.10,20)
circles.add_circle(0.15,30)
circles.add_circle(0.20,40)
circles.add_circle(0.25,50)
circles.add_circle(0.30,60)
circles.add_circle(0.35,70)
circles.add_circle(0.40,80)
circles.add_circle(0.45,90)
circles.add_circle(0.50,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[0]:
            #screen.fill([0,0,0])
            circles.draw()
            pygame.time.wait(50)
            pygame.display.update()
