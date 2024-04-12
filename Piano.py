#Ініціалізація Pygame
import pygame
pygame.init()

#Розміри вікна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

#Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Шлях до папки зі звуковими файлами


#Завантаження звукових файлів
sound_files = {
    pygame.K_a: pygame.mixer.Sound("sound1.wav"),
    pygame.K_s: pygame.mixer.Sound("sound2.wav"),
    pygame.K_d: pygame.mixer.Sound("sound3.wav"),
    pygame.K_f: pygame.mixer.Sound("sound4.wav"),
    pygame.K_g: pygame.mixer.Sound("sound5.wav"),
    pygame.K_h: pygame.mixer.Sound("sound6.wav"),
    pygame.K_j: pygame.mixer.Sound("sound7.wav"),
}

#Розміщення клавіш на екрані
key_positions = {
    pygame.K_a: (50, 50),
    pygame.K_s: (150, 50),
    pygame.K_d: (250, 50),
    pygame.K_f: (350, 50),
    pygame.K_g: (450, 50),
    pygame.K_h: (550, 50),
    pygame.K_j: (650, 50),
}

#Ініціалізація вікна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Піаніно")

#Завантаження фонового зображення
background = pygame.Surface(window.get_size())
background.fill(WHITE)

#Основний цикл програми
running = True
while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in sound_files:
                sound_files[event.key].play()

    # Відображення фонового зображення
    window.blit(background, (0, 0))

    # Малювання клавіш на екрані
    for key, position in key_positions.items():
        pygame.draw.rect(window, BLACK, (position[0], position[1], 100, 200))
        pygame.draw.rect(window, WHITE, (position[0] + 5, position[1] + 5, 90, 190))

    # Оновлення вікна
    pygame.display.update()

# Завершення роботи Pygame
pygame.quit()