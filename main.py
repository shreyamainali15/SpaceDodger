import pygame
import time
import random
pygame.font.init()

pygame.display.set_caption("Space Dodge")


def create_spaceship_surface(width, height):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    color = (0, 255, 0)  # Green
    # Draw triangle spaceship
    points = [(width//2, 0), (0, height), (width, height)]
    pygame.draw.polygon(surface, 'yellow', points)
    return surface


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.transform.scale(
    pygame.image.load("background.jpeg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("arial", 20)
LOST_FONT = pygame.font.SysFont("comicsans", 60)
BUTTON_FONT = pygame.font.SysFont("comicsans", 30)

# Player dimensions
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 6
PLAYER_IMG = create_spaceship_surface(PLAYER_WIDTH, PLAYER_HEIGHT)

# Meteor dimensions
METEOR_WIDTH = 20
METEOR_HEIGHT = 20
METEOR_VELOCITY = 8

# Button dimensions
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
RESTART_BUTTON = pygame.Rect(
    WIDTH // 2 - 170, HEIGHT // 2 + 100, BUTTON_WIDTH, BUTTON_HEIGHT)
QUIT_BUTTON = pygame.Rect(WIDTH // 2 + 20, HEIGHT //
                          2 + 100, BUTTON_WIDTH, BUTTON_HEIGHT)


def draw(player, end_time, meteors):
    WINDOW.blit(BACKGROUND, (0, 0))

    time_text = FONT.render(f"Time: {round(end_time)}secs", 1, "white")

    WINDOW.blit(time_text, (10, 10))

    WINDOW.blit(PLAYER_IMG, (player.x, player.y))

    for meteor in meteors:
        pygame.draw.circle(WINDOW, "grey", (meteor.centerx,
                           meteor.centery), meteor.width // 2)

    pygame.display.update()


def draw_game_over(end_time):
    WINDOW.blit(BACKGROUND, (0, 0))

    fun_msg = FONT.render("WHAT A PIECE OF SHIT!", True, "white")
    lost_msg = LOST_FONT.render("YOU LOST!", True, "white")
    time_msg = FONT.render(f"Final Time: {round(end_time)}secs", True, "white")

    WINDOW.blit(
        fun_msg, (WIDTH // 2 - fun_msg.get_width() // 2, HEIGHT // 2 - 150))
    WINDOW.blit(
        lost_msg, (WIDTH // 2 - lost_msg.get_width() // 2, HEIGHT // 2 - 40))
    WINDOW.blit(
        time_msg, (WIDTH // 2 - time_msg.get_width() // 2, HEIGHT // 2 + 50))

    # Draw restart button
    pygame.draw.rect(WINDOW, "green", RESTART_BUTTON, border_radius=15)
    restart_text = BUTTON_FONT.render("Restart", True, "white")
    restart_text_rect = restart_text.get_rect(center=RESTART_BUTTON.center)
    WINDOW.blit(restart_text, restart_text_rect)

    # Draw quit button
    pygame.draw.rect(WINDOW, "red", QUIT_BUTTON, border_radius=15)
    quit_text = BUTTON_FONT.render("Quit", True, "white")
    quit_text_rect = quit_text.get_rect(center=QUIT_BUTTON.center)
    WINDOW.blit(quit_text, quit_text_rect)

    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    end_time = 0

    meteor_add_increment = 2000
    meteor_count = 0
    meteors = []
    hit = False

    while run:
        meteor_count += clock.tick(60)
        end_time = time.time() - start_time

        if meteor_count > meteor_add_increment:
            for _ in range(3):
                meteor_x = random.randint(0, WIDTH - METEOR_WIDTH)
                meteor = pygame.Rect(
                    meteor_x, -METEOR_HEIGHT, METEOR_WIDTH, METEOR_HEIGHT)
                meteors.append(meteor)

            meteor_add_increment = max(200, meteor_add_increment - 50)
            meteor_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for meteor in meteors[:]:
            meteor.y += METEOR_VELOCITY
            if meteor.y > HEIGHT:
                meteors.remove(meteor)
            elif meteor.y + meteor.height >= player.y and meteor.colliderect(player):
                meteors.remove(meteor)
                hit = True
                break

        if hit:
            game_over = True
            final_time = end_time

            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = False
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if RESTART_BUTTON.collidepoint(mouse_x, mouse_y):
                            # Reset game
                            player.x = 200
                            player.y = HEIGHT - PLAYER_HEIGHT
                            meteors = []
                            meteor_count = 0
                            meteor_add_increment = 2000
                            start_time = time.time()
                            hit = False
                            game_over = False
                        elif QUIT_BUTTON.collidepoint(mouse_x, mouse_y):
                            game_over = False
                            run = False

                draw_game_over(final_time)

        draw(player, end_time, meteors)

    pygame.quit()


if __name__ == "__main__":
    main()
