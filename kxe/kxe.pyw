import os, random
from tkinter import *
from tkinter.messagebox import showinfo

def exit():
	try:
		os.system('shutdown -s -t 5')
	except:
		print('Error!')
	print('power off')
	lab['foreground'] = 'black'
	lab['text'] = '\n\n\nВы проиграли!\t\t\t'
	lab['font'] = 'Arial 30'
	root['background'] = lab['background']
	for i in array:
		i.grid_forget()

def Win():
	root = Tk()
	lab = Label(root, text='''
		\nПоздравляю! \nВы победили!\n"
		''',font = 'Arial 18', height=20, background='black', foreground='red')
	os.system('shutdown -a')
	lab.pack()
	root.mainloop()

def cancel(event):
	os.system('shutdown -a')

def about():
	showinfo('Информация', "Автор программы Храбрых Максим\nEmail - Neonexer12@gmail.com\n")

root = Tk()
root.geometry('864x422')
root['background'] = 'white'
root.title('Секретная кнопка')
try:
	root.iconbitmap(r'C:\Users\Maxim\Desktop\Alex-T-Fresh-Fruit-Apple.ico')
except:
	None
root.resizable(False, False)


m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_command(label="Информация", command=about)
m.add_command(label="Выход", command=exit)

lab = Label(root, text='''
		\n\n\tВам необходимо выбрать верную кнопку,\t\n   иначе компьютер будет выключен.\t\n\n
		''', font = 'Arial 20', width='53')

pushButton = Button(root, bg='silver', width = 23, height = 3)
pushButton_2 = Button(root, bg='silver', width = 23, height = 3)
pushButton_3 = Button(root, bg='silver', width = 23, height = 3)

array = [pushButton, pushButton_2, pushButton_3]

lab.grid(row=0, column=0, columnspan=3)
pushButton.grid(row=1, column=0)
pushButton_2.grid(row=1, column=1)
pushButton_3.grid(row=1, column=2)
os.system('shutdown -s')
n=0
for i in array:
    i['text'] = 'Нажми меня'
    i['command'] = exit
    i['font'] = 'strong 16'
    i['height'] = 5
    i['border'] = 3

SecretButton = random.choice(array)
SecretButton['command'] = Win

root.bind('<Delete>', cancel)

root.mainloop()