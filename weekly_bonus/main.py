import pygame
from levels import bricks

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

DOME_WIDTH = 300
DOME_HEIGHT = 60

PADDLE_WIDTH = DOME_WIDTH * 0.7
PADDLE_HEIGHT = DOME_HEIGHT * 0.7

player = pygame.FRect(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
player.midbottom = (screen.get_width() / 2, screen.get_height())

paddle_shape = pygame.FRect(0, 0, DOME_WIDTH, DOME_HEIGHT * 2)

margin = (DOME_WIDTH - PADDLE_WIDTH) / 2
player_area = pygame.FRect(
    margin,
    screen.get_height() - PADDLE_HEIGHT,
    screen.get_width() - 2 * margin,
    PADDLE_HEIGHT,
)

game_ball = pygame.FRect(
    screen.get_width() / 2,
    screen.get_height() / 2,
    50,
    50
)

brick_length = 20
brick_width = 60


speed = pygame.Vector2(550, 550)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")


    game_ball = game_ball.move(speed[0] * dt, speed[1] * dt)

    if game_ball.left <= 0 or game_ball.right >= screen.get_width():
        speed[0] = -speed[0]
    if game_ball.top <= 0 :
        speed[1] = -speed[1]
    game_ball.clamp_ip(screen.get_rect())



    if game_ball.colliderect(player) and speed[1] > 0:

        player_zone_1 = player.left + player.width / 7
        player_zone_2 = player_zone_1 + player.width / 7
        player_zone_3 = player_zone_2 + player.width / 7
        player_zone_4 = player_zone_3 + player.width / 7
        player_zone_5 = player_zone_4 + player.width / 7
        player_zone_6 = player_zone_5 + player.width / 7


        if game_ball.centerx < player_zone_1:
            speed.from_polar((550, -150))
        elif game_ball.centerx < player_zone_2:
            speed.from_polar((550, -130))
        elif game_ball.centerx < player_zone_3:
            speed.from_polar((550, -110))
        elif game_ball.centerx < player_zone_4:
            speed.from_polar((550, -90))
        elif game_ball.centerx < player_zone_5:
            speed.from_polar((550, -70))
        elif game_ball.centerx < player_zone_6:
            speed.from_polar((550, -50))
        else:
            speed.from_polar((550, -30))


        game_ball.bottom = player.top

    pygame.draw.circle(
        surface=screen,
        color='blue',
        center=game_ball.center,
         radius=game_ball.width / 2
    )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player.x -= 800 * dt
    if keys[pygame.K_d]:
        player.x += 800 * dt

    player.clamp_ip(player_area)

    paddle_shape.centerx = player.centerx
    paddle_shape.centery = screen.get_height()
    pygame.draw.ellipse(screen, "orange", paddle_shape)


    for brick in bricks:
        pygame.draw.rect(screen, "white", brick)

    indice = game_ball.collidelist(bricks)
    if indice != -1 :
        brique_overlap = game_ball.clip(bricks[indice])
        if brique_overlap.width > brique_overlap.height:
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
        bricks.pop(indice)



    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000  # limits FPS to 60
pygame.quit()

