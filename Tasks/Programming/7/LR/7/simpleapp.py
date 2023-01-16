from flask import Flask
import os
import socket

app = Flask(__name__)

count = 0 # инициализация счётчика

@app.route('/')
def hello():
    name = os.getenv("NAME", 'world') # получение значения переменной окружения (значение по умолчанию - world)
    hostname = socket.gethostname() # получение имени хоста

    # данные, которые отправляются клиенту:
    # значение переменной окружения name, имя хоста
    html = f'''
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    '''
    return html


@app.route('/stat')
def stat():
    global count # обращаемся к глобальной переменной count
    count += 1 # увеличиваем значение счётчика
    # отправляем клиенту текущее значение
    html = f'Counter value: {count}'

    return html


@app.route('/about')
def about():
    html = f'''
    Задание выполнил Илья Шумякин
	'''
    
    return html
	
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
