## Coding

Your game goes in `game.py`. Open it, and start building.

---

### 🖼️ Using Your Own Sprites

*Need a custom image? Here's the workflow — or rewatch the video from Lesson 1.*

1. Find an image that's **at least 80×80 pixels**
2. Open **[Squoosh](https://squoosh.app)**, resize to about 80×80, and download *(Squoosh can make images smaller but not larger — start with a big enough image!)*
3. Upload the file to your `images/` folder in Codio
4. Update the `Actor('name')` in your code to match the filename (no `.png`)

---

### Build Order

Don't try to write the whole game at once. Build one piece at a time, test it, then add the next.

A good order for most games:

1. **Player on screen** — create your Actor, draw it, get it moving with keyboard input
2. **Boundaries** — keep the player from leaving the screen
3. **One collectible or obstacle** — add a second Actor and get collision detection working
4. **Score or lives** — use `global` to track something
5. **Game states** — add a start screen and game over screen
6. **More sprites** — scale up with lists if your game needs multiple enemies or collectibles
7. **Polish** — background color, text styling, difficulty tuning

Run `python3 game.py` after every small change. If something breaks, you'll know exactly which change caused it.

---

### Test Your Code

Use this to check your game when you think you're finished. If a test fails, that's ok — you often know more than an automated test. Explain what you think is happening in the next question.

> *[ASSESSMENT NEEDED: Create an llm-based-auto-rubric assessment in the Codio GUI. Rubric items (1 point each): (1) Game has a player Actor that moves with keyboard input, (2) Player stays within screen boundaries, (3) Game includes at least one other Actor the player interacts with, (4) Collision detection works using colliderect(), (5) Game tracks score or lives using a global variable, (6) Game has at least two states (e.g. start and playing, or playing and game over), (7) Game displays text on screen (score, instructions, or game over message), (8) Code runs without errors. Point to .guides/secure/solution/ for solution files.]*

> *[ASSESSMENT NEEDED: Create a free-text-auto assessment in the Codio GUI — question: "How did the autograder score your game? If anything scored lower than you expected, explain what you think is happening in your code and why the test might have missed it."]*
