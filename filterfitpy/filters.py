from .filter import Filter

class Ar0diff(Filter):

    def __init__(self, b0):

        a = [1]
        b = [b0, -b0]    
        super(Ar0diff, self).__init__(b, a)

class Ar1diff(Filter):

    def __init__(self, a0, b0):

        a = [1, a0]
        b = [b0, -b0]    
        super(Ar1diff, self).__init__(b, a)

class Ar0ma2(Filter):

    def __init__(self, b0, b1):

        a = [1]
        b = [b0, b1]    
        super(Ar0ma2, self).__init__(b, a)

class Ar0ma3(Filter):

    def __init__(self, b0, b1, b2):

        a = [1]
        b = [b0, b1, b2]    
        super(Ar0ma3, self).__init__(b, a)

class Ar1ma2(Filter):

    def __init__(self, a1, b0, b1):

        a = [1, a1]
        b = [b0, b1]    
        super(Ar1ma2, self).__init__(b, a)

class Ar1ma3(Filter):

    def __init__(self, a1, b0, b1, b2):

        a = [1, a1]
        b = [b0, b1, b2]
        super(Ar1ma3, self).__init__(b, a)

class Ar1ma4(Filter):

    def __init__(self, a1, b0, b1, b2, b3):

        a = [1, a1]
        b = [b0, b1, b2, b3]
        super(Ar1ma4, self).__init__(b, a)

class Ar2diff(Filter):

    def __init__(self, a1, a2, b0):

        a = [1, a1, a2]
        b = [b0, -b0]    
        super(Ar2diff, self).__init__(b, a)

class Ar2ma2(Filter):

    def __init__(self, a1, a2, b0, b1):

        a = [1, a1, a2]
        b = [b0, b1]    
        super(Ar2ma2, self).__init__(b, a)

class Ar2ma3(Filter):

    def __init__(self, a1, a2, b0, b1, b2):

        a = [1, a1, a2]
        b = [b0, b1, b2]    
        super(Ar2ma3, self).__init__(b, a)
        
