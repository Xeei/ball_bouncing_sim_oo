import turtle

class Backgroud_Score:
    def __init__(self, my_turtle: turtle.Turtle, score: int):
        self.score = score
        self.__my_turtle = my_turtle
        self.location = [0,-50]
        self.__draw()
        
    def update_score(self, score: int):
        self.score = score
        self.__draw()

    def set_location(self, location):
        self.location = location
        self.__my_turtle.goto(self.location[0], self.location[1])

    def __draw(self):
        t = self.__my_turtle
        t.clear()
        t.penup()
        t.goto(self.location[0], self.location[1])
        t.pendown()
        t.pensize(5)
        t.color((255, 0, 0))
        
        # Look up num shape
        digit_instructions = {
            0: [(0, 100), (50, 0), (0, -100), (-50, 0)],  # 0
            1: [(0, 100)],  # 1
            2: [(-50, 0), (0, 50), (50, 0), (0, 50), (-50, 0)],  # "2" 
            3: 2*[(-50, 0), (50, 0), (0, 50)]+[(-50, 0)],  # "3"
            4: [(0, 100), (0, -50), (-50, 0), (0, 50)],  # "4"
            5: [(-50, 0), (50, 0), (0, 50), (-50, 0), (0, 50), (50, 0)],  # "5"
            6: [(0, 50), (-50, 0), (0, -50), (50, 0), (-50, 0), (0, 100), (50, 0)],  # "6"
            7: [(0, 100), (-50, 0)],  # "7"
            8: 2*[(-50, 0), (50, 0), (0, 50)]+[(-50, 0)]+[(0, -100)],  # "8"
            9: 2*[(-50, 0), (50, 0), (0, 50)]+[(-50, 0)]+[(0, -50)],  # "9"
        }
        
        instructions = digit_instructions.get(self.score, [])
        
        for dx, dy in instructions:
            t.pendown()
            t.goto(t.xcor() + dx, t.ycor() + dy)
        
        t.penup()
        