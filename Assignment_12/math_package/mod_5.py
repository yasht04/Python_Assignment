def para():
    b = float(input("Enter side of parallelogram: "))
    h = float(input("Enter height of parallelogram: "))
    a = b*h
    print("area of parallelogram:",a)
    p = 2*(b+h)
    print("perimeter of parallelogram:",p)
    with open("save_data.txt","+a") as f:
        f.writelines([f"\nParallelogram:\nSide:{b}\nHeight:{h}\nArea:{a}\nPerimeter:{p}"])