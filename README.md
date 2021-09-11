Introduction
============

This Python module is for fitting filters given the input and output signals.  It is naive but effective.


Installation
============

The easiest way is using the command line command:

   $ pip install .


Usage
=====

``` python
from numpy import zeros, cos, arange, pi

from filterfitpy import AR1MA2, FilterFitter

fitter = FilterFitter(AR1MA2)

t = arange(200)
# This signal does not have enough frequency components
# to provide much discrimination between filters.
x = 3 * cos(2 * pi * 5 * t / 400) + sin(2 * pi * 11 * t / 400)

fil = AR1MA2(2, 0.4, -0.04)

y = fil(x)

print(fitter.fit(x, y))

```

There are a number of predefined filters such as AR1MA2 with one autoregressive term and two moving average terms in the difference equation.

