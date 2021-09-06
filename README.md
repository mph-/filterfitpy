Introduction
============

This Python module is for fitting filters to measured signals. 


Installation
============

The easiest way is using the command line command:

   $ pip install .


Usage
=====

``` python
from numpy import zeros, cos, arange, pi

from .filters import Ar1diff
from .filterfitter import FilterFitter

fitter = FilterFitter(Ar1diff)

t = arange(200)
x = cos(2 * pi * 5 * t / 400)

fil = Ar1diff(2, 0.4)

y = fil(x)

print(fitter.fit(x, y))

```



