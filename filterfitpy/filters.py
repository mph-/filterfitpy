from .filter import Filter

class Ideal(Filter):

    def __init__(self):

        a = [1]
        b = [1]    
        super(Ideal, self).__init__(b, a)

class AR0Diff(Filter):

    def __init__(self, b0):

        a = [1]
        b = [b0, -b0]    
        super(AR0Diff, self).__init__(b, a)

class AR1Diff(Filter):

    def __init__(self, b0, a0):

        a = [1, a0]
        b = [b0, -b0]    
        super(AR1Diff, self).__init__(b, a)

class AR0MA2(Filter):

    def __init__(self, b0, b1):

        a = [1]
        b = [b0, b1]    
        super(AR0MA2, self).__init__(b, a)

class AR0MA3(Filter):

    def __init__(self, b0, b1, b2):

        a = [1]
        b = [b0, b1, b2]    
        super(AR0MA3, self).__init__(b, a)

class AR1MA2(Filter):

    def __init__(self, b0, b1, a1):

        a = [1, a1]
        b = [b0, b1]    
        super(AR1MA2, self).__init__(b, a)

class AR1MA3(Filter):

    def __init__(self, b0, b1, b2, a1):

        a = [1, a1]
        b = [b0, b1, b2]
        super(AR1MA3, self).__init__(b, a)

class AR1MA4(Filter):

    def __init__(self, b0, b1, b2, b3, a1):

        a = [1, a1]
        b = [b0, b1, b2, b3]
        super(AR1MA4, self).__init__(b, a)

class AR2Diff(Filter):

    def __init__(self, b0, a1, a2):

        a = [1, a1, a2]
        b = [b0, -b0]    
        super(AR2Diff, self).__init__(b, a)

class AR2MA2(Filter):

    def __init__(self, b0, b1, a1, a2):

        a = [1, a1, a2]
        b = [b0, b1]    
        super(AR2MA2, self).__init__(b, a)

class AR2MA3(Filter):

    def __init__(self, b0, b1, b2, a1, a2):

        a = [1, a1, a2]
        b = [b0, b1, b2]    
        super(AR2MA3, self).__init__(b, a)
