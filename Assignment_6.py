def ds(roll_no,name):
    n1 = [roll_no,name]
    n2 = (roll_no,name)
    n3 = {roll_no,name}
    n4 = {"roll no":roll_no,"name":name}

    print(n1)
    print(n2)
    print(n3)
    print(n4)

    roll = int(input("Enter Roll no: "))
    name = input("Enter name: ")

    n1[0] = roll
    n1[1] = name
    n2 = (roll,name)
    n3.clear()
    n3.add(roll)
    n3.add(name)
    n4["roll no"]= roll
    n4["name"]=name

    print("list:",n1)
    print("tuple:",n2)
    print("set:",n3)
    print("dictionary:",n4)

    del n1
    del n2
    del n3
    del n4

roll = int(input("enter roll no.: "))
name = input("Enter name: ")
ds(roll,name)
