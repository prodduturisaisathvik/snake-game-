from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.high_score=0
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"SCORE:{self.score} High Score: {self.high_score}", align="center", font=("arial", 24, "normal"))


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()


    def clean(self):
        self.clear()


    def reset_high_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()

