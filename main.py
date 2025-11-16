import tkinter as tk

# Настройка окна
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap("resources/icon/icon.ico")
root.resizable(0, 0)
# Формирование поля для кнопок
buttons = []
for i in range (9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)











# Запуск главного цикла программы
root.mainloop()