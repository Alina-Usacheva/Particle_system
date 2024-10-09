import pygame
import sys
import random
import math

pygame.init()

window_width = 800
window_height = 600

black = (0, 0, 0)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Particle system')

# Параметры частиц
particle_radius = 10
particle_speed = 200 / (5 * 60)  # Скорость движения за 3 секунды (60 кадров в секунду)
particle_fade_speed = 255 / (5 * 60)  # Скорость изменения прозрачности за 3 секунды (60 кадров в секунду)
particle_opacity_lst = [150, 0, 200, 0, 255, 0]  # Список начальной прозрачности

clock = pygame.time.Clock()

running = True
mouse_pressed = False  # Флаг для отслеживания зажатой кнопки мыши
particles = []  # Список для хранения всех созданных частиц
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False
    window.fill(black)

    if mouse_pressed:
        # Создание новых частиц при зажатой мышке
        mouse_x, mouse_y = pygame.mouse.get_pos()
        particle_opacity = particle_opacity_lst[random.randrange(6)]  # Начальная прозрачность
        particle_angle = random.uniform(-70, -110)  # Случайный угол движения
        particle_speed_x = particle_speed * math.cos(math.radians(particle_angle))
        particle_speed_y = particle_speed * math.sin(math.radians(particle_angle))
        particle_position_x = [mouse_x, mouse_x - 7, mouse_x + 7, mouse_x - 4, mouse_x + 4]
        particles.append((particle_position_x[random.randrange(5)], mouse_y, particle_opacity, particle_speed_x, particle_speed_y))

    # Рисование и обновление состояния частиц
    new_particles = []
    for x, y, opacity, speed_x, speed_y in particles:
        # Рисование частицы
        particle = pygame.Surface((particle_radius * 2, particle_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(particle, (255, 255, 255, opacity), (particle_radius, particle_radius), particle_radius)
        window.blit(particle, (x - particle_radius, y - particle_radius))

        # Движение частицы и уменьшение прозрачности
        x += speed_x
        y += speed_y
        opacity = max(opacity - particle_fade_speed, 0)

        # Проверка на завершение анимации частицы
        if opacity > 0:
            new_particles.append((x, y, opacity, speed_x, speed_y))

    particles = new_particles
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
