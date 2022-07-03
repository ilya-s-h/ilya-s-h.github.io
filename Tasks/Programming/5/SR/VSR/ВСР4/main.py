import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('apartment-prices.csv', delimiter=',')
x, y = data[:,0], data[:,1]

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

for deg in [1, 2]:
    f1p, residuals, rank, sv, rcond = np.polyfit(x, y, deg, full=True)
    f1 = np.poly1d(f1p)
    fx = np.linspace(min(x), max(x), 500)

    plt.scatter(x, y, s=10)
    plt.plot(fx, f1(fx), linewidth=1.0, color='r')
    plt.title('Зависимость стоимости квартиры от её площади')
    plt.xlabel('Площадь')
    plt.ylabel('Стоимость')
    plt.grid(True)
    plt.show()
