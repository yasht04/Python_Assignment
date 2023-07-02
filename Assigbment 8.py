class A:
    __a = None
    _b = None
    c = None
    def __init__(self,a,b,c):
        self.__a = a
        self._b = b
        self.c = c
        
    def display(self):
        print("Class A:")
        print("a:",self.__a)
        print("b:",self._b)
        print("c:",self.c)

class B(A):
    def display(self):
        try:
            print("Class B:")
            print("a:",self.__a)
        except AttributeError:
            print("Cannot access private data member")
        print("b:",self._b)
        print("c:",self.c)


a = B(5,6,7)
a.display()