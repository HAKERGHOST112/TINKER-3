from tkinter import *

root = Tk()
root.title("7 цветов радуги")
root.geometry("325x100")
def update_color_display(color_code, color_name):
    color_entry.delete(0, END)
    color_entry.insert(0, color_code)
    color_label['text'] = color_name

color_entry = Entry(root, width=40, justify=CENTER)
color_entry.pack()

color_label = Label(root, font=("Comic Sans MS", 20))
color_label.pack()

#Выравнивание
f_top=Frame(root)
f_top.pack(ipady=1)

color_palit = [
    ("#ff0000", "Красный"),
    ("#ff7d00", "Оранжевый"),
    ("#ffff00", "Желтый"),
    ("#00ff00", "Зеленый"),
    ("#007dff", "Голубой"),
    ("#0000ff", "Синий"),
    ("#7d00ff", "Фиолетовый"),
]

for color_code, color_title in color_palit:
    Button(root, bg=color_code, width=5, command=lambda c=color_code, n=color_title:
    update_color_display(c, n)).pack(side=LEFT, ipady=2)

root.mainloop()