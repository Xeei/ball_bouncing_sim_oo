
# Ball bouncing game 10-?

This project is all about ball and paddle that user need use control paddle left and right to hit the `Green Ball` that gonna `give 1` score and in the same time user need to aviod `Red Ball` that gonna `minus 1` score if score reach 10 score that game will end.




## Installation

clone repository
```bash
git clone https://github.com/Xeei/ball_bouncing_sim_oo.git
```

start game
```bash
python run_ball.py
```

    
## Usage/Examples

Interaction
| Key | effect | type |
| :--: | - | :- |
| ⬅️ | paddle move left | press |
| ➡️ | paddle move right | press |
| ␣ | active paddle immune | hold |

## Project design and implementation

### UML Diagram
```mermaid
classDiagram
    class Ball {
        + size: int
        + x: int
        + y: int
        + vx: float
        + vy: float
        + color: tuple
        + mass: float
        + count: int
        + id: int
        + canvas_width: int
        + canvas_height: int

        + draw() 
        + bounce_off_vertical_wall()
        + bounce_off_horizontal_wall()
        + bounce_off()
        + distance()
        + move()
        + time_to_hit()
        + time_to_hit_vertical_wall()
        + time_to_hit_horizontal_wall()
        + time_to_hit_paddle_vertical()
        + time_to_hit_paddle_horizontal()
        + bounce_off_paddle_vertical()
        + bounce_off_paddle_horizontal()
    }

    class Good_ball {
        - __score: int
        + score: int
    }

    class Bad_ball {
        - __score: int
        + score: int
    }

    class Paddle {
        + width: int
        + height: int
        + location: list
        + color: tuple
        + my_turtle: Turtle
        - __is_immune: bool
        + is_immune: bool

        + set_location()
        + draw()
        + active_immune()
        + deactive_immune()
        + clear()
    }

    class Backgroud_Score {
        + score: int
        - ___my_turtle: Turtle
        + location: list

        + update_score()
        + set_location()
        - __draw()
    }

    class Event {
        + time
        + a: Ball
        + b: Ball
        + paddle: Paddle

        + is_valid()
    }

    class BouncingSimulator {
        + num_balls: int
        + ball_list: List~Ball~
        + t: float
        + pq: list
        + HZ: int
        + canvas_width: int
        + canvas_height: int
        + score: int
        + my_paddle: Paddle
        + bg_score: Backgroud_Score

        - __predict()
        - __draw_border()
        - __redraw()
        - __paddle_predict()
        + move_left()
        + move_right()
        + run()
    }

    Ball "1" <|-- "1" Good_ball
    Ball "1" <|-- "1" Bad_ball
    BouncingSimulator "1" *-- "1" Event
    BouncingSimulator "1" *-- "1"Paddle
    BouncingSimulator "1" *-- "1" Backgroud_Score
    BouncingSimulator "1" -- "0..n" Good_ball
    BouncingSimulator "1" -- "0..n" Bad_ball
```

### Modify
- Make paddle can bouce with ball in horizontal way
- Create immune mode by hold space bar
### Extend
- Make Background score to render score that user get while playing
### Test
- test by simulation and see that the ball can hit the ball accuracy
- Test that score system are collect score correctly
### Bug
- There are some bug that when paddle move that ball bounce off before hit paddle sometime but it really small
## Rating
i give myself `80/100` because i only fix paddle to can hit in horizontal way and make it can immute and make score background.
