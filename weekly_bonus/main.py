import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

PADDLE_WIDTH = 600
PADDLE_HEIGHT = 100

player = pygame.FRect(
    screen.get_width() / 2 - PADDLE_WIDTH / 2,
    screen.get_height() - PADDLE_HEIGHT,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
)

player_area = pygame.FRect(
    0,
    screen.get_height() - PADDLE_HEIGHT,
    screen.get_width(),
    PADDLE_HEIGHT,
)

game_ball = pygame.FRect(
    screen.get_width() / 2,
    screen.get_height() / 2,
    50,
    50
)

speed = pygame.Vector2(300, 300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")


    # move the ball
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
            speed.from_polar((300, -150))
        elif game_ball.centerx < player_zone_2:
            speed.from_polar((300, -130))
        elif game_ball.centerx < player_zone_3:
            speed.from_polar((300, -110))
        elif game_ball.centerx < player_zone_4:
            speed.from_polar((300, -90))
        elif game_ball.centerx < player_zone_5:
            speed.from_polar((300, -70))
        elif game_ball.centerx < player_zone_6:
            speed.from_polar((300, -50))
        else:
            speed.from_polar((300, -30))



    pygame.draw.circle(surface=screen, color='blue',
                       center=game_ball.center, radius=game_ball.width / 2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player.x -= 800 * dt
    if keys[pygame.K_d]:
        player.x += 800 * dt

    player.clamp_ip(player_area)

    pygame.draw.ellipse(screen, "orange", player)




    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000  # limits FPS to 60
pygame.quit()

