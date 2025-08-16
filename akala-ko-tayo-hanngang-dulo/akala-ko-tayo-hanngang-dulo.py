import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("arai kouh")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player_width, player_height = 80, 15
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

block_width, block_height = 30, 30
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_speed = 12
speed_increase_rate = 0.5

score = 0
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

lyrics_lines = [
    ("akala ko tayo hanggang dulo", 0.09),
    ("ba't ngayon nagiisa ako?", 0.09),
    ("oh diba wala akong natutunan", 0.1),
    ("ang hirap mo paring kalimutan", 0.1)
]
delays = [1.6, 1.5, 1.5, 2]

running = True
game_over = False
clock = pygame.time.Clock()
start_time = time.time()

typing = False
current_line = ""
line_index = 0
char_index = 0
char_delay = 0
last_char_time = 0
line_start_time = 0
waiting_after_line = False

def start_lyrics():
    global typing, line_index, char_index, current_line, char_delay, last_char_time, waiting_after_line
    typing = True
    line_index = 0
    char_index = 0
    current_line = ""
    char_delay = lyrics_lines[line_index][1]
    last_char_time = time.time()
    waiting_after_line = False

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        elapsed_time = time.time() - start_time
        block_speed = 12 + elapsed_time * speed_increase_rate

        block_y += block_speed

        if (player_x < block_x + block_width and
            player_x + player_width > block_x and
            player_y < block_y + block_height and
            player_y + player_height > block_y):
            game_over = True
            start_lyrics()

        if block_y > HEIGHT:
            score += 1
            block_x = random.randint(0, WIDTH - block_width)
            block_y = -block_height

        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, RED, (block_x, block_y, block_width, block_height))
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    else:
        game_over_text = game_over_font.render("RELAPSE TIME", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))

        if typing:
            current_time = time.time()
            if not waiting_after_line:
                if current_time - last_char_time >= char_delay:
                    if char_index < len(lyrics_lines[line_index][0]):
                        current_line += lyrics_lines[line_index][0][char_index]
                        char_index += 1
                        last_char_time = current_time
                    else:
                        waiting_after_line = True
                        line_start_time = current_time
            else:
                if current_time - line_start_time >= delays[line_index]:
                    line_index += 1
                    if line_index < len(lyrics_lines):
                        current_line = ""
                        char_index = 0
                        char_delay = lyrics_lines[line_index][1]
                        waiting_after_line = False
                        last_char_time = current_time
                    else:
                        typing = False

            lyric_text = font.render(current_line, True, BLACK)
            screen.blit(lyric_text, (WIDTH//2 - lyric_text.get_width()//2, HEIGHT//2))

    pygame.display.flip()

pygame.quit()
