from turtle import Turtle, Screen
import random
from board import Board
import time


board = Board()

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("white")
screen.title("puzzle")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    board.draw_tiles()
screen.exitonclick()
