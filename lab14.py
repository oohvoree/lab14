from tkinter import *
from random import *
from tkinter import messagebox

a = []
b = []

def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    n = int(n)

    a.clear()
    b.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    listbox3.delete(0, END)

    for i in range(n):
        a.append(randint(-50, 50))
        b.append(randint(-50, 50))
        listbox1.insert(END, a[i])
        listbox3.insert(END, b[i])

def sort():
    n = len(a)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if a[i] < a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])

def sort_selection():
    n = len(a)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])
        
def compute_sum():
    s = sum(a)
    label4['text'] = 'sum = ' + str(s)

def scalar_product():
    if len(a) != len(b):
        messagebox.showerror('Помилка', 'Вектори мають різну довжину')
        return
    product = sum(a[i] * b[i] for i in range(len(a)))
    messagebox.showinfo('Скалярний добуток', f'Скалярний добуток = {product}')
    
def about_author():
    messagebox.showinfo('Про автора', 'Автор: Пучкова Валерія\nEmail: valery290907@gmail.com')

def problem_statement():
    messagebox.showinfo('Умова задачі', 'Згенерувати два вектори, відсортувати, обчислити скалярний добуток')

def set_light_theme():
    root['bg'] = 'lightgray'
    listbox1['bg'] = 'white'
    listbox2['bg'] = 'white'
    label1['bg'] = 'lightgray'
    label2['bg'] = 'lightgray'
    label3['bg'] = 'lightgray'
    label4['bg'] = 'lightgray'
    label1['fg'] = 'black'
    label2['fg'] = 'black'
    label3['fg'] = 'black'
    label4['fg'] = 'black'
    edit1['bg'] = 'white'

def set_dark_theme():
    root['bg'] = 'black'
    listbox1['bg'] = 'gray80'
    listbox2['bg'] = 'gray80'
    label1['bg'] = 'black'
    label2['bg'] = 'black'
    label3['bg'] = 'black'
    label4['bg'] = 'black'
    label1['fg'] = 'white'
    label2['fg'] = 'white'
    label3['fg'] = 'white'
    label4['fg'] = 'white'
    edit1['bg'] = 'gray80'

def set_default_theme():
    root['bg'] = '#F0F0F0'
    listbox1['bg'] = '#FFFFFF'
    listbox2['bg'] = '#FFFFFF'
    label1['bg'] = '#F0F0F0'
    label2['bg'] = '#F0F0F0'
    label3['bg'] = '#F0F0F0'
    label4['bg'] = '#F0F0F0'
    label1['fg'] = '#F0F0F0'
    label2['fg'] = '#F0F0F0'
    label3['fg'] = '#F0F0F0'
    label4['fg'] = '#F0F0F0'
    edit1['bg'] = '#FFFFFF'


x = y = 0

def do_popup(event):
    popupmenu.post(event.x_root, event.y_root)

# Інтерфейс
root = Tk()
root.title('Масиви')
root.geometry('650x400')

label1 = Label(text='Перший масив')
label1.place(x=20, y=30)

label2 = Label(text='Посортований масив')
label2.place(x=240, y=30)

label5 = Label(text='Другий масив')
label5.place(x=460, y=30)

listbox1 = Listbox(height=10, width=20)
listbox1.place(x=20, y=60)

listbox2 = Listbox(height=10, width=20)
listbox2.place(x=240, y=60)

listbox3 = Listbox(height=10, width=20)
listbox3.place(x=460, y=60)

label3 = Label(text='Кількість елементів:')
label3.place(x=20, y=250)

edit1 = Entry()
edit1.place(x=160, y=250)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=20, y=280)

button2 = Button(text='Сортувати (бульбашка)', width=20, command=sort)
button2.place(x=200, y=280)

button3 = Button(text='Сортувати (вибір)', width=20, command=sort_selection)
button3.place(x=200, y=310)

button4 = Button(text='Обчислити суму', width=20, command=compute_sum)
button4.place(x=20, y=310)

button5 = Button(text='Скалярний добуток', width=20, command=scalar_product)
button5.place(x=20, y=340)

label4 = Label(text='sum =')
label4.place(x=200, y=250)

# Меню
main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати (бульбашка)', command=sort)
array_menu.add_command(label='Сортувати (вибір)', command=sort_selection)
array_menu.add_command(label='Обчислити суму', command=compute_sum)
array_menu.add_command(label='Скалярний добуток', command=scalar_product)

about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label='Світла тема', command=set_light_theme)
popupmenu.add_command(label='Темна тема', command=set_dark_theme)
popupmenu.add_command(label='Початкова тема', command=set_default_theme)

root.bind("<Button-3>", do_popup)

root.mainloop()