class Snake:
    def __init__(self):
        self.length = 1
        self.head_posX = 4
        self.head_posY = 8
        self.move_dir = "none"
        self.body = []
    
    def is_colliding_with_body(self):
        pos = (self.head_posX, self.head_posY)
        for i in body:
            if pos == i:
                return True
        return False
    
    def update(self):
        if self.move_dir == "left":
            self.head_posX -= 1
        elif self.move_dir == "right":
            self.head_posX += 1
        elif self.move_dir == "up":
            self.head_posY -= 1
        elif self.move_dir == "down":
            self.head_posY += 1