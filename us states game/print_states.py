import turtle

class PrintStates(turtle.Turtle):
    def __init__(self):
        super().__init__()
        pass
      

    def print_stat(self,x,y,state):
            x_co=x
            y_co=y
            # turtle=turtle.Turtle()
            self.penup()
            self.hideturtle()
            self.goto(x_co,y_co)
            self.write(state, move=False,  font=("Arial", 8, 'normal'))