import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мем Вьюер")


categories = ["Категорія 1", "Категорія 2", "Категорія 3"]
images = {
    "Категорія 1": [pygame.image.load("meme1.jpg"), pygame.image.load("meme2.jpg"), pygame.image.load("meme3.jpg")],
    "Категорія 2": [pygame.image.load("meme4.jpg"), pygame.image.load("meme5.jpg"), pygame.image.load("meme6.jpg")],
    "Категорія 3": [pygame.image.load("meme7.jpg"), pygame.image.load("meme8.jpg"), pygame.image.load("meme9.jpg")]
}

selected_image = None

def show_random_mem(selected_category):
    global selected_image
    if selected_category in images:
        selected_image = random.choice(images[selected_category])

# Функція для відображення кнопок
def draw_buttons():
    button_y = 50
    for category in categories:
        button_rect = pygame.Rect(50, button_y, 200, 30)
        pygame.draw.rect(window, (0, 0, 255), button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(category, True, WHITE)
        window.blit(text, (button_rect.x + 10, button_rect.y + 5))
        button_y += 40

# Головний цикл програми
game = True
while game:
    window.fill(WHITE)

    draw_buttons()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_y = 50
                for category in categories:
                    if 50 <= mouse_x <= 250 and button_y <= mouse_y <= button_y + 30:
                        show_random_mem(category)
                    button_y += 40

    # Відображення вибраного зображення
    if selected_image:
        screen.blit(selected_image, (350, 200))

    pygame.display.update()  # Оновлення екрану

pygame.quit()
