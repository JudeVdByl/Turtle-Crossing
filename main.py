import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True

car = CarManager()
score = Scoreboard()
player = Player(score,car)
car.player = player

def reset():
    global game_is_on
    car.reset()
    player.reset()
    car.difficulty = 10
    game_is_on = True
    car.game_on = True
    score.reset()

screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')
screen.onkeypress(reset, 'space')


def play_game():
    global game_is_on
    car.car_create()
    car.move_all_cars()
    if car.collision():
        score.game_over_status()
        car.game_toggle()
        car.reset()
        score.clear_score()
        player.reset()
        game_is_on = False
        car.game_on = False
        player.player.teleport(-1000,-1000)

    screen.update()
    screen.ontimer(play_game, 50)

play_game()
screen.mainloop()
