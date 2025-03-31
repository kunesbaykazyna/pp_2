import pygame

# Определение размеров окна
WIDTH, HEIGHT = 1200, 800
FPS = 90  # Частота обновления экрана

draw = False  # Флаг для рисования
radius = 2  # Радиус кисти
color = 'blue'  # Цвет по умолчанию
mode = 'pen'  # Режим рисования

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Управление временем
screen.fill(pygame.Color('white'))  # Заполнение экрана белым цветом
font = pygame.font.SysFont('None', 60)  # Шрифт для отображения текста

def drawLine(screen, start, end, width, color):
    """ Функция рисования линии между двумя точками """
    pygame.draw.line(screen, pygame.Color(color), start, end, width)

def drawCircle(screen, start, end, width, color):
    """ Функция рисования окружности """
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = abs(start[0] - end[0]) // 2
    pygame.draw.circle(screen, pygame.Color(color), center, radius, width)

def drawRectangle(screen, start, end, width, color):
    """ Функция рисования прямоугольника """
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def drawSquare(screen, start, end, color):
    """ Функция рисования квадрата """
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(min(x1, x2), min(y1, y2), size, size)
    pygame.draw.rect(screen, pygame.Color(color), rect)

def drawRightTriangle(screen, start, end, color):
    """ Функция рисования прямоугольного треугольника """
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y2), (x1, y2)]
    pygame.draw.polygon(screen, pygame.Color(color), points)

def drawEquilateralTriangle(screen, start, end, width, color):
    """ Функция рисования равностороннего треугольника """
    x1, y1 = start
    x2, y2 = end
    base = abs(x2 - x1)
    height = (3 ** 0.5 / 2) * base
    points = [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)]
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

def drawRhombus(screen, start, end, width, color):
    """ Функция рисования ромба """
    x1, y1 = start
    x2, y2 = end
    points = [((x1 + x2) // 2, y1), (x1, (y1 + y2) // 2), ((x1 + x2) // 2, y2), (x2, (y1 + y2) // 2)]
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

lastPos = (0, 0)  # Начальная позиция мыши

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_p:
                mode = 'pen'
            elif event.key == pygame.K_e:
                mode = 'erase'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_tri'
            elif event.key == pygame.K_u:
                mode = 'eq_tri'
            elif event.key == pygame.K_h:
                mode = 'rhombus'
            elif event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))
            elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                colors = {pygame.K_1: 'black', pygame.K_2: 'green', pygame.K_3: 'red', pygame.K_4: 'blue', pygame.K_5: 'yellow'}
                color = colors[event.key]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            prevPos = event.pos
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
        
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, color)
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, color)
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)
        
        if event.type == pygame.MOUSEMOTION and draw:
            if mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos

    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = font.render(str(radius), True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))
    
    pygame.display.flip()
    clock.tick(FPS)
