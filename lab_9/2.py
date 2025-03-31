import pygame
import random


pygame.init()

# параметры экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Размер клетки для сетки

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK=(0,0,0)

# Настройки игры
FPS = 10  # Скорость змейки

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Шрифт для отображения веса еды
font = pygame.font.SysFont(None, 24)

# Змейка
snake = [(WIDTH // 2, HEIGHT // 2)]  # Начальное положение змейки
direction = RIGHT  # Начальное направление змейки

# Еда
food = []
food_timer = {}  # Словарь с таймерами еды

def generate_food():
    """Создает случайную еду с разным весом и таймером удаления."""
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    weight = random.randint(1, 5)  # Вес еды (1-5 очков)
    food.append((x, y, weight))
    food_timer[(x, y)] = pygame.time.get_ticks() + random.randint(3000, 6000)  # Таймер 3-7 сек.

generate_food()

running = True
while running:
    screen.fill(BLACK)  # Заполняем фон белым

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Движение змейки
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0] * CELL_SIZE, head_y + direction[1] * CELL_SIZE)

    # Проверка столкновений с границами или самой собой
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        running = False  # Конец игры

    snake.insert(0, new_head)

    # Проверка съеденной еды
    ate_food = None
    for f in food:
        if new_head[:2] == f[:2]:  # Если змейка попала на еду
            ate_food = f
            break

    if ate_food:
        food.remove(ate_food)
        del food_timer[(ate_food[0], ate_food[1])]
        generate_food()  # Создаем новую еду
    else:
        snake.pop()  # Удаляем хвост (если не съели еду)

    # Проверка таймеров еды
    current_time = pygame.time.get_ticks()
    food = [f for f in food if food_timer.get((f[0], f[1]), current_time) > current_time]
    food_timer = {pos: t for pos, t in food_timer.items() if t > current_time}

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Отрисовка еды
    for f in food:
        pygame.draw.rect(screen, RED, (f[0], f[1], CELL_SIZE, CELL_SIZE))
        weight_text = font.render(str(f[2]), True, BLUE)
        screen.blit(weight_text, (f[0] + 5, f[1] + 2))

    pygame.display.flip()
    pygame.time.delay(1000 // FPS)

pygame.quit()
