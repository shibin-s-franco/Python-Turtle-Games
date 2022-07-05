from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 13, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        # self.highscore=0
        with open(r"P:\PYTHON\my prog\intermediate level programs\snake game\data.txt",mode='r') as data:
            # data.write("love you")
            self.highscore = int(data.read())
        print(self.highscore)
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.score} High Score:{self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):  
        if self.score > self.highscore: 
            self.highscore=(self.score)
            with open(r"P:\PYTHON\my prog\intermediate level programs\snake game\data.txt",mode="w") as data:
                data.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()
    

    def change_score(self):
        self.score+=1
        self.update_scoreboard()
        
       