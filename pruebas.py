import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 300))

font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
fps = 50

# Duración total del cronómetro en minutos
total_minutes = 3

# Convertir la duración total a segundos
total_seconds = total_minutes * 60

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el tiempo restante en función de los ticks
    milliseconds = clock.tick(fps)  # Obtener la cantidad de milisegundos transcurridos desde la última actualización
    seconds_elapsed = milliseconds / 1000  # Convertir los milisegundos a segundos
    total_seconds -= seconds_elapsed

    # Verificar si se ha alcanzado el tiempo límite
    if total_seconds <= 0:
        total_seconds = 0
        running = False

    # Calcular los minutos y segundos actuales
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Renderizar el texto del cronómetro
    time_text = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    text_surface = font.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 150))

    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
