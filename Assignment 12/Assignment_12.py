import math_package.mod_1 as m1
import math_package.mod_2 as m2
import math_package.mod_3 as m3
import math_package.mod_4 as m4
import math_package.mod_5 as m5
n = "1"
while n == "1":
    print("\n1)Circle \n2)Square \n3)Rectangle \n4)Triangle \n5)Parallelogram \n6)See History\n")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        m1.circle()
    elif ch == 2:
        m2.square()
    elif ch == 3:
        m3.rectangle()
    elif ch == 4:
        m4.triangle()
    elif ch == 5:
        m5.para()
    elif ch == 6:
        with open("save_data.txt","+r") as f:
            f.seek(0)
            print(f.readlines())
    else:
        print("Invalid Choice!")
    n = input("To continue press 1 or press enter to exit ")
    if n != "1":
        exit()