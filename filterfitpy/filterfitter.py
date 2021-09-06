from scipy.optimize import curve_fit
from inspect import signature
from .oversample import oversample as oversample1

class FilterFitter:

    def __init__(self, filterclass):

        self.filterclass = filterclass
        self.__call__ = self.fit

    def fit(self, x, y, skip=None, method='dogbox', verbose=0, p0=None, **kwargs):
        """The interesting part of the waveform for determining the filter is
            the transient response but the specified signal might be
            the steady state part.  Use `skip=0` to consider the transient response.
        """

        if skip is None:
            skip = min(100, len(x) // 4)
        
        if p0 is None:
            sig = signature(self.filterclass)
            N = len(sig.parameters)
            p0 = [1] * N

        def func(x, *params):
            fil = self.filterclass(*params)
            return fil(x)[skip:]
        
        params, cov = curve_fit(func, x, y[skip:], p0=p0, method=method,
                                verbose=verbose, maxfev=1e5, **kwargs)
        fil = self.filterclass(*params)
        
        return fil

        
def filterfitter(filterclass, x, y, skip=None, method='dogbox', verbose=0, oversample=1, p0=None, **kwargs):

    fitter = FilterFitter(filterclass)

    if oversample != 1:
        x = oversample1(x, oversample)
        y = oversample1(y, oversample)        
    
    return fitter.fit(x, y, skip=skip, method=method, verbose=verbose, p0=p0, **kwargs)
