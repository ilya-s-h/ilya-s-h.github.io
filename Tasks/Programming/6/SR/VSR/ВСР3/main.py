'''
3.1 Реализация графического интерфейса и формы для приложения «Гостевая книга»
с возможностью сохранения данных из полей формы в файл.
'''

import json
import os
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class GuestbookForm:
    def __init__(self):
        self.root = Tk()
        self.root.title('Гостевая книга')
        
        padx, pady = 8, 6
        font=('Segoe UI', 10)
        
        self.title = Label(text='Гостевая книга', font=('Segoe UI', 18))
        self.title.grid(row=0, column=0, columnspan=2, sticky=W, padx=padx, pady=pady)
        
        self.surnameLabel = Label(text='Фамилия:', font=font)
        self.surnameLabel.grid(row=1, column=0, padx=padx, pady=pady)
        self.surnameEntry = Entry(font=font, width=35)
        self.surnameEntry.grid(row=1, column=1, padx=padx, pady=pady)
        
        self.nameLabel = Label(text='Имя:', font=font)
        self.nameLabel.grid(row=2, column=0, padx=padx, pady=pady)
        self.nameEntry = Entry(font=font, width=35)
        self.nameEntry.grid(row=2, column=1, padx=padx, pady=pady)
        
        self.emailLabel = Label(text='E-mail:', font=font)
        self.emailLabel.grid(row=3, column=0, padx=padx, pady=pady)
        self.emailEntry = Entry(font=font, width=35)
        self.emailEntry.grid(row=3, column=1, padx=padx, pady=pady)
        
        self.phoneLabel = Label(text='Телефон:', font=font)
        self.phoneLabel.grid(row=4, column=0, padx=padx, pady=pady)
        self.phoneEntry = Entry(font=font, width=35)
        self.phoneEntry.grid(row=4, column=1, padx=padx, pady=pady)
        
        self.addressLabel = Label(text='Адрес:', font=font)
        self.addressLabel.grid(row=5, column=0, padx=padx, pady=pady)
        self.addressEntry = Entry(font=font, width=35)
        self.addressEntry.grid(row=5, column=1, padx=padx, pady=pady)
        
        self.saveButton = Button(text='Сохранить', command=self.save_data)
        self.saveButton.grid(row=6, column=0, columnspan=2, sticky=E, padx=padx, pady=pady)

        self.root.mainloop()
        
        
    def save_data(self):
        surname = self.surnameEntry.get()
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()
        entry = {
            'surname': surname,
            'name': name,
            'email': email,
            'phone': phone,
            'address': address
        }
        if not os.path.exists('guestbook.json'):
            with open('guestbook.json', 'w') as f:
                json.dump([], f)
        with open('guestbook.json', 'r+') as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f)
        showinfo(title='Гостевая книга', message='Данные сохранены.')
        
        
if __name__ == '__main__':
    GuestbookForm()