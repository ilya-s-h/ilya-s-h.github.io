from flask import Flask, request
import os
import socket
import json
import mysql.connector

app = Flask(__name__)

count = 0 # инициализация счётчика

@app.route('/')
def hello():
    name = os.getenv("NAME", 'world') # получение значения переменной окружения (значение по умолчанию - world)
    hostname = socket.gethostname() # получение имени хоста

    # данные, которые отправляются клиенту:
    # значение переменной окружения name, имя хоста, значение счётчика
    html = f'''
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    <b>Counter value:</b> {count}
    '''
    return html


@app.route('/stat')
def stat():
    """
    Прототип функции, возвращающей значение счетчика
    """

    global count # обращаемся к глобальной переменной count
    count += 1 # увеличиваем значение счётчика
    # отправляем клиенту текущее значение
    html = f'Counter value: {count}'

    return html


@app.route('/initdb')
def db_init():
    # инициализация базы данных
    # подключение к БД
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1")
    cursor = mydb.cursor() # получаем курсор

    cursor.execute("DROP DATABASE IF EXISTS counter") # удаляем таблицу counter, если она есть в БД
    cursor.execute("CREATE DATABASE counter") # создаём таблицу counter

    cursor.close()

    # подключение к БД counter
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="counter")
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS logs") # удаляем таблицу logs, если она есть в БД
    cursor.execute(
        "CREATE TABLE logs (datetime VARCHAR(255), cilent_info VARCHAR(255))") # создаём таблицу logs
    cursor.close()

    return 'database init completed'


@app.route('/addlog')
def add_logs():
    """
    Позволяет вводить данные о посещении
    """

    # подключение к БД
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="counter")

    import datetime # для получения текущего времени

    headers = str(request.headers['User-Agent']) # получаем User-Agent клиента
    
    cursor = mydb.cursor() # получаем курсор

    data = (datetime.datetime.now(), headers) # формируем кортеж с датой и информацией о клиенте (User-Agent)
    cursor.execute('INSERT INTO logs VALUES (%s, %s)', data) # добавляем данные в БД

    mydb.commit() # сохраняем изменения в БД
    
    return 'log added successfully'


@app.route('/logs')
def get_logs():
    """
    Извлекает данные из таблицы logs
    """

    # подключение к БД
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="p@ssw0rd1",
                                   database="counter")
    cursor = mydb.cursor() # получаем курсор

    cursor.execute("SELECT * FROM logs") # запрос на получение данных из таблицы logs

    row_headers = [x[0] for x in cursor.description] # получаем названия полей таблицы logs

    results = cursor.fetchall() # получаем данные из таблицы logs
    json_data = [] # список со строками таблицы
    for result in results:
        json_data.append(dict(zip(row_headers, result))) # добавляем строку таблицы logs в список

    cursor.close()

    return json.dumps(json_data) # преобразуем список в JSON и отправляем клиенту


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
