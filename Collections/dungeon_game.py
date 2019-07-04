import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win or loss
# clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def get_locations():
    monster = None
    door = None
    player = None

    return monster, door, player


def move_player(player, move):
  # get players location
  # if move == LEFT, x-1
  # if move == RIGHT, x+1
  # if move == UP, y-1
  # if move == DOWN, y+1
  return player


def get_moves(player):
  moves = ["LEFT", "RIGHT", "UP", "DOWN"]
  # if player's y == 0, they can't move up
  # if player's y == 4, they can't move down
  # if player's x == 0, they can't move left
  # if player's x == 4, they can't move right
  return moves

downwhile True:
  print("Welcome to the Dungeon!")
  print("You're currently in room {}") #fill with player position
  print("You can move {}")  #fill with available moves
  print("Enter QUIT to quit")

  move = input("> ")
  move = move.upper()

  if move == 'QUIT':
    break

  # good move? Change player position
  # bad move? Don't change anything
  # on the door? They win!
  # on the monster? They lose!
  # otherwise loop back around
