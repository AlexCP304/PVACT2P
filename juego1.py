import pygame
# inicializacion de pygame
pygame.init()
# inicializacion de la superficie del dibujo
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ejemplo 1")
# bucle principal del juego
jugando = True
while jugando:
    # comprobamos los eventos
    # comprobamos si se ha pulsado el boton de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # se pinta la ventana de un color
    # esto borra los posibles elementos que teniamos anteriormente
    ventana.fill(( 252, 243, 207 ))
    # todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # controlamos la frecuencia de refresco (fps)
    pygame.time.Clock().tick(60)
pygame.quit()
