import turtle
import pandas


def new_state_text():
    """
    Create a new turtle with the name of the state
    :return: name of the state
    """
    state_text = turtle.Turtle()
    state_text.penup()
    state_text.hideturtle()
    return state_text


def engine():
    correct_state = 0
    while correct_state != 50:
        # It takes the name of the input state by capitalizing the first letter
        user_answer = s.textinput(f"{correct_state}/50 States Correct", "What's another state name?").capitalize()

        # Look for the user-supplied status name in the file
        state = data[data.state == user_answer]

        # Exit when user select "cancel"
        if user_answer is None:
            exit(0)

        # Create a new turtle and place the name of the state
        if not state.empty:
            correct_state += 1
            state_text = new_state_text()
            state_text.goto(int(state["x"]), int(state["y"]))
            state_text.write(f"{user_answer}", False, align="center", font=("Courier", 12, "normal"))


data = pandas.read_csv("50_states.csv")

# GUI
s = turtle.Screen()
s.setup(725, 491)
s.title("U.S States Game")
image = "blank_states_img.gif"
s.addshape(image)

t = turtle.Turtle()
t.shape(image)

# Start
engine()

s.mainloop()
