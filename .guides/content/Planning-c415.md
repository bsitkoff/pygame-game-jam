## Planning

This is your capstone project. You'll design and build a complete game from scratch using everything you've learned in this unit.

There are three tiers — pick the one that fits where you are right now. All three are real games. The difference is scope, not quality.

---

### Choose Your Tier

**🟢 Mild — Catcher Game**
Build a falling-objects catcher. Your player moves left and right along the bottom of the screen. Objects fall from the top. Catch them for points, and track a score.

The only new idea: making things fall is just `y += speed` inside `update()`. Everything else you've already done.

**🟡 Medium — Original Game**
Design and build your own game using the mechanics from this unit: Actors, keyboard input, collision detection, score/lives tracking, and game states (start, playing, game over). Your theme. Your rules. Your design. The catch: you also need at least one mechanic you invent yourself — something we didn't build together in class.

**🔴 Spicy — Realistic Motion**
Build a game that uses **velocity variables** (`dx` and `dy`) for smooth, realistic motion. Instead of moving a fixed amount per keypress, you change the velocity — and the velocity changes the position. This is how real physics works in games: gravity adds to `dy` each frame, bouncing reverses `dx` or `dy`, friction reduces speed over time.

What kind of game you make is up to you — a bouncing ball game, a gravity platformer, a projectile launcher, whatever you want. The unit mechanics still apply; the new piece is figuring out velocity-based movement yourself.

Which tier are you attempting? Why did you choose it?

{Check It!|assessment}(free-text-auto-3339166880)

---

### Design Your Game

Before you write any code, answer these questions:

**Your concept:**
- What's your game about? (one sentence)
- Who or what is the player? What are they trying to do?
- What's working against them? (enemy, timer, gravity, obstacles?)

{Check It!|assessment}(free-text-auto-3574462663)

**Your mechanics:**
- How does the player move?
- What does the player collect, avoid, or interact with?
- What ends the game?
- *(Medium/Spicy)* What's your unique or new mechanic?

{Check It!|assessment}(free-text-auto-967543816)

**Your sprites:**
- List every sprite you need and what image you'll use
- Get your images into the `images/` folder before you start coding

{Check It!|assessment}(free-text-auto-2697697793)


---

### Quick Reference — Where You've Seen This Before

You've already written code for every pattern below. When you get stuck, go back and look at the working code in that lesson.

| Pattern | Where to find it |
|---------|------------------|
| Creating Actors and drawing them | Lesson 1 (`explore.py`) |
| Keyboard input for movement | Lesson 2 (`move.py`) |
| Keeping the player on screen (boundaries) | Lesson 2 (`move.py`) |
| Collision detection with `colliderect()` | Lesson 3 (`collide.py`) |
| Making a sprite chase the player | Lesson 3 (`collide.py`) |
| The `global` keyword for score/state variables | Lesson 4 (`track.py`) |
| Game states: start, playing, game over | Lesson 4 (`track.py`) |
| Displaying text with `screen.draw.text()` | Lesson 4 (`track.py`) |
| Restarting with `on_key_down()` | Lesson 4 (`track.py`) |
| Designing readable UI and consistent screens | Lesson 5 (`interface.py`) |
| Lists of sprites with `for` loops | Lesson 6 (`lists.py`) |
| Collision checking across a list | Lesson 6 (`lists.py`) |
| Making things fall: `actor.y += speed` | New — but it's one line! |
| Velocity with `dx`/`dy` (Spicy only) | New — you figure this one out |

---

|||important
## No AI on this one

This is a "show what you know" project. You can use your notes, your earlier Codio projects, and you can ask Ms. Sitkoff for help — but no AI tools and no copying code from outside sources. You'll have other projects where those tools are fair game, but this one is about demonstrating what *you* can write.
|||
