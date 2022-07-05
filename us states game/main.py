import turtle
import pandas
from print_states import PrintStates
screen=turtle.Screen()
print_state=PrintStates()

screen.title("U.S State Game")
image = r"P:\PYTHON\my prog\intermediate level programs\us states game\blank states img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state=[]

data=pandas.read_csv(r"P:\PYTHON\my prog\intermediate level programs\us states game\50_states.csv")
state_list=data.state.to_list()
while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 States Corret",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missed_state=[item for item in state_list if item not in guessed_state]
        print(missed_state)
        # missed_states=pandas.DataFrame(missed_state)
        # missed_states.to_csv("missed_states.csv")
        break
        
    if answer_state in state_list:
        guessed_state.append(answer_state)
        co=data[data.state==answer_state]
        x=co.x.values[0]
        y=co.y.values[0]
        print_state.print_stat(x,y,answer_state)




# turtle.mainloop()