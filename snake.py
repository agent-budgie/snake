from food import Food

class Snake:
    def __init__(self):
        self.length: int = 1
        self.head_posX: int = 4
        self.head_posY: int = 8
        self.move_dir: string = "none"
        self.body: list[tuple] = []
    
    def is_colliding_with_body(self) -> bool:
        for i in body:
            if (self.head_posX, self.head_posY) == i:
                return True
        return False
    
    def is_colliding_with_food(self, f: Food) -> bool:
        return (self.head_posX, self.head_posY) == (f.posX, f.posY)
    
    def update(self):
        if self.move_dir == "left":
            self.head_posX -= 1
        elif self.move_dir == "right":
            self.head_posX += 1
        elif self.move_dir == "up":
            self.head_posY -= 1
        elif self.move_dir == "down":
            self.head_posY += 1