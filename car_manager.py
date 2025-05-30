import random
from turtle import Turtle,Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self,player=None):
        self.screen = Screen()
        self.game_on = True
        self.difficulty = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.move_increment = MOVE_INCREMENT

        self.player = player

    def car_create(self):
        if self.game_on and len(self.car_list) <= 10:
            car = Turtle()
            car.setheading(180)
            car.shape('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.color(random.choice(COLORS))
            car.goto(random.randint(330, 1000), random.randint(-250, 250))
            self.car_list.append(car)
        elif len(self.car_list) > 10:
            self.traffic()


    def traffic(self):
        for car in self.car_list:
            if car.xcor() < -350:
                self.car_list.remove(car)

    def move_all_cars(self):
        if self.game_on:
            for car in self.car_list:
                car.forward(self.difficulty)

    def reset(self):
        for car in self.car_list:
            car.hideturtle()
            car.clear()
        self.car_list.clear()

    def collision(self):
        for car in self.car_list:
            if self.player.player.distance(car) <20:
                return True
        return False

    def game_toggle(self):
        self.game_on = False
