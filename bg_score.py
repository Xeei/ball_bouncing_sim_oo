import turtle

class Backgroud_Score:
    def __init__(self, my_turtle: turtle.Turtle, score: int):
        self.score = score
        self.__my_turtle = my_turtle
        self.location = [0,0]
        
    def update_score(self, score: int):
        self.score = score

    def set_location(self, location):
        self.location = location
        self.__my_turtle.goto(self.location[0], self.location[1])

    def draw(self):
        t = self.__my_turtle
        t.color((255,0,0))
        if self.score == 0:
            t.goto(-50, 100)
            t.pendown()
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.forward(100)
            t.right(90)
            t.penup()