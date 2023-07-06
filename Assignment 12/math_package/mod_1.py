import math as m
class input(Exception):
    def __init__(self,*i):
        super().__init__(*i)
def circle():
    try:
        r = float(input("Enter Radius of Circle: "))
        if r<=0:
            raise input("cannot accept 0 as Radius.")
        a = m.pi*m.pow(r,2)
        print("Area of circle:",a)
        cir = 2*m.pi*r
        print("Circumference:",cir)
        with open("save_data.txt","+a") as f:
            f.writelines([f"\ncircle:\nRadius:{r}\nArea:{a}\nCircumference:{cir}"])
    except input as p:
        print(p.args[0])