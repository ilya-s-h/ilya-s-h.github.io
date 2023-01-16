import timeit
from integrate import integrate, integrate_async
from fun import f

def run_tests(test_function):
    for n_iter in [10**4, 10**5, 10**6]:
        t = timeit.timeit(lambda: test_function(f, 1, 10, n_iter=n_iter), number=100)
        print(f'Function {test_function.__name__}, n_iter={n_iter}, number=100: result = {t:.2f} sec.')

if __name__ == '__main__':
    run_tests(integrate)
    run_tests(integrate_async)
