from numpy import zeros, cos, arange, pi

from .filters import AR1MA2, AR1MA3
from .filterfitter import FilterFitter

fitter = FilterFitter(AR1MA2)

t = arange(200)
x = cos(2 * pi * 5 * t / 400)

fil = AR1MA2(0.4, -0.4, 2)

y = fil(x)

print(fitter.fit(x, y))


