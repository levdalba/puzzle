from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        self.t = Turtle()
        self.tiles = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
        self.t.hideturtle()
        self.t.penup()

    def draw_tiles(self):
        self.t.goto(-100, 100)
        for i in range(4):
            for j in range(4):
                self.t.write(
                    self.tiles[i][j], align="center", font=("Arial", 20, "normal")
                )
                self.t.forward(50)
            self.t.backward(200)
            self.t.sety(self.t.ycor() - 50)
