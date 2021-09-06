from scipy.signal import lfilter

class Filter:

    def __init__(self, b, a):

        self.b = b
        self.a = a

    def __call__(self, x):

        y = lfilter(self.b, self.a, x)
        return y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'b=%s, a=%s' % (self.b, self.a)
    
    def rmse(self, x, z, skip=100):

        zfit = self(x)
        rmse = np.sqrt(np.mean((zfit[skip:] - z[skip:])**2))

        return rmse
    

        
