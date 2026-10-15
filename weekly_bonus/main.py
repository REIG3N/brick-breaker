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


game_ball = pygame.FRect(
    screen.get_width() / 2,
    screen.get_height() / 2,
    50,
    50
)

speed = [300, 300]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")


    # move the ball
    game_ball = game_ball.move(speed[0] * dt, speed[1] * dt)

    # if ball goes out of screen then change direction of movement
    if game_ball.left <= 0 or game_ball.right >= screen.get_width():
        speed[0] = -speed[0]
    if game_ball.top <= 0 or game_ball.bottom >= screen.get_height():
        speed[1] = -speed[1]


    if game_ball.colliderect(player) and speed[1] > 0:
        speed[1] = -speed[1]

    # draw ball at new centers that are obtained after moving ball_obj
    pygame.draw.circle(surface=screen, color='blue',
                       center=game_ball.center, radius=game_ball.width / 2)




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

