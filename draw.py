import turtle as t
scr = t.Screen()
t1 = t.Turtle()
t1.speed(20)
# def triangle(tcolor='black',size=100):
#     t1.color(tcolor)
#     for i in range(3):
#         t1.forward(size)
#         t1.left(120)
#     t1.color('black')
# for i in range(36):
#     triangle('blue')
#     t1.left(10)

# t1.fillcolor('black')
# t1.begin_fill()
# for i in range(4):
#     t1.forward(100)
#     t1.left(90)
# t1.end_fill()
# t1.penup()
# t1.forward(120)
# t1.pendown()
# t1.begin_fill()
# t1.circle(5)
# t1.end_fill()
# t1.hideturtle()

# t1.color('yellow')
# t1.pensize(2)
# for i in range(6):
#     t1.forward(150)
#     t1.left(18)

# t1.pensize(10)
# for i in range(4):
#     t1.color('indigo')
#     t1.left(70)
#     t1.forward(50)
#     t1.right(140)
#     t1.forward(50)
#     t1.color('thistle')
#     t1.left(140)
#     t1.forward(100)
#     t1.right(140)
#     t1.forward(100)
#     t1.left(70)

# def sqaure(len,rgb):
#     t1.pensize(2)
#     t1.color(rgb)
#     t1.begin_fill()
#     for i in range(4):
#         t1.forward(len)
#         t1.left(90)
#     t1.end_fill()
# sqaure(200,'black')
# sqaure(150,'white')
# sqaure(100,'lavender')
# sqaure(50,'black')



def our_cirlce(color,size):
    t1.color(color)
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
def mark():
    our_cirlce('red',18)
    t1.penup()
    t1.goto(-15,54)
    t1.pendown()
    t1.begin_fill()
    t1.forward(34)
    t1.left(80)
    t1.forward(100)
    t1.left(100)
    t1.forward(64)
    t1.left(96)
    t1.forward(100)
    t1.end_fill()
speed= t.numinput('Ввод скорости','Введите скорость траспорта:', 20, 0, 300)
if speed >= 60 and speed < 80:
    our_cirlce('yellow',50)
elif speed >= 80:
    mark()

else:
    our_cirlce('green',50)
t1.hideturtle()

scr.mainloop()