print("==========--***===***===***===***===***===***===***===***===***===***")
print("==***===***===***===*Task 2 question1*===***===***===***===***===***==")
n=int(input("Enter the number :"))
if(n%2==0):
    print(n,"This number is Even")
else:
    print(n,"This number is Odd")
print( "== == == == == -- ** *= == ** *= == ** *= == ** *= == ** *= == ** *= == ** *= == ** *= == ** *= == ** * ")
#####
#b) print odd and even number by using for loop and user will enter the starting range and ending range
print("==========--***===***===***===***Task2 question number2***===***===***===***===***===***")
lowerrang = int(input("Enter the first number: "))
higherrang = int(input("Enter the end number: "))
higherrang +=1
for x in range(lowerrang,higherrang):
    if x %2 == 0:
        print("The number is even: ",x)
    else:
        print("The number is odd: ", x)
#The given number is even and odd numb
print("==========--***===***===***===***==***===***===***===***===***===***")
print("==========--***===***===***===*Task2 question3*===***===***===***===***===***===***")
