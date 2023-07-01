def func(file):
    f = open(file,'+a')
    roll = int(input("Enter Your Roll No.: "))
    name = input("Enter Your Name: ")
    class_ = input("Enter Your Class: ")
    f.writelines([f"Roll No.: {roll},",f" Name: {name},",f" Class: {class_}"])
    f.seek(0)
    print(f.readlines())

file = input("Enter file name and add .txt at end: ")
func(file)