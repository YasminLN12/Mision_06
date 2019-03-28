#Autor: Yasmín Landaverde Nava
#Descripción: Dibuja un espirógrafo


import math
import pygame

ANCHO = 800
ALTO = 800

NEGRO = (0, 0, 0)
DEEP_PINK = (255, 20, 147)
DARK_ORANGE = (255, 140, 0)

def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(NEGRO)

        radio = 100
        for angulo in range(0, r//math.gcd(r, R)*360, 1):
            ang = math.radians(angulo)
            x = int(radio * math.cos(ang))
            y = int(radio * math.sin(ang))
            pygame.draw.circle(ventana, DEEP_PINK, (x+ANCHO//2, ALTO//2-y), 1)

            for r in range (0, 300, 5):
               k = r/R
            x = int(R*(((1-k)*math.cos(ang))-(l*k*math.cos(((1-k)/k)*ang))))
            y = int(R*(((1-k)*math.sin(ang))+(l*k*math.sin(((1-k)/k)*ang))))
            pygame.draw.circle(ventana, DARK_ORANGE, (x + ANCHO//2, ALTO//2-y), 1)





        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    r = int(input("Inserta r: "))
    R = int(input("Inserta R: "))
    l = float(input("Inserta l: "))
    dibujar(r,R,l)

main()