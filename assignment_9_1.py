import math
class input_in_pow(Exception):
    def __init__(self,*i):
        super().__init__(*i)

class math_options:
    def choose(self):
        i = "1"
        while i == "1":
            print("\n1)Arithmetic operations \n2)math module options \n3)set operations\n")
            n = int(input("Enter Choice: "))
            if n == 1:
                j = "1"
                while j == "1":
                    print("\n1)addition \n2)subtraction \n3)multiplication \n4)division \n")
                    a = int(input("Enter choice: "))
                    if a == 1:
                        print("Addition: ")
                        x = int(input("enter number: "))
                        y = int(input("enter number: "))
                        print("Addition:",x+y)
                    elif a == 2:
                        print("\nsubtraction: ")
                        x = int(input("enter number: "))
                        y = int(input("enter number: "))
                        print("subtraction:",x-y)
                    elif a == 3:
                        print("\nmultiplication: ")
                        x = int(input("enter number: "))
                        y = int(input("enter number: "))
                        print("Multiplication:",x*y)
                    elif a == 4:
                        try:
                            print("\ndivision: ")
                            x = int(input("enter number: "))
                            y = int(input("enter number: "))
                            print("quetient:",x/y)
                            print("remainder:",x%y)
                        except ZeroDivisionError as z:
                            print("do not enter 0 for division")
                    else:
                        print("Invalid input")
                    j = input("To continue press 1 or press enter to go to main menu ")
                    if j != "1":
                        break
            elif n == 2:
                j = "1"
                while j == "1":
                    print("\n1)Ceil \n2)Floor \n3)Pow \n4)sum \n")
                    a = int(input("Enter choice: "))
                    if a == 1:
                        z = float(input("\nEnter number in float for ceil function: "))
                        print("after ceil function: ",math.ceil(z))
                    elif a == 2:
                        z = float(input("\nEnter number in float for floor function: "))
                        print("after floor function: ",math.floor(z))
                    elif a == 3:
                        print("\nFor pow function: ")
                        try:
                            x = int(input("enter number: "))
                            y = int(input("enter number: "))
                            if y<=0:
                                raise input_in_pow("cannot accept 0 for pow function.")
                            print("after pow function:",math.pow(x,y))
                        except input_in_pow as p:
                            print(p.args[0])
                    elif a == 4:
                        print("\nEnter 5 values for list: ")
                        l = list()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value: "))
                            l.append(z)
                        print("sum of all elements in list:",math.fsum(l))
                    else:
                        print("Invalid input")
                    j = input("To continue press 1 or press enter to go to main menu ")
                    if j != "1":
                        break
            elif n == 3:
                j = "1"
                while j == "1":
                    print("\n1)Union \n2)intersection \n3)difference \n")
                    c = int(input("Enter choice: "))
                    if c == 1:
                        l = set()
                        l1 = set()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value for 1st set: "))
                            l.add(z)
                        print()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value for 2nd set: "))
                            l1.add(z)
                        print("Union lUl1:",l.union(l1))
                    elif c == 2:
                        l = set()
                        l1 = set()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value 1st set: "))
                            l.add(z)
                        print()
                        for i in range(1,6):
                                z = int(input(f"enter {i} value for 2nd set: "))
                                l1.add(z)
                        print("Union lnl1:",l.intersection(l1))
                    elif c == 3:
                        l = set()
                        l1 = set()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value 1st set: "))
                            l.add(z)
                        print()
                        for i in range(1,6):
                            z = int(input(f"enter {i} value for 2nd set: "))
                            l1.add(z)
                        print("Union l-l1:",l.difference(l1))
                    else:
                        print("Invalid input")
                    j = input("To continue press 1 or press enter to go to main menu ")
                    if j != "1":
                        break  
            else:
                print("Invalid input")
            i = input("To continue press 1 or press enter to exit ")
            if i != "1":
                exit()