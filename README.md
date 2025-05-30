# Turtle Crossing Game

A minimalist Frogger style arcade game built with Python's turtle graphics module. Guide the turtle to the finish line while avoiding a stream of oncoming cars. Each successful crossing increases the game's speed and your score.

## Requirements

* Python 3.8 or later
* Standard `turtle` module (bundled with CPython)
  
## Demo
![turtlecrossing-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/4ea37062-b3c1-4e67-8b3a-40fe55a0cadf)


## Setup

```bash
git clone <repository-url>
cd <repository-folder>
python main.py
```

No extra packages are needed.

## Controls

* **Up arrow**: move forward
* **Down arrow**: move backward
* **Space**: restart after a collision

## Gameplay

* Cars spawn from the right edge and drive left at a constant speed.
* Reaching the top edge increments your score and speeds up traffic.
* Colliding with a car ends the round and shows a **GAME OVER** message.
* Press **Space** to reset the board and start a new round.

## File overview

| File             | Purpose                                                    |
| ---------------- | ---------------------------------------------------------- |
| `main.py`        | Initializes the window, binds keys, and runs the game loop |
| `car_manager.py` | Spawns, moves, and manages car sprites                     |
| `player.py`      | Handles turtle movement and finish-line checks             |
| `scoreboard.py`  | Renders the score and game-over messages                   |

## License

Released under the MIT License.
