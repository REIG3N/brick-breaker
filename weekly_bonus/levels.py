import pygame

# Niveau citrouille : 78 briques de 60 x 25, espacement de 4 px,
# grille de 12 colonnes x 13 rangees centree a partir de x = 256, y = 40

BRICK_WIDTH = 60
BRICK_HEIGHT = 25
BRICK_GAP = 4

COLORS = {
    "O": (255, 152, 0),    # orange
    "B": (179, 106, 0),    # orange foncé (ombre)
    "G": (76, 175, 80),    # tige claire
    "D": (56, 125, 56),    # tige foncée
}

PUMPKIN = [
    ".......GD...",
    "......GD....",
    ".....GD.....",
    ".....GD.....",
    "..OOOOOOOO..",
    ".OBBOOOOBBO.",
    "OO..BOOB..OB",
    "OO...BB...OB",
    "OOOOOOOOOOBB",
    "O..O.OO.O..B",
    "OO........BB",
    "OOO......BBB",
    ".OOOBBBBBBB.",
]


def build_level(grid, screen_width, top=40):
    step_x = BRICK_WIDTH + BRICK_GAP
    step_y = BRICK_HEIGHT + BRICK_GAP
    grid_width = len(grid[0]) * step_x - BRICK_GAP
    left = (screen_width - grid_width) // 2

    bricks = []
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char in COLORS:
                rect = pygame.Rect(
                    left + col_index * step_x,
                    top + row_index * step_y,
                    BRICK_WIDTH,
                    BRICK_HEIGHT,
                )
                bricks.append({"rect": rect, "color": COLORS[char]})
    return bricks

bricks = [
    pygame.Rect(704, 40, 60, 25),
    pygame.Rect(768, 40, 60, 25),
    pygame.Rect(640, 69, 60, 25),
    pygame.Rect(704, 69, 60, 25),
    pygame.Rect(576, 98, 60, 25),
    pygame.Rect(640, 98, 60, 25),
    pygame.Rect(576, 127, 60, 25),
    pygame.Rect(640, 127, 60, 25),
    pygame.Rect(384, 156, 60, 25),
    pygame.Rect(448, 156, 60, 25),
    pygame.Rect(512, 156, 60, 25),
    pygame.Rect(576, 156, 60, 25),
    pygame.Rect(640, 156, 60, 25),
    pygame.Rect(704, 156, 60, 25),
    pygame.Rect(768, 156, 60, 25),
    pygame.Rect(832, 156, 60, 25),
    pygame.Rect(320, 185, 60, 25),
    pygame.Rect(384, 185, 60, 25),
    pygame.Rect(448, 185, 60, 25),
    pygame.Rect(512, 185, 60, 25),
    pygame.Rect(576, 185, 60, 25),
    pygame.Rect(640, 185, 60, 25),
    pygame.Rect(704, 185, 60, 25),
    pygame.Rect(768, 185, 60, 25),
    pygame.Rect(832, 185, 60, 25),
    pygame.Rect(896, 185, 60, 25),
    pygame.Rect(256, 214, 60, 25),
    pygame.Rect(320, 214, 60, 25),
    pygame.Rect(512, 214, 60, 25),
    pygame.Rect(576, 214, 60, 25),
    pygame.Rect(640, 214, 60, 25),
    pygame.Rect(704, 214, 60, 25),
    pygame.Rect(896, 214, 60, 25),
    pygame.Rect(960, 214, 60, 25),
    pygame.Rect(256, 243, 60, 25),
    pygame.Rect(320, 243, 60, 25),
    pygame.Rect(576, 243, 60, 25),
    pygame.Rect(640, 243, 60, 25),
    pygame.Rect(896, 243, 60, 25),
    pygame.Rect(960, 243, 60, 25),
    pygame.Rect(256, 272, 60, 25),
    pygame.Rect(320, 272, 60, 25),
    pygame.Rect(384, 272, 60, 25),
    pygame.Rect(448, 272, 60, 25),
    pygame.Rect(512, 272, 60, 25),
    pygame.Rect(576, 272, 60, 25),
    pygame.Rect(640, 272, 60, 25),
    pygame.Rect(704, 272, 60, 25),
    pygame.Rect(768, 272, 60, 25),
    pygame.Rect(832, 272, 60, 25),
    pygame.Rect(896, 272, 60, 25),
    pygame.Rect(960, 272, 60, 25),
    pygame.Rect(256, 301, 60, 25),
    pygame.Rect(448, 301, 60, 25),
    pygame.Rect(576, 301, 60, 25),
    pygame.Rect(640, 301, 60, 25),
    pygame.Rect(768, 301, 60, 25),
    pygame.Rect(960, 301, 60, 25),
    pygame.Rect(256, 330, 60, 25),
    pygame.Rect(320, 330, 60, 25),
    pygame.Rect(896, 330, 60, 25),
    pygame.Rect(960, 330, 60, 25),
    pygame.Rect(256, 359, 60, 25),
    pygame.Rect(320, 359, 60, 25),
    pygame.Rect(384, 359, 60, 25),
    pygame.Rect(832, 359, 60, 25),
    pygame.Rect(896, 359, 60, 25),
    pygame.Rect(960, 359, 60, 25),
    pygame.Rect(320, 388, 60, 25),
    pygame.Rect(384, 388, 60, 25),
    pygame.Rect(448, 388, 60, 25),
    pygame.Rect(512, 388, 60, 25),
    pygame.Rect(576, 388, 60, 25),
    pygame.Rect(640, 388, 60, 25),
    pygame.Rect(704, 388, 60, 25),
    pygame.Rect(768, 388, 60, 25),
    pygame.Rect(832, 388, 60, 25),
    pygame.Rect(896, 388, 60, 25),
]
