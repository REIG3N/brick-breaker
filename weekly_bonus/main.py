import pygame
from levels import PUMPKIN, build_level

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 1000))
bricks = build_level(PUMPKIN, screen.get_width())
clock = pygame.time.Clock()
running = True
dt = 0
font_big = pygame.font.Font(None, 96)
font_small = pygame.font.Font(None, 40)

DOME_WIDTH = 275
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
    35,
    35
)
game_ball.midbottom = player.midtop


brick_length = 20
brick_width = 60

START_BALL_SPEED = 800
MAX_BALL_SPEED = 1400
SPEED_STEP = 5
ball_speed = START_BALL_SPEED


speed = pygame.Vector2(ball_speed, ball_speed)

state = "menu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state != "play":
                # nouvelle partie : tout revient comme au départ
                player.midbottom = (screen.get_width() / 2,
                                    screen.get_height())
                game_ball.midbottom = player.midtop
                speed = pygame.Vector2(ball_speed, ball_speed)
                bricks = build_level(PUMPKIN, screen.get_width())
                state = "play"

    screen.fill("black")

    if state == "menu":
        title = font_big.render("PUMPKIN BREAKER", True, "orange")
        screen.blit(title, title.get_rect(center=(640, 400)))
        text = font_small.render("ESPACE pour jouer", True, "white")
        screen.blit(text, text.get_rect(center=(640, 500)))
        ball_speed = START_BALL_SPEED
    elif state == "game_over" or state == "win":
        if state == "game_over":
            title = font_big.render("GAME OVER", True, "red")
        else:
            title = font_big.render("CITROUILLE VAINCUE", True, "orange")
        screen.blit(title, title.get_rect(center=(640, 400)))
        text = font_small.render("ESPACE pour rejouer", True, "white")
        screen.blit(text, text.get_rect(center=(640, 500)))
        ball_speed = START_BALL_SPEED
    elif state == "play":

        game_ball = game_ball.move(speed[0] * dt, speed[1] * dt)
        if game_ball.left <= 0:
            game_ball.left = 0
            speed[0] = -speed[0]
        if game_ball.right >= screen.get_width():
            game_ball.right = screen.get_width()
            speed[0] = -speed[0]
        if game_ball.top <= 0:
            game_ball.top = 0
            speed[1] = -speed[1]

        if game_ball.colliderect(player) and speed[1] > 0:

            player_zone_1 = player.left + player.width / 7
            player_zone_2 = player_zone_1 + player.width / 7
            player_zone_3 = player_zone_2 + player.width / 7
            player_zone_4 = player_zone_3 + player.width / 7
            player_zone_5 = player_zone_4 + player.width / 7
            player_zone_6 = player_zone_5 + player.width / 7

            if game_ball.centerx < player_zone_1:
                speed.from_polar((ball_speed, -150))
            elif game_ball.centerx < player_zone_2:
                speed.from_polar((ball_speed, -130))
            elif game_ball.centerx < player_zone_3:
                speed.from_polar((ball_speed, -110))
            elif game_ball.centerx < player_zone_4:
                speed.from_polar((ball_speed, -90))
            elif game_ball.centerx < player_zone_5:
                speed.from_polar((ball_speed, -70))
            elif game_ball.centerx < player_zone_6:
                speed.from_polar((ball_speed, -50))
            else:
                speed.from_polar((ball_speed, -30))
            game_ball.bottom = player.top

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 1000 * dt
        if keys[pygame.K_RIGHT]:
            player.x += 1000 * dt

        player.clamp_ip(player_area)

        paddle_shape.centerx = player.centerx
        paddle_shape.centery = screen.get_height()
        pygame.draw.ellipse(screen, "orange", paddle_shape)

        for brick in bricks:
            pygame.draw.rect(screen, brick["color"], brick["rect"])

        pygame.draw.circle(
            surface=screen,
            color='blue',
            center=game_ball.center,
            radius=game_ball.width / 2
        )

        brick_rects = []
        for brick in bricks:
            brick_rects.append(brick["rect"])

        indice = game_ball.collidelist(brick_rects)
        if indice != -1:
            brique_overlap = game_ball.clip(brick_rects[indice])
            if brique_overlap.width > brique_overlap.height:
                speed[1] = -speed[1]
            else:
                speed[0] = -speed[0]
            bricks.pop(indice)
            ball_speed = min(ball_speed + SPEED_STEP, MAX_BALL_SPEED)
            speed.scale_to_length(ball_speed)

        if game_ball.top > screen.get_height():
            state = "game_over"
        if len(bricks) == 0:
            state = "win"

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000  # limits FPS to 60
pygame.quit()
