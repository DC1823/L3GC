import pygame
from pygame.locals import *
from figu import *
from luces import *
from RayTracer import RayTracer
from mats import *

Width = 550
Height = 550
pygame.init()
pantalla = pygame.display.set_mode((Width, Height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
pantalla.set_alpha(None)
rayTracer = RayTracer(pantalla)
rayTracer.escena.append(Pyramid(pos=(0,0,-10),Width=1,Height=1,dp=1,rttn=(1,1,1),mat=snow()))
rayTracer.escena.append(Pyramid(pos=(-1,0,-5),Width=1,Height=1,dp=1,rttn=(1,5,1),mat=glass()))
rayTracer.luces.append(AmbientLight(intens=1))
rayTracer.luces.append(DirectionalLight(dir=(1,1,1),intens=3,col=(1,1,1)))
rayTracer.luces.append(PointLight(puntop=(5,-5,-15), intens=6,col=(1,1,0)))
corriendo = True
rayTracer.rayclear()
rayTracer.raytRend()

while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                corriendo = False
    pygame.display.flip()
pan = pygame.Rect(0, 0, Width, Height)
sb = pantalla.subsurface(pan)
pygame.image.save(sb, "output.png")
pygame.quit()