import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1100,600

SCREEN = pygame.display.set_mode(SIZE)

RED_COLOR = 255,0,0
BLACK_COLOR = 0,0,0
WHITE_COLOR = 255,255,255
BLUE_COLOR = 0,0,255

bg_music = pygame.mixer.Sound("theme.ogg")
bg_music.play()

move_x = 0

ship = pygame.image.load("player.png")
ship_w = ship.get_width()
ship_h = ship.get_height()
ship_x = (WIDTH // 2) - (ship_w // 2)
ship_y = HEIGHT - ship_h - 10

enemy_ship = pygame.image.load("enemy.png")
enemy_w = enemy_ship.get_width()
enemy_h = enemy_ship.get_height()

enemyList = []
rows = 3
cols = WIDTH // enemy_w - 1
enemyRect = []
for i in range(rows):
    for j in range(cols):
        rect_x = (enemy_w + 5) * j
        rect_y = (enemy_h + 5) * i
        enemyList.append([rect_x, rect_y])
        enemyRect.append(pygame.Rect(rect_x, rect_y, enemy_w, enemy_h))

bullet_sound = pygame.mixer.Sound("sound_3.wav")

bullet_w = 10
bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
bullet_y = ship_y
move_bullet = 0

while True:
    bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
    # Events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()  # quit python

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 3
            elif event.key == pygame.K_LEFT:
                move_x = -3
            elif event.key == pygame.K_SPACE:
                move_bullet = -5
                bullet_sound.play()
        else:
            move_x = 0

    SCREEN.fill(WHITE_COLOR)

    for i in range(len(enemyList)):
        SCREEN.blit(enemy_ship, 
        (enemyList[i][0], enemyList[i][1]))

    bullet_rect = pygame.draw.rect(SCREEN, RED_COLOR, 
    [bullet_x, bullet_y, bullet_w, bullet_w])
    SCREEN.blit(ship, (ship_x, ship_y))

    ship_x += move_x
    bullet_y += move_bullet

    for i in range(len(enemyRect)):
        if bullet_rect.colliderect(enemyRect[i]):
            del enemyRect[i]
            del enemyList[i]
            bullet_y = ship_y
            move_bullet = 0
            break

    if bullet_y < 0:
        bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
        bullet_y = ship_y
        move_bullet = 0

    # to update the screen
    pygame.display.flip()