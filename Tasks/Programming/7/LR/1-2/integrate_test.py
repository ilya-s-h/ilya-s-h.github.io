from integrate import integrate, integrate_async
from fun import f


def test_integrate():
    assert integrate(f, 1, 10, n_iter=10000) == 0.70528875,\
        "Интеграл f(x) = (sin(0.2m^2+0.7))/(1.4+cos(0.5m+0.2)) от 1 до 10 вычислен некорректно"


def test_integrate_2():
    import math
    assert integrate(math.sin, 1, 2.5, n_iter=1000) == 1.34054616, \
        "Интеграл f(x) = sin(x) от 1 до 2.5 вычислен некорректно"


def test_integrate_type():
    result = integrate(f, 1, 10, n_iter=10000)
    assert type(result) is float, "Результат должен быть представлен в виде float"


def test_integrate_3():
    assert integrate(f, 10, 10, n_iter=10000) == 0, "Результат должен быть равен 0, если a равно b"


def test_integrate_async():
    assert integrate_async(f, 1, 10, n_jobs=2, n_iter=10000) == 0.70528876,\
        "Интеграл f(x) = (sin(0.2m^2+0.7))/(1.4+cos(0.5m+0.2)) от 1 до 10 вычислен некорректно"


def test_integrate_async_type():
    result = integrate_async(f, 1, 10, n_jobs=2, n_iter=10000)
    assert type(result) is float, "Результат должен быть представлен в виде float"


def test_integrate_async_2():
    import math
    assert integrate_async(math.cos, math.pi, math.pi * 2, n_jobs=2, n_iter=10000) == 0, \
        "Интеграл f(x) = (sin(0.2m^2+0.7))/(1.4+cos(0.5m+0.2)) от 1 до 10 вычислен некорректно"


def test_integrate_async_3():
    assert integrate_async(f, 10, 10, n_iter=10000) == 0, "Результат должен быть равен 0, если a равно b"
