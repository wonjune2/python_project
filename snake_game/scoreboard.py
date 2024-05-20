from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"score: {self.score}", False, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", False, align="center")
