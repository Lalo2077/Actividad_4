"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.
"""

from turtle import clear
from turtle import right
from turtle import forward
from turtle import dot
from turtle import back
from turtle import update
from turtle import ontimer
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import width
from turtle import onkey
from turtle import listen
from turtle import done
from turtle import onscreenclick

state = {'turn': 0}


def spinner():
    """Draw fidget spinner."""
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'yellow')
    back(100)
    right(120)
    forward(100)
    dot(120, 'purple')
    back(100)
    right(120)
    forward(100)
    dot(120, 'grey')
    back(100)
    right(120)
    update()


def animate():
    """Animate fidget spinner."""
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)


def flick():
    """Flick fidget spinner."""
    state['turn'] += 10

def flickClick(x,y):
    "Flicks fidget spinner with left click"
    state['turn'] += 10


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
onscreenclick(flickClick, btn=1)
listen()
animate()
done()
