class Private:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__A = (self.__a**3 + self.__b**3 + self.__c**3)
    def main(self):
        return self.__A
class sub(Private):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)