from integrate import integrate, integrate_async

from fun import f

# Написание программы для численного интегрирования площади под кривой.
# 10000 100000 1000000

if __name__ == '__main__':
    print("Метод трапеций")
    print("Интегрируемая функция: f(x) = (sin(0.2m^2+0.7))/(1.4+cos(0.5m+0.2))")
    print("Точность: 10^-8")
    print('Введите значение а и b')
    a = float(input())
    b = float(input())
    print('Введите количество разбиений')
    res = integrate(f, a, b, n_iter=float(input()))
    print('Ответ:', res)

