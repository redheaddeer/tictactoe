import tkinter as tk
from clicker import *
from buttons import *

current_player = "X"

# Функция для заполнения клеток поля 
def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        if current_player == "X":
            current_player = "O"  
        else:
            current_player = "X"

# Функция для очистки поля
def clean_space():
    for i in range(9):
        buttons[i]["text"] = ""


# Настройка окна
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap("resources/icon/2.ico")
root.resizable(0, 0)

# Формирование поля
buttons = []
for i in range (9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Кнопочки меню
menu = []
clearButton = tk.Button(
    root,
    text="Очистить\nполе",
    font=("Arial", 8),
    width=10,
    height=2,
    command=lambda: clean_space()
)
clearButton.grid(row=3, column=1)
menu.append(clearButton)

# Запуск игрушки
root.mainloop()
