import ball
import my_event
import turtle
import random
import heapq
import paddle
from bg_score import Backgroud_Score
import datetime

class BouncingSimulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.t = 0.0
        self.pq = []
        self.HZ = 4
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.score = 0
        print(self.canvas_width, self.canvas_height)

        ball_radius = 0.05 * self.canvas_width
        bad_ball_radius = 0.025 * self.canvas_width
        for i in range(self.num_balls//2):
            x = -self.canvas_width + (i+1)*(2*self.canvas_width/(self.num_balls+1))
            y = 0.0
            vx = 10*random.uniform(-1.0, 1.0)
            vy = 10*random.uniform(-1.0, 1.0)
            ball_color = (61, 232, 58)
            self.ball_list.append(ball.Good_ball(ball_radius, x, y, vx, vy, ball_color, i))

        for i in range(self.num_balls//3):
            x = -self.canvas_width + (i+1)*(2*self.canvas_width/(self.num_balls+1))
            y = 0.0
            vx = 5*random.uniform(-1.0, 1.0)
            vy = 5*random.uniform(-1.0, 1.0)
            ball_color = (235, 64, 52)
            self.ball_list.append(ball.Bad_ball(bad_ball_radius, x, y, vx, vy, ball_color, i))

        

        tom = turtle.Turtle()
        self.my_paddle = paddle.Paddle(200, 50, (255, 0, 0), tom)
        self.my_paddle.set_location([0, -50])

        jerry = turtle.Turtle()
        self.bg_score = Backgroud_Score(jerry, self.score)
        self.bg_score.set_location([0, 50])
        self.screen = turtle.Screen()

    # updates priority queue with all new events for a_ball
    def __predict(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.ball_list)):
            dt = a_ball.time_to_hit(self.ball_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, my_event.Event(self.t + dt, a_ball, self.ball_list[i], None))
        
        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, my_event.Event(self.t + dtX, a_ball, None, None))
        heapq.heappush(self.pq, my_event.Event(self.t + dtY, None, a_ball, None))
    
    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))   
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def __redraw(self):
        turtle.clear()
        self.my_paddle.clear()
        self.__draw_border()
        self.my_paddle.draw()
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw()
        turtle.update()
        heapq.heappush(self.pq, my_event.Event(self.t + 1.0/self.HZ, None, None, None))

    def __paddle_predict(self):

        for i in range(len(self.ball_list)):
            a_ball = self.ball_list[i]
            dtPV = a_ball.time_to_hit_paddle_vertical(self.my_paddle)
            dtPH = a_ball.time_to_hit_paddle_horizontal(self.my_paddle)
            heapq.heappush(self.pq, my_event.Event(self.t + dtPV, a_ball, None, self.my_paddle))
            heapq.heappush(self.pq, my_event.Event(self.t + dtPH, None, a_ball, self.my_paddle))

    # move_left and move_right handlers update paddle positions
    def move_left(self):
        if (self.my_paddle.location[0] - self.my_paddle.width/2 - 40) >= -self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] - 40, self.my_paddle.location[1]])

    # move_left and move_right handlers update paddle positions
    def move_right(self):
        if (self.my_paddle.location[0] + self.my_paddle.width/2 + 40) <= self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] + 40, self.my_paddle.location[1]])

    # def move_up(self):
    #     if (self.my_paddle.location[1] + self.my_paddle.height/2 + 40) <= self.canvas_height:
    #         self.my_paddle.set_location([self.my_paddle.location[0], self.my_paddle.location[1] + 40])

    # def move_down(self):
    #     if (self.my_paddle.location[1] - self.my_paddle.height/2 - 40) >= -self.canvas_height:
    #         self.my_paddle.set_location([self.my_paddle.location[0], self.my_paddle.location[1] - 40])

    def run(self):
        # initialize pq with collision events and redraw event
        for i in range(len(self.ball_list)):
            self.__predict(self.ball_list[i])
        heapq.heappush(self.pq, my_event.Event(0, None, None, None))

        # listen to keyboard events and activate move_left and move_right handlers accordingly
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkeypress(self.my_paddle.active_immune, "space")
        self.screen.onkeyrelease(self.my_paddle.deactive_immune, "space")
        # self.screen.onkey(self.move_up, "Up")
        # self.screen.onkey(self.move_down, "Down")
        while (True):
            e = heapq.heappop(self.pq)
            if not e.is_valid():
                continue

            ball_a = e.a
            ball_b = e.b
            paddle_a = e.paddle

            # update positions, and then simulation clock
            for i in range(len(self.ball_list)):
                self.ball_list[i].move(e.time - self.t)
            self.t = e.time

            if (ball_a is not None) and (ball_b is not None) and (paddle_a is None):
                ball_a.bounce_off(ball_b)
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is None):
                ball_a.bounce_off_vertical_wall()
            elif (ball_a is None) and (ball_b is not None) and (paddle_a is None):
                ball_b.bounce_off_horizontal_wall()
            elif (ball_a is None) and (ball_b is None) and (paddle_a is None):
                self.__redraw()
            elif (paddle_a is not None):
                if self.score == 10:
                    break
                if ball_a is not None and ball_b is None:
                    ball_a.bounce_off_paddle_vertical()
                elif ball_a is None and ball_b is not None:
                    ball_b.bounce_off_paddle_horizontal()
                if not self.my_paddle.is_immune:
                    if isinstance(ball_a, ball.Good_ball):
                        self.score += ball_a.score
                        self.bg_score.update_score(self.score)
                    elif isinstance(ball_a, ball.Bad_ball):
                        if self.score - 1 >= 0:
                            self.score += ball_a.score
                            self.bg_score.update_score(self.score)

            self.__predict(ball_a)
            self.__predict(ball_b)

            # regularly update the prediction for the paddle as its position may always be changing due to keyboard events
            self.__paddle_predict()
        turtle.clear()
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()

# num_balls = int(input("Number of balls to simulate: "))
num_balls = 10
my_simulator = BouncingSimulator(num_balls)
my_simulator.run()
