from snake import Snake
from food import Food

class Board:
    def __init__(self):
        self.snake_head: chr = "●"
        self.snake_body: chr = "○"
        self.food: chr = "⚬"
        # self.spaces: list[list] = []

    def draw(self, s: Snake, f: Food):
        for i in range(0, 16):
            row = []
            for j in range(0, 16):
                if s.head_posX == j and s.head_posY == i:
                    row.append(self.snake_head)
                # TODO add functionality for drawing the body
                elif f.posX == j and f.posY == i:
                    row.append(self.food)
                else:
                    row.append(" ")
            for j in row:
                print(j, end="")
            print("\n", end="")
        input()