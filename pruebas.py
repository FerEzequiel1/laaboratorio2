import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear una pantalla
screen = pygame.display.set_mode((800, 600))

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variable para indicar si el juego está en pausa
game_paused = False

# Posición inicial del objeto en movimiento
object_position = [400, 300]
object_velocity = [2, 2]
 
vida = 3



# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Pausar o reanudar el juego
                game_paused = not game_paused
    if not game_paused:
        # Actualizar la posición del objeto
        object_position[0] += object_velocity[0]
        object_position[1] += object_velocity[1]

        # Lógica adicional y colisiones

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, object_position, 20)
    separacion = 20
    for cuadrado in range(vida):
        pygame.draw.rect(screen,WHITE,(separacion,100,50,50))
        pygame.draw.rect(screen,"black",(separacion,100,50,50),5)
        separacion += 50

    if game_paused:
        # Mostrar mensaje de pausa
        pause_font = pygame.font.Font(None, 36)
        pause_text = pause_font.render("Juego en pausa", True, WHITE)
        screen.blit(pause_text, (300, 250))

    pygame.display.flip()
