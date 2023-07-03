import math
class input_in_pow(Exception):
    def __init__(self,*i):
        super().__init__(*i)

class math_options:
    def add(self):
        print("Addition: ")
        a = int(input("enter number: "))
        b = int(input("enter number: "))
        print("Addition:",a+b)

    def sub(self):
        print("\nsubtraction: ")
        a = int(input("enter number: "))
        b = int(input("enter number: "))
        print("subtraction:",a-b)

    def mul(self):
        print("\nmultiplication: ")
        a = int(input("enter number: "))
        b = int(input("enter number: "))
        print("Multiplication:",a*b)

    def div(self):
        print("\ndivision: ")
        a = int(input("enter number: "))
        b = int(input("enter number: "))
        print("quetient:",a/b)
        print("remainder:",a%b)

    def Ceil(self):
        a = float(input("\nEnter number in float for ceil function: "))
        print("after ceil function: ",math.ceil(a))

    def Floor(self):
        a = float(input("\nEnter number in float for floor function: "))
        print("after floor function: ",math.floor(a))

    def Pow(self):
        print("\nFor pow function: ")
        try:
            a = int(input("enter number: "))
            b = int(input("enter number: "))
            if b<=0:
                raise input_in_pow("cannot accept 0 for pow function.")
            print("after pow function:",math.pow(a,b))
        except input_in_pow as i:
            print(i.args[0])
        
    def sum(self):
        print("\nEnter 5 values for list: ")
        l = list()
        for i in range(1,6):
            z = int(input(f"enter {i} value: "))
            l.append(z)
        print("sum of all elements in list:",math.fsum(l))

# m = math_options()
# m.sum()