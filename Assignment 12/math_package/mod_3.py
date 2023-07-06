
def rectangle():
    l = float(input("Enter Length of rectangle: "))
    b = float(input("Enter Breadth of rectangle: "))
    a = l*b
    print("Area:",a)
    p = 2*(l+b)
    print("Perimeter: ",p)
    with open("save_data.txt","+a") as f:
        f.writelines([f"\nReactangle:\nLength:{l}\nBreadth:{b}\nArea:{a}\nPerimeter:{p}"])