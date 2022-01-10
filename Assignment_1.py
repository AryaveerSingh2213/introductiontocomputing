#Assignment_1
#Question_1_Average of three numbers entered by the user
number_1=int(input("Enter the first number  :"))
number_2=int(input("Enter the second number :"))
number_3=int(input("Enter the third number :"))
print("The first number is :",number_1)
print("The second number is :",number_2)
print("The third number is :",number_3)
sum=number_1+number_2+number_3
#Average
avg=sum/3
print("The average of ",number_1 ,",",number_2 ,"and",number_3 ,"is =",avg)

#Question_2_Calculation of a person's income tax
tax_rate=20
#Tax Rate = 20%
print("Tax Rate is : ", tax_rate)
std_deduxn=10000
# All taxpayers are allowed a $10,000 standard deduction
print("Standard Deduction is : ", std_deduxn)
#For each dependent , a taxpayer is allowed an additional $3,000 deduction
dep_deduxn=3000
print("Additional Dependent Deduction is :",dep_deduxn)
gross_income=float(input("Enter Gross Income : "))
dependent_no=int(input("Enter the Number of Dependents : "))
taxable_income=gross_income-std_deduxn-(dep_deduxn*dependent_no)
print("Taxable Income is : ",taxable_income)
tax=taxable_income*tax_rate/100
print("Income Tax is  : ",tax)

#Ques_3_Storage of different datatype values into a list
Name = input("Enter the name of the student : ")
SID = int(input("Enter the student I.D. : "))
Gender = input("Enter the gender of the student (F,M,U) : ")
Course = input("Enter the student's  course name : ")
CGPA = input("Enter the student's CGPA : ")
Student = [ "Name", "SID" , "Gender" , "Course" , "CGPA" ]
print(Student)
Student_info =[Name , SID , Gender , Course , CGPA]
print(" Te list of the student's information is : " , Student_info)

#Ques_4_Entry and display of marks of five students into a list in a sorted manner
print("Marks of the five students are :")
SMarks = [ 88 , 93 , 89 , 78 , 90 ]
print(" List of students' marks before sorting is : " , SMarks)
SMarks.sort()
print(" List ofstudents' marks after sorting in increasing order  is : " , SMarks)

#Ques_5_(a) Removal of fourth element i.e. Black ( index = 3 ) :
Colour=[ "Red" , "Green" , "White" , "Black" , "Pink" , "Yellow" ]
print(" Colour list is : " , Colour)
Colour.pop(3)
print("(a) List of colours after removing the fourth element is : " ,Colour)

#Ques_5_(b) Replacement of Black and Pink by Purple :
Colour=[ "Red" , "Green" , "White" , "Black" , "Pink" , "Yellow" ]
print(" Colour list is : " , Colour )
Colour[ 3:5 ] = ["Purple"]
print("(b) List of colours after replacing Black and Pink by Purple is  : " ,Colour)