from numpy import zeros, cos, sin, arange, pi

from .filters import AR1MA2, AR1MA3
from .filterfitter import filterfit

t = arange(200)
x = cos(2 * pi * 5 * t / 400) + 0.3 * sin(2 * pi * 11 * t / 400) + 0.2 * cos(2 * pi * 51 * t / 400)

fil = AR1MA2(0.4, -0.4, -0.05)

y = fil(x)

fil1 = filterfit(AR1MA2, x, y)
print(fil1)

fil2 = filterfit(AR1MA3, x, y)
print(fil2)


