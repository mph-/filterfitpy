from scipy.optimize import curve_fit


class FilterFitter:

    def __init__(self, fil):

        self.fil = fil

    def fit(self, x, y, skip=100, method='dogbox', verbose=0):

        N = len(self.a) + len(self.b)
        p0 = [0.5] * N

        def func(x, *params):

            fil = self.fil(*params)
            return fil(x)[skip:]
        
        params, cov = curve_fit(func, x, y[skip:], p0=p0, method=method, verbose=verbose, maxfev=1e5)

        return self.fil(*params)

        

        
        