import math as m

def triangle():
    b = float(input("Enter Base of Triangle: "))
    h = float(input("Enter Height of Triangle: "))
    a = 1/2*b*h
    print("Area of Triangle:",a)
    s = list()
    for i in range(1,4):
        n = float(input(f"Enter {i} side lengh: "))
        s.append(n)
    n = m.fsum(s)
    print("Perimeter of triangle:",m.fsum(s))
    with open("save_data.txt","+a") as f:
        f.writelines([f"\nTriangle:\nBase:{b}\nHeight:{h}\nArea:{a}\nAll Three sides:{s}\nPerimeter:{n}"])