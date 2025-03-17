import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("red ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x, y = WIDTH // 2, HEIGHT // 2 
speed = 20  

running = True
while running:
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (x, y), radius)  
    pygame.display.update() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + radius + speed <= HEIGHT:
                y += speed
            if event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + radius + speed <= WIDTH:
                x += speed

pygame.quit()
