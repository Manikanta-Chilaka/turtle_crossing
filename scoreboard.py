from turtle import Turtle
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-270,270)
        self.write(f"Level {self.level}", font= FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game over",align="center", font = FONT)
    
    def level_up(self):
        self.level +=1
        self.clear()
        self.write(f"Level {self.level}", font= FONT)
