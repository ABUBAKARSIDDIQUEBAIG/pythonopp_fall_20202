#Topic: Classes and Lists. ---- Lab --- 4
#----> Task-1: Create two classes university and teacher,
#   - University class will have three variable ---> uniName, uniCity, uniAge
#   - University class will have one function ---> University Information ---> which will show all the information of university.
#   - Teacher class will have three variable ---> tchName, tchSubject, tchSal
#   - Teacher class will have one function ---> Teacher Introduction ---> which will show the introduction of teacher.
#----> Task - 2:
# Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.
#    - Then use loops to get the information and introduction of universities and teachers.
#Task1
#Class one1
class university:
    uniName = ""
    uniCity = ""
    uniAge = ""
    def information(self):
        print("uniName is: " +self.uniName)
        print("uniCity is: " + self.uniCity)
        print("uniAge is: "  +str(self.uniAge) )
        print("====-----====-----====-----====-----====")

#Task1
#CLASS two2
class teacher:
    tchName = ""
    tchSubject = ""
    tchSal  =  ""
    def information(self):
        print("tchName is: " + self.tchName)
        print("tchSubject is:  " + self.tchSubject)
        print("tchSal is: " + str(self.tchSal))
        print("====-----====-----====-----====-----====")

#creat the object of class university
uni = university()
uni.uniName = "superior university"
uni.uniCity = "Lahore"
uni.uniAge = 15
uni.information()
print("====-----====-----====-----====-----====")
#creat the object of the Teacher class
tch = teacher()
tch.tchName = "sir Qasim riaz"
tch.tchSubject = "object orianted programing"
tch.tchSal = 200000
tch.information()
print("====-----====-----====-----====-----====")
print("====-----====-----====-----====-----====")
print("====-----====-----====-----====-----====")
#task two2
#----> Task - 2:
# Create 2 lists one list will contain the 5 objects of university class and second list will contain the 5 objects of teacher class.
#    - Then use loops to get the information and introduction of universities and teachers.
#creat the object of university
uni1 = university()
uni1.uniName="uskt"
uni1.uniCity="sialkot"
uni1.uniAge="5"

uni2 = university()
uni2.uniName="Punjab uni lahore"
uni2.uniCity="lahore"
uni2.uniAge="150"

uni3 = university()
uni3.uniName="UOF"
uni3.uniCity="faslabad"
uni3.uniAge="19"

uni4 = university()
uni4.uniName="GC"
uni4.uniCity="lahore"
uni4.uniAge="90"

uni5 = university()
uni5.uniName="uog"
uni5.uniCity="Gujrat"
uni5.uniAge="40"

#creat the object of teacher
tch1 = teacher()
tch1.tchName ="Abid"
tch1.tchSubject="english"
tch1.tchSal=40000

tch2 = teacher()
tch2.tchName ="hafiz zahib"
tch2.tchSubject="urdu"
tch2.tchSal=60000

tch3 = teacher()
tch3.tchName ="wahab"
tch3.tchSubject="ITC"
tch3.tchSal=40000

tch4 = teacher()
tch4.tchName ="nabia"
tch4.tchSubject="programing"
tch4.tchSal=80000


tch5 = teacher()
tch5.tchName ="zohab ahmad"
tch5.tchSubject="islami Education"
tch5.tchSal=50000
unilist = [uni1,uni2,uni3,uni4,uni5]
tchlist =  [tch1,tch2,tch3,tch4,tch5 ]
for eachuniversity in unilist:
    eachuniversity.information()
foreachteacher in tchlist:
    eachteacher.information()
