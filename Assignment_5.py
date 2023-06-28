l = list()
for i in range(1,6):
    n = int(input("enter element: "))
    l.append(n)
#Calculate the sum of all the elements in the list
print("sum of all elements in list:",sum(l))

#Find the smallest number
print("Smallest element in list:",min(l))

#Find the largest number
print("Largest element in list:",max(l))

#Display list in ascending order
l.sort()
print("list in ascending order:",l)

#Display list in descending order
l.reverse()
print("List in descending order:",l)

#Convert list into tuple
list_to_tuple = tuple(l)
print(list_to_tuple)
print(type(list_to_tuple))

#Delete the list.
del l