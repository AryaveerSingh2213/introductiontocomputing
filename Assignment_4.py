# Assignment_4 :

#Ques_1 : Write  recursive pyhton function to solve the problem of tower of Hanoi with three disks.

def Tower_Of_Hanoi(n, Source_rod, Middle_rod, Dest_rod):       #function definition
    if n > 0:
        Tower_Of_Hanoi(n - 1, Source_rod, Dest_rod, Middle_rod)
        print(" Transferring Disk ", n, "from rod", Source_rod, "to rod", Dest_rod)
        Tower_Of_Hanoi(n - 1, Middle_rod, Source_rod, Dest_rod)

Tower_Of_Hanoi(3, "A", "B", "C")                #function invoking

#Ques_2 : WAPP to print the Pascal's triangle for 'n' no. of rows given by the user both recursive and iterative procedures.

#using iterative procedure

print("Using iteration......")

# making factorial function

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# making nCr function

def nCr(n, r):
    ncr = fact(n) / (fact(n - r) * fact(r))
    return int(ncr)

row = int(input(" Enter the number of rows :"))
i = 1
while i <= row:
    print(" " * (row - i), end="")
    j = 0
    while j < i:
        print(nCr(i - 1, j), " ", end="")
        j += 1
    print("\n")
    i += 1

# using recursive procedure

print("Using recursion......")

def Pascals_triangle(n, s, m):
    if n == 0:
        print(" " * (s - 1), 1, "\n")

        return Pascals_triangle(n + 1, s, m)
    elif n == m:
        print("Done!")
        n = -1

    else:
        print(" " * (s - n), end="")
        x = 0
        while x <= n:
            print(nCr(n, x), "", end="")
            x += 1
        print("\n")
        if n == m:
            print("Done!")
            n = -2
        return Pascals_triangle(n + 1, s, m)

m=int(input(" Enter the number of rows :"))
n=m-m
s=m+m
Pascals_triangle(n, s, m)


#Ques_3 : Input two integer values from user ,calculate and print the quotient and remainder. Now do as directed:

def divide(a, b):                        #function definition
    quotient = a // b
    remainder = a % b

    print("The quotient is :", quotient)
    print("The remainder is :", remainder)
    Result = [quotient, remainder]
    return Result

#(a) : Check whether it(function/value) is callable or not.

x = int(input("Enter the first number :"))
y = int(input("enter the second number :"))

Result = divide(x, y)                     #function calling
print(" The resulting list is :", Result)
print(" The function is callable :", callable(divide))

#(b) : Check whether all the values are non zeroes or not.

print(" The first number is zero:", x == 0)
print(" The second number is zero:", y == 0)
print(" The quotient is zero :", Result[0] == 0)
print(" The remainder is zero :", Result[1] == 0)

#(c) : Add values (4 ,5 ,6) to the result and filter out the values which are greater than 4.

val = [4, 5, 6]
Result = Result + val
print(" Adding (4, 5, 6) to the resulting list , we have : ", Result)
List = []
for i in Result:
    if i > 4:
        List.append(i)
print("The values greater than four are :", List)

#(d) : Convert the above result into set datatype.

Set = set(List)
print(" Converting the resulting list into a set ,we have : ", Set)

#(e) : Make the set immutable.

immutable_set = frozenset(Set)
print(" The required immutable set is :", immutable_set)

#(f) : Evaluate the maximum value from set and find out its hash value.

max = 0
for i in immutable_set:
    if i > max:
        max = i

print("The required maximum value is :", max)
print("The required hash value is :", hash(max))

#Ques_4 : Create a class Student,use the _init_() function to assign values for name and roll no.Also call _del_() function to destroy the created object.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __del__(self):
        print("Destructor called,thus the object so created is destroyed.")

p1 = Student("Stuart", 22)
print("Student's name is :", p1.name)
print("Student's roll no. is :", p1.roll_no)

#Ques_5 : WAPP to store details of three employees : name amd salary using class.

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

p1 = Employees("Mehak", 40000)
p2 = Employees("Ashok", 50000)
p3 = Employees("Viren", 60000)

print(p1.name, "earns INR", p1.salary)
print(p2.name, "earns INR", p2.salary)
print(p3.name, "earns INR", p3.salary)

#(a) : Update the salary of Mehak to 70000.

p1.salary = 70000                                          # updating salary of Mehak to 70000
print("The updated salary of Mehak is : ", p1.salary)

#(b) : Delate the record of employee Viren.

del p1                                                               # deleting the record of Viren
print("The record of Viren has been deleted successfully.")

#Ques_6 : WAPP to create a new meaningful word using exact same letters from the input word .

def anagram(word):                                   #function definition
    if len(word) == 1:
        return [word]
    partial_words = anagram(word[1:])
    char = word[0]
    result = []
    for perm in partial_words:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result

George_word = input(" Enter George's word :")
Possible_words = anagram(George_word)                  #function calling
Barbie_word = input(" Enter Barbie's word :")

print("All the possible words are :", Possible_words)
print("If Barbie's word is present among all possible words, then their friendship is real.")

if Barbie_word in Possible_words:
    a = "REAL"
    b = "are"
else:
    a = "FAKE"
    b = "ain't"

print(" Their friendship is", a, "! So they", b, "real friends .")
