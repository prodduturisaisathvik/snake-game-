from tokenize import group
from turtle import Screen,Turtle



game_on=True

class Snake:

    def __init__(self):
        self.group=[]
        self.x =0
        self.y=0
        self.direction()





    def box(self):
        for turtle in range(0,3):
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.goto(x=0, y=self.y)
            tim.color("white")
            self.group.append(tim)
            self.y = self.y + 20
        self.group[0].left(90)


    def move(self):
        for turtle in range(len(self.group) - 1, 0, -1):
            new_x = self.group[turtle - 1].xcor()
            new_y = self.group[turtle - 1].ycor()
            self.group[turtle].goto(new_x, new_y)
        self.group[0].forward(10)

    def direction(self):
        def up():
            if self.group[0].heading()!=270:
                self.group[0].setheading(90)
            else:
                self.move()
        def right():
            if self.group[0].heading() != 180:
                self.group[0].setheading(0)
            else:
                self.move()

        def left():
            if self.group[0].heading() != 0:
                self.group[0].setheading(180)
            else:
                self.move()
        def down():
            if self.group[0].heading()!= 90:
                self.group[0].setheading(270)
            else:
                self.move()
        screen=Screen()
        screen.onkey(up, "w")
        screen.onkey(right, "d")
        screen.onkey(left, "a")
        screen.onkey(down, "s")
        screen.listen()


    def boundary(self):
        self.group[0].setworldcoordinates(-300,-300,300,300)

    def body_grow(self):
        top=Turtle()
        top.penup()
        top.shape("square")
        top.color("white")
        x2=self.group[len(self.group)-1].xcor()
        y2=self.group[len(self.group)-1].ycor()
        top.goto(x2,y2)
        self.group.append(top)


    def reset(self):
        for parts in self.group:
            parts.hideturtle()
        self.group.clear()
        self.box()
        self.x = 0
        self.y = 0
        self.direction()



