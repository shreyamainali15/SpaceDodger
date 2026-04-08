# SpaceDodger

## Description
SpaceDodger is a simple, Python game built with Pygame. Control a spaceship to dodge falling meteors and survive as long as possible. The game features increasing difficulty as time progresses, with meteors falling more frequently over time.

## Features
- Smooth spaceship movement using arrow keys
- Randomly generated falling meteors (grey circles)
- Real-time survival timer displayed in the top-left corner
- Game over screen with humorous message and final time
- Restart and quit buttons after collision
- Increasing difficulty: meteors spawn more frequently as time passes
- Colorful spaceship (yellow triangle) on a space background

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies:
   ```
   pip install pygame
   ```

## How to Run
1. Clone or download the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the game:
   ```
   python main.py
   ```

## Controls
- **Left Arrow Key**: Move the spaceship left
- **Right Arrow Key**: Move the spaceship right
- **Mouse Click**: Interact with restart/quit buttons on the game over screen

## Game Mechanics
- The player controls a yellow triangular spaceship at the bottom of the screen.
- Grey circular meteors fall from the top at random horizontal positions.
- The goal is to avoid all meteors and survive as long as possible.
- Each collision with a meteor ends the game.
- The survival time is tracked and displayed during gameplay.
- Upon game over, the final time is shown, and the player can choose to restart or quit.
- Difficulty ramps up: meteors spawn in groups of 3 every 2 seconds initially, with the spawn interval decreasing over time (minimum 200ms).

## Assets
- `background.jpeg`: A space-themed background image used for the game window. Ensure this file is present in the same directory as `main.py`.

## Troubleshooting
- If the game doesn't start, ensure Pygame is installed correctly.
- Make sure `background.jpeg` is in the project directory.
- The game window is set to 1000x800 pixels; ensure your display supports this resolution.

## License
This project is open-source and built for the community!

Feel free to tinker, break things, and put them back together in ways I never imagined. 
I’m beyond excited to see how you’ll take this foundation and push the creative boundaries. Whether it’s a minor tweak or a total overhaul, show me what you’ve got! Go ahead—modify, distribute, and make it yours.
