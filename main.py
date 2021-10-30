import time
import tkinter


# Функция определения времени
def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(1000, timing)


# Дефолтные настройки программы
root = tkinter.Tk()
root.title("Dendy's Digital Clock")
root.geometry("400x200")
root.resizable(0, 0)
root.configure(background="black")

# Настройка меню=Выход
menu = tkinter.Menu(root)
new_item = tkinter.Menu(menu, tearoff=0)
new_item.add_command(label='Выход', command=root.destroy)
root.config(menu=menu)
menu.add_cascade(label="Файл", menu=new_item)

# Оформление скина часов

# Показ времени
clock = tkinter.Label(root, font=("arial", 40, "bold"), bg="white")
clock.grid(row=2, column=2, pady=20, padx=60)
timing()

# Название часов
digital = tkinter.Label(root, text="Dendy's Digital Clock", font="arial 14 bold")
digital.grid(row=0, column=2)

# Показ даты
datenow = tkinter.Label(root, text=time.strftime("%d/%m/%Y"), font="arial 14 bold", bg="white")
datenow.grid(row=1, column=2)

# Подпись времени
nota = tkinter.Label(root, text="hours        minutes        seconds", font="arial 14 bold")
nota.grid(row=3, column=2)

root.mainloop()
