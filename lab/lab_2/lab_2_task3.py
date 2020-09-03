#3) enter a number from user and check it whether it is primary number or not
print("==========--***===***===***===***===***===***===***===***===***===***")
print("==========--***===***===***==*Task3 question3*===***===***===***===***===***")
print("==========--***===***  Find the given number is prime number or not ===***===***===***===***")
primenumber = int(input("Enter any positive number to check whether it is Even or odd number"))
if primenumber >1:
    for host in range(2,primenumber):
        if(primenumber%host)==0:
            print(primenumber,"is not a prime number")
            break
    else:
        print(primenumber,"is a prime number ")
else:
    print(primenumber,"is not a prime number")
    print("==========--***===***===***===***===***===***===***===***===***===***")
