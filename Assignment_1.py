#Assignment_1
#Question_1_Average of three numbers entered by the user
number_1=int(input("Enter the first number  :"))
numbeer_2=int(input("Enter the second number :"))
number_3=int(input("Enter the third number :"))
print("The first number is :",number_1)
print("The second number is :",number_2)
print("The third number is :",number_3)
sum=number_1+number_2+number_3
avg=sum/3
print("The average of",number_1,",",num ber_2,"and",number_3,"is",avg)

#Question_2_Calculation of a person's income tax
tax_rate=20
print("Tax Rate is : ", tax_rate)
std_deduxn=10000
print("Standard Deduction is : ", std_deduxn)
dep_deduxn=3000
print("Additional Dependent Deduction is :",dep_deduxn)
gross_income=float(input("Enter Gross Income :"))
dependent_no=int(input("Enter the Number of Dependents :"))
taxable_income=gross_income-std_deduxn-(dep_deduxn*dependent_no)
print("Taxable Income is :",taxable_income)
tax=taxable_income*tax_rate
print("Income Tax is  :",tax)

#Ques_3_Storage of different datatype values in a list
print("Student=[ SID , Name , Gender , Department , CGPA ]"
Student=[21103004 , "Aryaveer" , "M" , "CSE" , 7.9]
print("The student list is" ,Student)

#Ques_4_Entry and display of marks of five students into a list in a sorted manner
print("Marks of five students are :")
Marks=[ 88 , 90 , 86 , 89 , 79 ]
print("List of marks before sorting is :" ,Marks)
Marks.sort()
print("List of marks after sorting is :" ,Marks)

#Ques_5_(a)Removal of fourth element i.e. Black(index=3)
Colour=[ "Red" , "Green" , "White" , "Black" , "Pink" , "Yellow" ]
print("Colour list is :" , Colour)
Colour.pop(3)
print(" List of colours after removing the fourth element is :" ,Colour)
#Ques_5_(b)Replacement of Black and Pink by Purple
Colour2=[ "Red" , "Green" , "White" , "Black" , "Pink" , "Yellow" ]
Colour2[ 3:5 ] = ["Purple"]
print(" List of colours after replacing Black and Pink by Purplr is :" ,Colour2)