from turtle import Turtle,Screen

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.game_over = Turtle()
        self.game_over.color("red")
        self.game_over.goto(0, 0)
        self.game_over.hideturtle()
        self.game_over.penup()

        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-230,270)
        self.score_value = 0

    def update_score(self):
        self.score_value += 1
        self.score.clear()
        self.score.write(f"Current Score is {self.score_value}", align="center", font=("Arial", 10, "bold"))

    def game_over_status(self):
        self.game_over.write(f"GAME OVER", align="center", font=("Arial", 25, "bold"))
        self.game_over.goto(0, -45)
        self.game_over.write(f"PRESS SPACE TO RESTART", align="center", font=("Arial", 25, "bold"))

    def reset(self):
        self.game_over.clear()
        self.score.clear()

        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(-230,270)
        self.score_value = 0

        self.game_over = Turtle()
        self.game_over.color("red")
        self.game_over.goto(0, 0)
        self.game_over.hideturtle()
        self.game_over.penup()

    def clear_score(self):
        self.score.clear()

