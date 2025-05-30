from turtle import Turtle, Screen
from scoreboard import Scoreboard
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self, score, car):
        self.screen = Screen()
        self.player = Turtle()
        self.score = score
        self.car = car

        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup()
        self.player.teleport(STARTING_POSITION[0],STARTING_POSITION[1])
        self.player.setheading(90)

    def move_up(self):
        self.player.forward(MOVE_DISTANCE)
        if self.player.ycor() >= FINISH_LINE_Y:
            self.score.update_score()
            self.reset()
            self.car.reset()
            self.car.difficulty += self.car.move_increment

    def move_down(self):
        self.player.backward(MOVE_DISTANCE)
        if self.player.ycor() <= -281:
            self.player.teleport(STARTING_POSITION[0],STARTING_POSITION[1])

    def reset(self):
        self.player.teleport(STARTING_POSITION[0], STARTING_POSITION[1])







