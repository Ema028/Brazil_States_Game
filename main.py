from unicodedata import normalize
import turtle
import pandas

screen = turtle.Screen()
screen.title("Estados do Brasil")

img = "mapa_brasil.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("estados.csv")

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

guessed_states = []

while len(guessed_states) < 26:
    answer = screen.textinput(title = f"{len(guessed_states)}/26 Estados Corretos",
                              prompt = "Qual o nome de outro estado?").title()
    ascii_answer = normalize('NFKD', answer).encode('ASCII', 'ignore').decode('ASCII')

    if answer == 'Sair':
        missing_states = []
        for state in data.state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states).to_csv("estados_faltando.csv")
        break
    for state in data.state:
        ascii_state = normalize('NFKD', state).encode('ASCII', 'ignore').decode('ASCII')
        if ascii_answer == ascii_state:
            guessed_states.append(state)
            data_row = data[data.state == state]
            turtle.goto(data_row.x.item(), data_row.y.item())
            turtle.write(state)
