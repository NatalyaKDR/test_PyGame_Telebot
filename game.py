import pygame
import sys

pygame.init()

W = 500
H = 500
window = pygame.display.set_mode((W, H))
fps = 60
clock = pygame.time.Clock()


surf_comp=pygame.Surface((50,50))
surf_comp.fill((255,0,0))
rect_comp=surf_comp.get_rect()
rect_comp.x=300
rect_comp.y=300

surf_user=pygame.Surface((50,50))
surf_user.fill((255,255,0))
rect_user=surf_comp.get_rect()
rect_user.x=50
rect_user.y=50


left=False
right=False
up=False
down=False

#для бота
x='правее'
y='ниже'

coord_comp =(f'Кубик компа находится {x} и {y} вашего в координатах {rect_comp.x} по x и {rect_comp.y} по y')
f = open('coord.txt', 'w')
f.write(coord_comp)
f.close()



pygame.display.update()

while True:
    clock.tick(fps)

    window.fill((0,0,0))
    window.blit(surf_comp,rect_comp)
    window.blit(surf_user,rect_user)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key=pygame.key.get_pressed()
    if key [pygame.K_RIGHT]:
        rect_user.x+=5
        left = False
        right = True
        up = False
        down = False
    if key[pygame.K_LEFT]:
        rect_user.x-= 5
        left = True
        right = False
        up = False
        down = False
    if key[pygame.K_UP]:
        rect_user.y-= 5
        left = False
        right = False
        up = True
        down = False
    if key[pygame.K_DOWN]:
        rect_user.y+= 5
        left = False
        right = False
        up = False
        down = True

    if rect_user.x < rect_comp.x and rect_user.colliderect(rect_comp) and right and rect_comp.x>=0 and rect_comp.x<=445:
        rect_comp.x+=5

        if rect_user.x<rect_comp.x:
            x="правее"
        else:
            x = "левее"
        if rect_user.y<rect_comp.y:
            y="ниже"
        else:
            y = "выше"

        coord_comp = (f'Кубик компа находится {x} и {y} вашего в координатах {rect_comp.x} по x и {rect_comp.y} по y')
        print(coord_comp)
        f = open('coord.txt', 'w')
        f.write(coord_comp)
        f.close()

    elif rect_user.x > rect_comp.x and rect_user.colliderect(rect_comp) and left and rect_comp.x>=0 and rect_comp.x<=445:
        rect_comp.x-=5

        if rect_user.x < rect_comp.x:
            x = "правее"
        else:
            x = "левее"
        if rect_user.y < rect_comp.y:
            y = "ниже"
        else:
            y = "выше"

        coord_comp = (f'Кубик компа находится {x} и {y} вашего в координатах {rect_comp.x} по x и {rect_comp.y} по y')
        print(coord_comp)
        f = open('coord.txt', 'w')
        f.write(coord_comp)
        f.close()
    elif rect_user.y > rect_comp.y and rect_user.colliderect(rect_comp) and up and rect_comp.y>=0 and rect_comp.y<=445:
        rect_comp.y-=5

        if rect_user.x < rect_comp.x:
            x = "правее"
        else:
            x = "левее"
        if rect_user.y < rect_comp.y:
            y = "ниже"
        else:
            y = "выше"

        coord_comp = (f'Кубик компа находится {x} и {y} вашего в координатах {rect_comp.x} по x и {rect_comp.y} по y')
        print(type(coord_comp))
        f = open('coord.txt', 'w')
        f.write(coord_comp)
        f.close()
    elif rect_user.y < rect_comp.y and rect_user.colliderect(rect_comp) and down and rect_comp.y>=0 and rect_comp.y<=445:
        rect_comp.y+=5

        if rect_user.x < rect_comp.x:
            x = "правее"
        else:
            x = "левее"
        if rect_user.y < rect_comp.y:
            y = "ниже"
        else:
            y = "выше"

        coord_comp = (f'Кубик компа находится {x} и {y} вашего в координатах {rect_comp.x} по x и {rect_comp.y} по y')
        f = open('coord.txt', 'w')
        print(coord_comp)
        f.write(coord_comp)
        f.close()

    pygame.display.update()







