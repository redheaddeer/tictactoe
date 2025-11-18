import tkinter as tk

current_player = "X"
buttons = []

# Настройка окна
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap("resources/icon/2.ico")
root.resizable(0, 0) # нам не надо, чтобы у окна была возможность расползаться по экрану

# Функция для заполнения клеток поля 
def on_click(index):
    global current_player
    if buttons[index]["text"] == "": # мы можем изменить значение кнопки только если она пустая
        buttons[index]["text"] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        check_streak()

# Функция для очистки поля
def clear_field():
    for i in range(9):
        buttons[i]["text"] = ""
        buttons[i]["background"] = ("#ffffff")
        buttons[i]["state"]=("normal")
    global current_player
    current_player = "X" # крестики всегда начинают первые, поэтому сбрасываем current_player также до "X"

def check_streak():
    streak_map = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for streak in streak_map:
        a, b, c = streak
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a]["background"] = ("#55ff00") # красим фон в приятный зелёный цвет, приятный же, ну?
            buttons[b]["background"] = ("#55ff00")
            buttons[c]["background"] = ("#55ff00")
            for i in range(9):
                buttons[i]["state"]=("disabled") # и запрещаем дальнейшие изменения игрового поля, ибо game over 

for i in range (9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 16),
        width=5,
        height=2,
        background=("#ffffff"),
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Кнопочки меню
menu = []
clearButton = tk.Button(
    root,
    text="RESET",
    font=("Arial", 8),
    width=10,
    height=2,
    command=lambda: clear_field()
)
clearButton.grid(row=4, column=1)
menu.append(clearButton)

# Запуск игрушки
root.mainloop()
