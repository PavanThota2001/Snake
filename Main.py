from turtle import Screen, Turtle
from snake import snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)


snake = snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True;
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    if snake.segments[0].xcor() < -290 or snake.segments[0].xcor() > 290 or snake.segments[0].ycor() < -290 or snake.segments[0].ycor() > 290:
        game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



screen.exitonclick()
