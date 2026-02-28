# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game in Python.

## Overview

This project provides a terminal-based Rock Paper Scissors game where you can play against the computer. The game features a fully functional game engine with intelligent win/loss detection and clear feedback on every round.

## Features

- **Interactive Gameplay**: Play Rock Paper Scissors directly in your terminal
- **Computer Opponent**: Compete against a computer with random move selection
- **Smart Input Handling**: Case-insensitive input - enter choices in any case (rock, ROCK, Rock, etc.)
- **Clear Feedback**: Detailed messages showing your choice, computer's choice, and game outcome
- **Complete Game Logic**: Fully implemented win/loss/tie detection with descriptive messages

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/Terminal_Based_RockPaperScissors_Game_PY.git
   cd Terminal_Based_RockPaperScissors_Game_PY
   ```

2. Ensure Python 3.x is installed on your system

## Usage

Run the game:

```bash
python RSP.py
```

Follow the on-screen prompts:

- Enter your choice: `rock`, `paper`, or `scissors`
- Input is case-insensitive (ROCK, Rock, rock all work)
- The computer will make its random selection
- The game will display the outcome with a descriptive message

## Game Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- Same choices result in a tie

## How It Works

The game consists of two main functions:

- **`get_choices()`**: Prompts the player for input and generates a random computer choice
- **`check_win()`**: Determines the winner by comparing player and computer choices, then returns a descriptive result message

## Example Gameplay

```
Enter a choice(rock, paper, scissors: )rock
You choose rock, Computer chose scissors
Rock smashes Scissors! You Win!
```

## File Structure

- `RSP.py` - Main game file containing game logic

## Project Structure

```
Terminal_Based_RockPaperScissors_Game_PY/
├── RSP.py
└── README.md
```

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## Future Enhancements

- Add score tracking across multiple rounds
- Replay functionality (play multiple rounds)
- Difficulty levels
- GUI implementation
- Input validation with error handling

## License

This project is open source and available under the MIT License.

## Author

Created as a simple Python learning project.

---

**Have fun playing!** 🎮
