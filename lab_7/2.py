import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("music")


kilemger = pygame.transform.scale(pygame.image.load("C:/Users/User/Downloads/kilemgerkeide.jpg"), (WIDTH, HEIGHT))
kunzharyq = pygame.transform.scale(pygame.image.load("C:/Users/User/Downloads/saujurek.jpg"), (WIDTH, HEIGHT))
arshat = pygame.transform.scale(pygame.image.load("C:/Users/User/Downloads/arshat.jpg"), (WIDTH, HEIGHT))

arrP = [kilemger, kunzharyq, arshat]
arrM = [
    "C:/Users/User/Downloads/kilemger-keide.mp3",
    "C:/Users/User/Downloads/Kunzharyq-sau zhurek.mp3",
    "C:/Users/User/Downloads/sagan.mp3"
]

index = 0 
is_playing = False 


X_BUTTON_RECT = pygame.Rect(WIDTH - 50, 10, 40, 40)

def play_music():
    global is_playing
    pygame.mixer.music.load(arrM[index])
    pygame.mixer.music.play()
    is_playing = True

running = True
while running:
    screen.blit(arrP[index], (0, 0))  
   
    pygame.draw.rect(screen, (200, 0, 0), X_BUTTON_RECT)  
    pygame.draw.line(screen, (255, 255, 255), (WIDTH - 45, 15), (WIDTH - 15, 45), 3)  
    pygame.draw.line(screen, (255, 255, 255), (WIDTH - 15, 15), (WIDTH - 45, 45), 3)  

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.mixer.music.stop()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if not is_playing:
                    play_music()

            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                is_playing = False

            elif event.key == pygame.K_RIGHT:  
                index = (index + 1) % len(arrM)
                play_music()

            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(arrM)
                play_music()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if X_BUTTON_RECT.collidepoint(event.pos):  
                running = False
                pygame.mixer.music.stop()

pygame.quit()  
