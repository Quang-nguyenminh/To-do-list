# import turtle
#
# side = int(input('Input number of sides: '))
# length = int(input('Input length: '))
#
# turtle_screen = turtle.getscreen()
# turtle_actor = turtle.Turtle()
# turtle_actor.color('black')
# turtle_actor.fillcolor('orange')
# turtle_actor.begin_fill()
# for i in range(side):
#     turtle_actor.forward(length)
#     turtle_actor.left(360/side)
# turtle_actor.end_fill()
# turtle.exitonclick()
# -----------------------------------------------------------
num = [1, '2', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']
sum = 0
for i in num:
    if isinstance(i, (int, float)):
        sum += i
print(sum)
