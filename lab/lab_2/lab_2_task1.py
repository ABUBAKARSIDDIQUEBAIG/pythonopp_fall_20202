#And also Get table Number, String, rang, And Ending range
#creat table

#Creat table with two different way
#first Creat table with for loop
#And secound creat table with while loop
print("===---===___===---===_Creat table_===---===___===---___===")
print("===---===___===---===_Creat table with while loop_===---===___===---___===")
alphanumber= int(input("Enter a number: "))
upperlimit = int(input("Enter a upper limit: "))
lowerlimit = int(input("Enter a lower limit: "))
i = upperlimit
while (i <= lowerlimit):
    print (i,"*",alphanumber,"=",i*alphanumber)
    i=i+1
print("===---===___===---===_Creat table_===---===___===---___===")
print("===---===___===---===_Creat table with for loop_===---===___===---___===")

betanumber = int(input("Enter a number: "))
highrange = int(input("Enter a upper limit: "))
lowrange = int(input("Enter a lower limit: "))
for foreachnumber in range(highrange, lowrange+1):
    print (i,"*",betanumber,"=",i*betanumber)