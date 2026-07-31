from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
snake.box()
food=Food()
score = Scoreboard()


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food.
    if snake.group[0].distance(food)<15:
        food.refresh()
        score.clean()
        score.increase_score()
        snake.body_grow()

    #detect collision with wall.
    if snake.group[0].xcor()>280 or snake.group[0].xcor()<-280 or snake.group[0].ycor()>280 or snake.group[0].ycor()<-280:
        score.update_scoreboard()
        score.reset_high_score()
        snake.reset()


    #detect collision.
    for blocks in range(4,len(snake.group),1):
        if snake.group[0].distance(snake.group[blocks])<15:
            score.update_scoreboard()
            score.reset_high_score()
            snake.reset()









screen.exitonclick()