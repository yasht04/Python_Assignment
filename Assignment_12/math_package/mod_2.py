class inp(Exception):
    def __init__(self,*i):
        super().__init__(*i)
def square():
    try:
        a = float(input("Enter length of side of square: "))
        if a<=0:
            raise inp("cannot accept 0 as length.")
        c = 4*a
        print("Circumference:",c)
        s = a*a
        print("Area:",s)
        with open("save_data.txt","+a") as f:
            f.writelines([f"\nSquare:\nSide length:{a}\nCircumference:{c}\nArea:{s}"])
    except inp as i:
        print(i.args[0])
