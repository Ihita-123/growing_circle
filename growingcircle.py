import pygame
pygame.init()
screen= pygame.display.set_mode((500,500))
screen.fill((255,0,0))
black=(0,0,0)
pygame.display.update()

class circle():
    def __init__(self,color,pos,radius,width):
        self.circlecolor=color
        self.circlepos=pos
        self.circleradius=radius
        self.circlewidth=width
        self.circlesurface=screen


    def draw(self):
        self.drawcircle=pygame.draw.circle(self.circlesurface,self.circlecolor,self.circlepos,self.circleradius,self.circlewidth)

    def grow(self,r):
        self.circleradius+=r
        self.drawcircle=pygame.draw.circle(self.circlesurface,self.circlecolor,self.circlepos,self.circleradius,self.circlewidth)


circle1=circle(black,(250,300),3,0)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill((255,0,0))
            circle1.draw()
            pygame.display.update()
        elif event.type== pygame.MOUSEBUTTONUP:
            screen.fill((255,0,0))
            circle1.grow(3)
            pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

            


