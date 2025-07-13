# Falling Sand Simulation

## Overview
The Falling Sand Simulation is an interactive program that simulates the behavior of falling sand particles. Users can add sand particles to the grid, and the simulation will handle their movement based on simple physics-like rules. The program is built using Python and Pygame.

## Features
- **Interactive Sand Placement**: Click and drag to add sand particles to the grid.
- **Real-Time Simulation**: Watch the sand particles fall and interact with each other in real-time.
- **Colorful Particles**: Each sand particle is assigned a random color for a visually appealing experience.
- **Threaded Simulation**: The sand falling logic runs in a separate thread, ensuring smooth user interaction.

## How It Works
- The grid is represented as a 2D array of `cell` objects.
- Each `cell` can be in an "on" (active) or "off" (inactive) state.
- Sand particles fall downward, and if blocked, they attempt to move diagonally left or right.
- The simulation uses threading to handle the falling logic independently of user input.

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository to your local machine.

## Usage
1. Run the program:
   ```bash
   python main.py
   ```
2. Use your mouse to add sand particles to the grid:
   - **Left Click**: Add sand particles.
3. Watch the particles fall and interact with each other.
4. Close the window to exit the simulation.

## Code Structure
- `main.py`: Contains the entire implementation of the simulation, including the `cell` and `display` classes.
  - **`cell` Class**: Represents individual grid cells and their states.
  - **`display` Class**: Manages the grid, handles user input, and runs the sand falling logic.

## Requirements
- Python 3.x
- Pygame

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

## Acknowledgments
- Inspired by classic falling sand simulations.
- Built using the [Pygame](https://www.pygame.org/) library for Python.
