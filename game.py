from board import Board
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.s = Snake()
        self.f = Food()
        self.b = Board()
    def run(self):
        self.s.update()
        self.b.draw(self.s, self.f)