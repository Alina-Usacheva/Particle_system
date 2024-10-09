import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация частиц")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255, 255)

# Список для хранения частиц
particles = []

# Основной цикл программы
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Добавление новых частиц при клике мыши
            x, y = pygame.mouse.get_pos()
            for _ in range(10):
                size = random.randint(15, 25)
                color = WHITE
                particles.append((x, y, size, (255, 255, 255)))

    screen.fill(BLACK)

    # Обновление и отрисовка частиц
    circle = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
    for particle in particles:
        x, y, size, color = circle
        pygame.draw.circle(circle, (255, 255, 255, 255), [x, y], size)
        y += 2  # Движение вниз
        circle.set_alpha(50)  # Уменьшение времени жизни частицы
        if color[3] <= 0:
            particles.remove(particle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
