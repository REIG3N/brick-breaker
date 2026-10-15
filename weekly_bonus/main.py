import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

PADDLE_WIDTH = 200
PADDLE_HEIGHT = 20

player = pygame.FRect(
    screen.get_width() / 2 - PADDLE_WIDTH / 2,
    screen.get_height() - PADDLE_HEIGHT,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
)

player_area = pygame.Rect(
    0,
    screen.get_height() - PADDLE_HEIGHT,
    screen.get_width(),
    PADDLE_HEIGHT,
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    pygame.draw.circle(screen, "blue", (50, 50), 25)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player.x -= 800 * dt
    if keys[pygame.K_d]:
        player.x += 800 * dt

    player.clamp_ip(player_area)

    pygame.draw.rect(screen, "red", player)




    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000  # limits FPS to 60
pygame.quit()
