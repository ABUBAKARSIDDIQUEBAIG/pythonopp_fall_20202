#   Here in this lecture we are going to see how we can insert or retrieve values from the list using the loops.
list_stdName = []
list_stdAge = []
numberOfRecords = int(input("How many records you want to enter: "))
print("---------------------------------------------------")
listIndex = 0
while listIndex < numberOfRecords:  # 0<3, 1<3, 2<3, 3<3
    list_stdName.append(input("Enter the name of student: "))
    list_stdAge.append(input("Enter the age of student:"))
    print("---------------------------------------------------")
    print(" Your Enter Record Saved ")
    print("---------------------------------------------------")
    listIndex = listIndex + 1  # 0+1=1, 1+1=2, 2+1=3
counter = 0
for name in list_stdName:
    print("The name of student = " + name)
    print("The age of student = " + list_stdAge[counter])
    counter = counter+1
    print("------------------------------")
print(list_stdName)
print(list_stdAge)


