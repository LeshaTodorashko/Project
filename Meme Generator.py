import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мем Вьюер")


categories = ["Категорія 1", "Категорія 2", "Категорія 3"]
images = {
    "Категорія 1": [pygame.image.load("cat1.jpg"), pygame.image.load("cat2.jpg"), pygame.image.load("cat3.jpg"), pygame.image.load("cat4.jpg"), pygame.image.load("cat5.jpg"), pygame.image.load("cat6.jpg"), pygame.image.load("cat7.jpg"), pygame.image.load("cat8.jpg"), pygame.image.load("cat9.jpg"), pygame.image.load("cat10.jpg")],
    "Категорія 2": [pygame.image.load("internet1.jpg"), pygame.image.load("internet2.jpg"), pygame.image.load("internet3.jpg"), pygame.image.load("internet4.jpg"), pygame.image.load("internet5.jpg"), pygame.image.load('internet6.jpg'), pygame.image.load("internet7.jpg"), pygame.image.load("internet8.jpg"), pygame.image.load("internet9.jpg"), pygame.image.load("internet10.jpg")],
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
        window.blit(selected_image, (350, 200))

    pygame.display.update()  # Оновлення екрану

pygame.quit()
