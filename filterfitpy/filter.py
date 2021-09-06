from numpy import mean, sqrt
from scipy.signal import lfilter

class Filter:
    
    def __init__(self, b, a):
        """Create filter from lists of numerator, `n`,
        and denominator, `a`, coefficients."""
        
        self.b = b
        self.a = a

    def __call__(self, x):
        """Apply filter."""

        y = lfilter(self.b, self.a, x)
        return y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'b=%s, a=%s' % (self.b, self.a)

    def params(self):
        """Return tuple of parameters, not including a0=1."""

        return tuple(self.b + self.a[1:])
    
    def rmse(self, x, y, skip=100):
        """Return rms error for y - H * x.
        `skip` is the number of samples to ignore at start
        due to a transient response."""

        yfit = self(x)
        rmse = sqrt(mean((yfit[skip:] - y[skip:])**2))

        return rmse

