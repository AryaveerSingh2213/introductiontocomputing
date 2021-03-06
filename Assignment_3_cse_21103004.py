# PYTHON_ASSIGNMENT:3

# Ques_1:WAPP to count the no. of occurence of each word or character in the string entered by the user

String1 = input(" Enter any string :")
print(" The string entered by the user is :", String1)
List1 = []
List2 = String1.split()
x = len(List2)
y1 = dict()
y2 = dict()

if x == 1:                     #For string with a single word
    for i in String1:
        List1.append(i)
    for j in List1:            #All the unique characters get the value one, if it gets repeated, its value will be incremented by one
        if j in y1:
            y1[j] = y1[j]+1
        else:
            y1[j] = 1
    print(" The frequency of each character is :", y1)

else:                             #For string with multiple words
    for i in List2:               #All the unique words get the value one, if it gets repeated, its value will be incremented by one
        if i in y2:
            y2[i] = y2[i]+1
        else:
            y2[i] = 1
    print(" The frequency of each word is :", y2)

#Ques_2:WAPP to print next date of input date

Month = int(input("Enter month no.:"))


if Month in [1, 3, 5, 7, 8, 10, 12]:                       # Case for months with 31 days
    Day = int(input("Enter day: "))
    if(1 <= Day <= 31):
        Year = int(input("Enter year:"))
        if(1800 <= Year <= 2025):
            print(" Entered Date is :", Day, "/", Month, "/", Year)
            if(Month == 12 and Day == 31):
                print("Next Date is :", "1/1/", Year+1)
            elif(Day == 31):
                print("Next Date is:", "1/", Month+1, "/", Year)
            else:
                print("Next Date is:", Day+1, "/", Month, "/", Year)
        else:
            print(" You have entered an invalid year!")
    else:
         print(" You have entered an invalid date!")

elif Month in [4, 6, 9, 11]:                            # Case for months with 30 days
    Day = int(input("Enter day:"))
    if(1 <= Day <= 30):
        Year=int(input("Enter year:"))
        if(1800 <= Year <= 2025):
            print("Date-", Day,"/", Month, "/", Year)
            if(Day == 30):
                print("Next Date is :", "1/", Month+1, "/", Year)
            else:
                print("Next Date is :", Day+1, "/", Month, "/", Year)
        else:
            print(" You have entered an invalid year!")
    else:
         print(" you have entered an invalid date!")
elif(Month == 2):                                     # Special case for February
    Year = int(input("Enter year:"))
    if(1800 <= Year <= 2025):
        Day = int(input("Enter day:"))
        if(Year%4 == 0):
            if(1 <= Day <= 29):                                    # For leap year
                print("Entered Date is:", Day, "/", Month, "/", Year)
                if(Day==29):
                    print("Next Date is :", "1/", Month+1, "/", Year)
                else:
                    print("Next Date is :", Day+1, "/", Month, "/", Year)
            else:
                print(" You have entered an invalid day!")
        else:
            if(1 <= Day <= 28):                                     # For non-leap years
                print(" Entered Date is:", Day, "/", Month, "/", Year)
                if(Day == 28):
                    print("Next Date is:", "1/", Month+1, "/", Year)
                else:
                    print("Next Date is:", Day+1, "/", Month, "/", Year)
            else:
                print(" You have entered an invalid day!")
    else:
        print(" You have entered an invalid year!")
else:
    print(" You have entered an invalid month!")

#Ques_3:WAPP to create a list of tuples with first element as a no. and the second element as its square

List = []                                                        #creating empty list
n = int(input("Enter the number of elements :"))                 #taking number of elements as input
print("Enter the elements of the list :")

for i in range(0, n):                                            #iterating till the range
    ele = int(input())
    List.append(ele)

print("The entered list of numbers is :",List)
List_of_tuples = []
for x in List:
    List_of_tuples.append((x, x**2))
print(" The required list of tuples is :", List_of_tuples)

#Ques_4:WAPP to prompt the use for a grade between 4 and 10.Print their performance and letter grade accordingly.

Grade_Points = int(input("Enter your grade between 4 and 10 including them:"))    #4<=Grade_Points<=10

Performance = int
Letter_Grade = str

if(Grade_Points == 4):
    Performance = "Poor"
    Letter_Grade = "D"
elif(Grade_Points == 5):
    Performance = "Below Average"
    Letter_Grade = "C"
elif(Grade_Points == 6):
    Performance = "Average"
    Letter_Grade = "C+"
elif(Grade_Points == 7):
    Performance = "Good"
    Letter_Grade = "B"
elif(Grade_Points == 8):
    Performance = "Very Good"
    Letter_Grade = "B+"
elif(Grade_Points == 9):
    Performance = "Excellent"
    Letter_Grade = "A"
elif(Grade_Points == 10):
    Performance = "Outstanding"
    Letter_Grade = "A+"
else:
    print("Error:The grade point entered by you is out of range!")
print(" Your Performance is: ", Performance)
print(" Letter Grade is:", Letter_Grade)

#Ques_5:WAPP to print the following pattern
#ABCDEFGHIJK
 #ABCDEFGHI
  #ABCDEFG
   #ABCDE
    #ABC
     #A

Alpha = "ABCDEFGHIJK"
count = 1
print("The required pattern is :")
while(count < 7):
    print(" "*(count-1), Alpha[0:11-((count-1)*2)])      #leaves (count-1) times space" " and prints Alpha ( deletes last two letters ),for count=count+1
    count = count + 1

#Ques_6:WAPP that asks repeatedly the user to enter name and SID of students and perform tasks as given

Student = dict()           #creating an empty dictionary
Choice = "y"               #default value
List_sid = []              #creating an empty list

# (a) Print student details stored in the dictionary

print("(a):Printing student details stored in the dictionary ")

while(Choice == "y"):                               #entering student SIDs as keys and student names as values till choice==y
    SID = int(input("Enter SID of a student:"))
    Name = input("Enter the name of the student:")
    Student[SID] = Name
    Choice = input("Do you want to enter more SIDs and Names ? ('y' or 'n'):")
    List_sid.append((SID, Name))                                                 #to be used later

print("The entered dictionary is :", Student)
print("The entered list of SIDs is :", List_sid)

#(b) Sort dictionary using student names

print("(b):Sorting dictionary using student names")

print("The dictionary we have is :", Student)

#Exchanging the key-value pair and making a new dictionary and a new list

Student_new = dict()
List_name = []

for (key, val) in Student.items():
    Student_new[val] = key
    List_name.append((val, key))

print("Exchanging the key-value pair , we get :", Student_new)
print("The unsorted list of names is :", List_name)

List_name.sort()
print("The list of name after sorting (alphabetically) is :", List_name)

#Creating a sorted dictionary from our sorted list of names

print("The sorted dictionary is :")
Sorted_Student = dict(List_name)
print(Sorted_Student)

#Exchanging the key value pair of the sorted_dict to get the required dictionary

Required_Student_names = dict()

for (key, val) in Sorted_Student.items():
    Required_Student_names[val] = key

print(" The dictionary sorted on the basis of names is :", Required_Student_names)

#(c) Sort dictionary using student SIDs

print("(c):Sorting dictionary using student SIDs ")

print("The list of SIDs is :", List_sid)
List_sid.sort()
print("The sorted list is :", List_sid)

Sorted_Student_SIDs = dict(List_sid)

print("The dictionary sorted on the basis of SIDs is:", Sorted_Student_SIDs)

#(d) Search a student's name using  SID

print("(d) Searching a students's name using SID")

Input_SID = int(input(" Enter one of the SIDs you entered before:"))
print("The name of the student with the SID ", Input_SID, " is:", Student[Input_SID])

#Ques_7:WAPP to print Fibonacci Sequence .Also print average of the resultant Fibonacci Series

Term1 = int(input("Enter the first term :"))
Term2 = int(input("Enter the second term :"))

#It will keep on printing the sequence till you say y and to stop it when you say n
um = Term1+Term2
Sequence = [Term1, Term2]
choice = "y"                    #default value

while(choice == "y"):
    Sequence.append(Sequence[len(Sequence)-1]+Sequence[len(Sequence)-2])
    print(Sequence)
    choice=input(" Enter y to continue or n to stop here :")

print("The list having a Fibonacci Series is :",Sequence)

#Average of the resultant fibonacci series
Sum = 0

for i in Sequence:
    Sum = Sum+i
print("Average of the resultant Fibonacci series is :")
print(Sum/len(Sequence))


#Ques_8:DO as Directed

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

print("Set1=", Set1)
print("Set2=", Set2)
print("Set3=", Set3)

#(a):Create anew set of all elements that are in Set1 and Set2 but not in both

print("(a)-------------------------")
Set_A = Set1 ^ Set2
print("Set1^Set2=", Set_A)

#(b):Create a new set of all elements that are only in one of the three sets Set1, Set2 and Set3

print("(b)-------------------------")
Set_B = Set1 ^ (Set2 ^ Set3)
print("Set1^(Set2^Set3)=", Set_B)

#(c):Create a new set of elements that are exactly two of the Set1 ,Set2 and Set3

print("(c)-------------------------")
Set_C = (Set1 & Set2) | (Set2 & Set3) | (Set1 & Set3)
print("(Set1&Set2)|(Set2&Set3)|(Set1&Set3)=", Set_C)

#(d):Create a new set of all integers in the range 1 to 10 that are not in Set1

print("(d)-------------------------")
Set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Set_D = Set4-Set1
print("Set4-Set1=", Set_D)

#(e):Create a new set of all integers in the range 1 to 10 that are not in Set1 ,Set2 and Set3

print("(e)-------------------------")
Set_E = Set4-(Set1 | Set2 | Set3)
print("Set4-(Set1|Set2|Set3)=", Set_E)

print("----------END OF CODE----------")
