import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

player = Actor('rabbit')
player.pos = (WIDTH // 2, HEIGHT // 2)

carrot = Actor('carrot')
carrot.pos = (300, 300)

fox = Actor('fox')
fox.pos = (100, 100)


def update():
    global score, game_over

    if game_over:
        return

    # Player moves with arrow keys
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Keep rabbit on screen (boundary — can't escape)
    if player.x < 20:
        player.x = 20
    if player.x > WIDTH - 20:
        player.x = WIDTH - 20
    if player.y < 20:
        player.y = 20
    if player.y > HEIGHT - 20:
        player.y = HEIGHT - 20

    # Fox slowly chases the rabbit
    if player.x > fox.x:
        fox.x += 1
    elif player.x < fox.x:
        fox.x -= 1
    if player.y > fox.y:
        fox.y += 1
    elif player.y < fox.y:
        fox.y -= 1

    # Collect the carrot — it respawns somewhere new
    if player.colliderect(carrot):
        score += 1
        carrot.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    # Fox catches rabbit — game over
    if player.colliderect(fox):
        game_over = True


def draw():
    screen.fill((34, 139, 34))

    player.draw()
    carrot.draw()
    fox.draw()

    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 40),
                         fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}",
                         center=(WIDTH // 2, HEIGHT // 2 + 20),
                         fontsize=30, color="white")


pgzrun.go()
