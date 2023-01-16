import concurrent.futures as ftres

def integrate(f, a: float, b: float, *, n_iter: int = 1000):
    if b == a:
        return 0

    h = (b-a)/float(n_iter)
    z = 0
    x = a + h

    while x <= b - h:
      z = z + f(x)
      x = x + h

    y = (f(a)+ f(b)) /2
    z = h*(z+y)

    return round(z, 8)


def integrate_async(f, a: float, b: float, *, n_jobs: int = 2, n_iter: int = 1000):
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs) # пул потоков
    step = (b - a) / n_jobs # интервал делится на части, кол-во частей равно числу потоков

    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)] # указание интервала для вычисления в каждом потоке
    spawn_lst = [executor.submit(integrate, f, *interval, n_iter= n_iter // n_jobs) for interval in fs] # запуск потоков, общее число итераций n_iter делится на число потоков
    s = [r.result() for r in ftres.as_completed(spawn_lst)] # каждый поток вычисляет значение интеграла на части интервала от a до b

    return sum(s) # значение интеграла равно сумме значений, вычисленных для каждой части в потоках
