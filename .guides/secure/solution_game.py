import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Game states
state = "start"
score = 0
lives = 3

# Player
player = Actor('fox')
player.pos = (400, 550)

# Collectible
cookie = Actor('cookie')
cookie.pos = (random.randint(50, 750), random.randint(50, 300))

# Enemy
alien = Actor('alien')
alien.pos = (random.randint(50, 750), random.randint(50, 300))


def update():
    global state, score, lives

    if state == "playing":
        # Keyboard input
        if keyboard.left and player.x > 30:
            player.x -= 5
        if keyboard.right and player.x < WIDTH - 30:
            player.x += 5
        if keyboard.up and player.y > 30:
            player.y -= 5
        if keyboard.down and player.y < HEIGHT - 30:
            player.y += 5

        # Collision with collectible
        if player.colliderect(cookie):
            score += 1
            cookie.pos = (random.randint(50, 750), random.randint(50, 300))

        # Enemy chases player
        if alien.x < player.x:
            alien.x += 2
        if alien.x > player.x:
            alien.x -= 2
        if alien.y < player.y:
            alien.y += 2
        if alien.y > player.y:
            alien.y -= 2

        # Collision with enemy
        if player.colliderect(alien):
            lives -= 1
            alien.pos = (random.randint(50, 750), random.randint(50, 300))
            if lives <= 0:
                state = "gameover"


def draw():
    screen.clear()
    screen.fill((30, 30, 60))

    if state == "start":
        screen.draw.text("Cookie Collector", center=(400, 250), fontsize=60, color="white")
        screen.draw.text("Collect cookies, avoid the alien!", center=(400, 320), fontsize=30, color="yellow")
        screen.draw.text("Press SPACE to start", center=(400, 400), fontsize=24, color="white")

    elif state == "playing":
        player.draw()
        cookie.draw()
        alien.draw()
        screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")
        screen.draw.text(f"Lives: {lives}", topright=(790, 10), fontsize=30, color="red")

    elif state == "gameover":
        screen.draw.text("Game Over!", center=(400, 250), fontsize=60, color="red")
        screen.draw.text(f"Final Score: {score}", center=(400, 320), fontsize=30, color="white")
        screen.draw.text("Press SPACE to play again", center=(400, 400), fontsize=24, color="white")


def on_key_down(key):
    global state, score, lives
    if key == keys.SPACE:
        if state == "start" or state == "gameover":
            state = "playing"
            score = 0
            lives = 3
            player.pos = (400, 550)
            alien.pos = (random.randint(50, 750), random.randint(50, 300))
            cookie.pos = (random.randint(50, 750), random.randint(50, 300))


pgzrun.go()
