lenOfList= int(input("Enter the number of List: "))
li= []

for i in range(lenOfList):
    number= int(input(f"Enter the {i} value: "))
    li.append(number)
print("Your list is: ")
print(li)
s= sum(li)
avg= s/2
print(f"Your Sum of list is {s} and average of list is: {avg}")