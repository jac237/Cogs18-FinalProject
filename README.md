# Cogs 18: Introduction to Python (Spring 2019) Final Project

# Preview

```
my_game = Game2048()
my_game.play()
```
Output
```
Use the following keys:
        
               w (UP)
    a (LEFT)   s (DOWN)   d (RIGHT)

    q - QUIT
        
(0, 3, 2)
(2, 0, 2)
['__2', '__0', '__0', '__2']
['__2', '__0', '__0', '__2']
['__2', '__0', '__0', '__2']
['__2', '__0', '__0', '__2']

Enter Key: d
(0, 0, 2)
['__2', '__0', '__0', '__4']
['__0', '__0', '__0', '__4']
['__0', '__0', '__0', '__4']
['__0', '__0', '__0', '__4']

Enter Key: s
(1, 0, 2)
['__0', '__0', '__0', '__0']
['__2', '__0', '__0', '__0']
['__0', '__0', '__0', '__8']
['__2', '__0', '__0', '__8']

Enter Key: s
(2, 0, 2)
['__0', '__0', '__0', '__0']
['__0', '__0', '__0', '__0']
['__2', '__0', '__0', '__0']
['__4', '__0', '__0', '_16']

Enter Key: d
(2, 1, 2)
['__0', '__0', '__0', '__0']
['__0', '__0', '__0', '__0']
['__0', '__2', '__0', '__2']
['__0', '__0', '__4', '_16']

Enter Key: d
(1, 2, 2)
['__0', '__0', '__0', '__0']
['__0', '__0', '__2', '__0']
['__0', '__0', '__0', '__4']
['__0', '__0', '__4', '_16']

Enter Key: a
(0, 3, 2)
['__0', '__0', '__0', '__2']
['__2', '__0', '__0', '__0']
['__4', '__0', '__0', '__0']
['__4', '_16', '__0', '__0']

```

# Project

The Jupyter Notebook for this project can be found here [ProjectNotebook.ipynb](./ProjectNotebook.ipynb).

## Description

I decided to implement the game 2048 (http://2048game.com/). The object of the game is to reach the 2048 tile by sliding the tiles left, right, up, or down and combining tiles of the same number values (powers of 2's: 2,4,8,..).

Description from Wikepedia(https://en.wikipedia.org/wiki/2048_(video_game)):
> 2048 is played on a gray 4×4 grid, with numbered tiles that slide smoothly when a player moves them using the four arrow keys. Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move. Higher-scoring tiles emit a soft glow.

> A scoreboard on the upper-right keeps track of the user's score. The user's score starts at zero, and is increased whenever two tiles combine, by the value of the new tile. As with many arcade games, the user's best score is shown alongside the current score.

> The game is won when a tile with a value of 2048 appears on the board, hence the name of the game. After reaching the 2048 tile, players can continue to play (beyond the 2048 tile) to reach higher scores. When the player has no legal moves (there are no empty spaces and no adjacent tiles with the same value), the game ends.

> The simple gameplay mechanics (just four directions) allowed it to be used in a promo video for the Myo gesture control armband, the availability of the code underneath allowed it to be used as a teaching aid for programming, and the second-place winner of a coding contest at Matlab Central Exchange was an AI system that would play 2048 on its own.
