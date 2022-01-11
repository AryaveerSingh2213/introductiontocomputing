#Ques_3_Storage of different datatype values into a list
Name = input("Enter the name of the student : ")
SID = int(input("Enter the student I.D. : "))
Gender = input("Enter the gender of the student (F,M,U) : ")
Course = input("Enter the student's  course name : ")
CGPA = input("Enter the student's CGPA : ")
Student = [ "Name", "SID" , "Gender" , "Course" , "CGPA" ]
print(Student)
Student_info =[Name , SID , Gender , Course , CGPA]
print(" The list of the student's information is : " , Student_info)