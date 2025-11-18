import tkinter as tk

current_player = "X"

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
def clean_space():
    for i in range(9):
        buttons[i]["text"] = ""
        buttons[i]["background"] = ("#ffffff")
        buttons[i]["state"]=("normal")
    global current_player
    current_player = "X" # крестики всегда начинают первые, поэтому сбрасываем current_player также до "X"

def check_streak():
    streak = False # сначала мы не знаем, есть ли стрики на карте 
    if (buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"]
        and buttons[0]["text"] != ""): # если хотя бы одно поле не пустое, и при этом поля равны, значит они все равны X или O
        streak = True
        buttons[0]["background"] = ("#55ff00") # красим фон в приятный зелёный цвет, приятный же, ну?
        buttons[1]["background"] = ("#55ff00")
        buttons[2]["background"] = ("#55ff00")
    else:
        if (buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"]
            and buttons[3]["text"] != ""):
            streak = True
            buttons[3]["background"] = ("#55ff00")
            buttons[4]["background"] = ("#55ff00")
            buttons[5]["background"] = ("#55ff00")
        else:
            if (buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"]
                and buttons[6]["text"] != ""):
                streak = True
                buttons[6]["background"] = ("#55ff00")
                buttons[7]["background"] = ("#55ff00")
                buttons[8]["background"] = ("#55ff00")
            else:
                if (buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"]
                    and buttons[0]["text"] != ""):
                    streak = True
                    buttons[0]["background"] = ("#55ff00")
                    buttons[3]["background"] = ("#55ff00")
                    buttons[6]["background"] = ("#55ff00")
                else:
                    if (buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"]
                        and buttons[1]["text"] != ""):
                        streak = True
                        buttons[1]["background"] = ("#55ff00")
                        buttons[4]["background"] = ("#55ff00")
                        buttons[7]["background"] = ("#55ff00")
                    else:
                        if (buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"]
                            and buttons[2]["text"] != ""):
                            streak = True
                            buttons[2]["background"] = ("#55ff00")
                            buttons[5]["background"] = ("#55ff00")
                            buttons[8]["background"] = ("#55ff00")
                        else:
                            if (buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"]
                                and buttons[0]["text"] != ""):
                                streak = True
                                buttons[0]["background"] = ("#55ff00")
                                buttons[4]["background"] = ("#55ff00")
                                buttons[8]["background"] = ("#55ff00")
                            else:
                                if (buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"]
                                    and buttons[2]["text"] != ""):
                                    streak = True
                                    buttons[2]["background"] = ("#55ff00")
                                    buttons[4]["background"] = ("#55ff00")
                                    buttons[6]["background"] = ("#55ff00")
    if streak:
        for i in range(9):
            buttons[i]["state"]=("disabled") # и запрещаем дальнейшие изменения игрового поля, ибо game over 

# Формирование поля
buttons = []
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
