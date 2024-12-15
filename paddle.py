class Paddle:
    def __init__(self, width, height, color, my_turtle):
        self.width = width
        self.height = height
        self.location = [0, 0]
        self.color = color
        self.my_turtle = my_turtle
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.hideturtle()
        self.__is_immune = False

    @property
    def is_immune(self):
        return self.__is_immune

    def set_location(self, location):
        self.location = location
        self.my_turtle.goto(self.location[0], self.location[1])

    def draw(self):
        self.my_turtle.color(self.color)
        self.my_turtle.goto(self.location[0], self.location[1] - self.height/2)
        self.my_turtle.forward(self.width/2)
        self.my_turtle.pendown()
        self.my_turtle.begin_fill()
        for _ in range(2):
            self.my_turtle.left(90)
            self.my_turtle.forward(self.height)
            self.my_turtle.left(90)
            self.my_turtle.forward(self.width)
        self.my_turtle.end_fill()
        self.my_turtle.penup()
        self.my_turtle.goto(self.location[0], self.location[1])

    def active_immune(self):
        self.__is_immune = True
        self.color = (224, 193, 36)

    def deactive_immune(self):
        self.__is_immune = False
        self.color = (255, 0 , 0)

    def clear(self):
        self.my_turtle.clear()

    def __str__(self):
        return "paddle"
