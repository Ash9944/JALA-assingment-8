class Pri:
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
        self._A = (self._a**3 + self._b**3 + self._c**3)
    def main(self):
        return self._A
class sub1(Pri):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)