import turtle as t
import random
import colorgram

t.colormode(255)
screen = t.Screen()
screen.title("Hirst Dot Painting")

tim = t.Turtle()
tim.speed(0)

colors = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171),
          (234, 226, 204), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120),
          (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194),
          (183, 192, 201), (214, 177, 191)]

tim.hideturtle()
tim.penup()
position = -200

while position < 251:
    tim.penup()
    tim.setx(-230)
    tim.sety(position)
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    position += 50


# Colorgram
# colors = colorgram.extract("day_18_image.jpg", 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)



# SPIROGRAPH
# def set_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b
#
# angles = [0, 90, 180, 270]

# def draw_spirograph(gap_size):
#     for _ in range(int(360 / gap_size)):
#         tim.color(set_color())
#         tim.circle(radius=100)
#         tim.setheading(tim.heading() + gap_size)
#
#
# draw_spirograph(8)

# RANDOM WALK
# for _ in range(300):
#     tim.forward(30)
#     tim.color(set_color())
#     tim.setheading(random.choice(angles)


# DRAW SHAPES
# tim.penup()
# tim.setx(-50)
# tim.sety(50)
# tim.pendown()
# sides = 3
#
# while sides < 30:
#     angle = 360 / sides
#     tim.color(set_color())
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1


screen.exitonclick()
