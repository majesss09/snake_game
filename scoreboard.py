from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("data.txt", mode="r")
        self.high_score = int(data.read())
        data.close()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}",align="center",font=("Arial",15,"normal"))

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            data = open("data.txt",mode="w")
            data.write(str(self.score))
            data.close()
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

