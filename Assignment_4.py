n = "python"
print("\nbreak")
for i in n:
    if i == "h":
        break
    else:
        print(i)
        
print("\npass")
a = [1,2,3,4,5]
for i in a:
    if i == 4:
        pass
    else:
        print(i)

print("\ncontinue")
a = [1,2,3,4]
for i in a:
    if i == 2:
        continue
    else:
        print(i)
        
        
print("\nfor with else")
for i in a:
    if i%2 == 0:
        print("even number:",i)
        break
    
else:
    print("even number is not present")


print("\nwhile with else")
i = 1
while i <= 5:
    print(i)
    i+=1

else:
    print("out of while")