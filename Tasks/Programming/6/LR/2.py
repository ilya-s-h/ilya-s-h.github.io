# -*- coding: utf-8 -*-
"""Лабораторная работа 3, 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_yS68aEj99YR1_8diOraadmigz3wFJa6
"""



"""Источник данных: https://www.kaggle.com/c/titanic/data"""

# Импортируем pandas
import pandas as pd
# Считываем содержимое CSV 
data = pd.read_csv('train.csv', index_col="PassengerId")
type (data)

# 1
def get_sex_distrib(data) -> str:
    """
    1. Какое количество мужчин и женщин ехало на параходе? 
    
    Приведите два числа через пробел.
    """
    # Считаем количество людей каждого пола с помощью value_counts()
    data['Sex'].value_counts()
    n_male, n_female = data['Sex'].value_counts()
    return f"{n_male}, {n_female}"

print(get_sex_distrib(data))

# 2

def get_port_distrib(data) -> str:
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? 
    Приведите три числа через пробел.
    """
    # Считаем количество портов отправления с помощью value_counts()
    port_S, port_C, port_Q = data['Embarked'].value_counts()
    return f"{port_S}, {port_C}, {port_Q}"


print(get_port_distrib(data))

def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """
    # Объявляем счётчики
    n_died, perc_died = 0, 0
    # Считаем количество погибшх и выживших с помощью value_counts()
    res = data['Survived'].value_counts()
    n_died, perc_died = res[0], round(res[0]/(res[1]+res[0])*100, 2)
    return n_died, perc_died

print(get_surv_percent(data))

def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    # Объявляем счётчики
    first_cl, second_cl, third_cl = 0, 0, 0
    # Считаем количество пассажиров с помощью value_counts()
    first_cl, second_cl, third_cl = data['Pclass'].value_counts()
    # Подсчёт общего числа пассажиров
    sum =  first_cl + second_cl + third_cl
    # Вычисляем долю пассажиров класса "n", округляем до двух знаков после запятой, возвращаем полученное значение
    return round(first_cl/(sum),2), round(second_cl/(sum), 2), round(third_cl/(sum),2)

print(get_class_distrib(data))

"""# **pandas.Series.corr** (Задание 5 - объяснение)

Series.corr(other, method='pearson', min_periods=None)[source]
Compute correlation with other Series, excluding missing values.

Parameters
otherSeries
Series with which to compute the correlation.

method{‘pearson’, ‘kendall’, ‘spearman’} or callable
Method used to compute correlation:

pearson : Standard correlation coefficient

kendall : Kendall Tau correlation coefficient

spearman : Spearman rank correlation

callable: Callable with input two 1d ndarrays and returning a float.

Warning

Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable’s behavior.

min_periodsint, optional
Minimum number of observations needed to have a valid result.

Returns
float
Correlation with other.
"""

def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    # Переменная для коэффициента Пирсона
    corr_val = -1
    # Считываем информацию о кол-ве супругов 
    sibsp = data['SibSp']
    # Считываем информацию о кол-ве детей
    parch = data['Parch']
    # Вычисляем корреляцию между количеством супругов и количеством детей
    corr_val = sibsp.corr(parch, method='pearson')
    return round(corr_val, 2)

print(find_corr_sibsp_parch(data))

# Импортируем isnan из numpy
from numpy import isnan
# TODO #6-1
def find_corr_age_survival(data) -> float:
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;

    """
    # Объявляем список возрастов
    age = []
    # Объявляем список выживших
    surv = []
    # Объявляем счётчик
    i = 0
    # Работаем со всеми данными Data
    while i < len(data):
      # Проверяем, не является ли возраст пассажира NaN
      if not(isnan(data.iloc[i]['Age'])):
         # Если нет, то добавляем возраст в список
        age.append(data.iloc[i]['Age'])
        # а также добавляем значение в список выживших
        surv.append(data.iloc[i]['Survived'])
      # Переходим к следующему пассажиру
      i+=1
    # Получаем Series (со списка возрастов, со списка выживших)
    age, surv = pd.Series(age), pd.Series(surv)
    # Вычисляем корреляцию
    corr_val = age.corr(surv)
    # Возвращаем округлённое значение
    return round(corr_val, 2)
print(find_corr_age_survival(data))

# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;
    """
    # Переменная для коэффициента Пирсона
    corr_val = -1
    # Объявляем список полов
    level_map = {'male': 0, 'female': 1}
    # Получаем Series (со списка полов)
    data['Sex_map'] = data['Sex'].map(level_map) # Map - values of Series according to an input mapping or function.
    # Вычисляем корреляцию
    corr_val = data['Sex_map'].corr(data['Survived'])
    return round(corr_val, 2)

print(find_corr_sex_survival(data))

# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - классом, в котором пассажир ехал, и параметром survival.
    """
    # Переменная для коэффициента Пирсона
    corr_val = -1
    # Вычисляем корреляцию (Информация о классе и информация о том, выжил пассажир или нет)
    corr_val = data['Pclass'].corr(data['Survived'])
    return round(corr_val, 2)

print(find_corr_class_survival(data))

# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров, медиану, минимальный и максимальный возраст
    """
    # Объявляем переменные среднего возраста, медианы, минимума и максимума
    mean_age, median, min, max = None, None, None, None
    # Подсчитываем средний возраст
    mean_age = round(data['Age'].mean(), 2)
    # Подсчитываем медиану
    median = round(data['Age'].median(), 2)
    # Вычисляем минимум
    min = round(data['Age'].min(), 2)
    # Вычисляем максимум
    max = round(data['Age'].max(), 2)
    return mean_age, median, min, max

print(find_pass_mean_median(data))

# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану, минимальную и максимальную цену
    """
    # Объявляем переменные средней цены, медианы, минимума и максимума 
    mean_price, median, min, max = None, None, None, None
    # Вычисляем среднюю цену
    mean_price = round(data['Fare'].mean(), 2)
    # Подсчитываем медиану
    median = round(data['Fare'].median(), 2)
    # Вычисляем минимум
    min = round(data['Fare'].min(), 2)
    # Вычисляем максимум
    max = round(data['Fare'].max(), 2)
    return mean_price, median, min, max

print(find_ticket_mean_median(data))

# Функция разделитель имён
def parse_name(name_list):
  #Создаём список имён
  first_name_list = []
  # Для каждого имени в полученном списке
  for i in name_list:
    # Если обнаружены (), то
    if '(' in i:
      # Имя определяется как имя в кавычках, остальные элементы отсекаются
      fn = i.split('(')[1].split(')')[0].split(' ')
    else:
      # Имя определяется как элемент после ., остальное отсекается
      fn = i.split(". ")[1].split(" (")[0].split(' ')
      # Каждое полученное имя занисим в список
    for name in fn:
      first_name_list += [name]
  return first_name_list

def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    # Объявляем список имён
    name = []
    # Считываем данные всех мужских имён
    data_with_names = data[['Sex', 'Name']].loc[data['Sex'] == 'male']

    # Список имен из series
    name_list = data_with_names['Name'].to_list()
    # Получаем Series (с обработанного списка name_list)
    series_names = pd.Series(parse_name(name_list))
    
    # Вычисление самого популярного имени по ключевым наименованиям
    name = series_names.value_counts().keys()[0]
    return name

print(find_popular_name(data))

# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    # Объявляем списки популярных мужских/женских имён
    popular_male_name, popular_female_name = [], []
    # Считываем данные тех людей, которые старше 15 лет
    data_with_names = data[['Sex', 'Name', 'Age']].loc[data['Age'] > 15]
    
    # Считываем мужские имена из прошлой выборки (series)
    data_with_names_male = data_with_names['Name'].loc[data_with_names['Sex'] == 'male']
    # Считываем женские имена из прошлой выборки (series)
    data_with_names_female = data_with_names['Name'].loc[data_with_names['Sex'] == 'female']

    # Возвращаем список мужских имен из серии
    name_list_male = data_with_names_male.to_list()
    # Получаем серию имен после обработки списка name_list_male
    series_names_male = pd.Series(parse_name(name_list_male))
     # Вычисление самого популярного имени по ключевым наименованиям
    popular_male_name = series_names_male.value_counts().keys()[0]
    

    # Возвращаем список женских имен из серии
    name_list_female = data_with_names_female.to_list()
    # Получаем серию имен после обработки списка name_list_female
    series_names_female = pd.Series(parse_name(name_list_female))
    # Вычисление самого популярного имени по ключевым наименованиям
    popular_female_name = series_names_female.value_counts().keys()[0]

    return popular_male_name, popular_female_name

print(find_popular_adult_names(data))

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
print((data.iloc[100]['Name']))

def test_get_sex_distrib():
    assert get_sex_distrib('train.csv') == (577,314), "1 Количество мужчин и женщин на Титанике"

def test_get_port_distrib():
    assert get_port_distrib('train.csv') == (644, 168, 77), "2 Количество портов отправления"

def test_get_surv_percent():
    assert get_surv_percent('train.csv') == (549, 61.62), "3 Доля погибших на параходе"

def test_class_distrib():
    assert class_distrib('train.csv') == (0.55, 0.24, 0.21), "4 Доли пассажиров класса 1, 2, 3"

def test_find_corr_sibsp_parch():
    assert find_corr_sibsp_parch('train.csv') == 0.41, "5 Коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch)"

def test_find_corr_age_survival():
    assert find_corr_age_survival('train.csv') == -0.08, "6 Корреляция между возрастом и параметром Survived"

def test_find_corr_sex_survival():
    assert find_corr_sex_survival('train.csv') == 0.54, "6 Корреляция между полом человека и параметром Survived"

def test_find_corr_class_survival():
    assert find_corr_class_survival('train.csv') == -0.34, "6 Корреляция между классом, в котором пассажир ехал, и параметром survival"

def test_find_pass_mean_median():
    assert find_pass_mean_median('train.csv') == (29.7, 28.0, 0.42, 80.0), "7 Средний возраст пассажиров, медиана, минимальный и максимальный возраст"

def test_find_ticket_mean_median():
    assert find_ticket_mean_median('train.csv') == (32.2, 14.45, 0.0, 512.33), "8 Средная цена за билет и медиана, минимальная и максимальная цена"

"""# Часть 2

Для набора данных из лабораторной работы 1 посчитать средние значения, медианы, максимальные и минимальные значения для столбцов Offline Spend, Online Spend.

https://replit.com/@IlyaShumyakin/ClassicIntelligentEvaluations#main.py
"""