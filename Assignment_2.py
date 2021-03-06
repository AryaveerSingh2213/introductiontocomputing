#Assignment_2
#Question_1_Do as directed:

string_1  ="Python is a case sensitive language"
print( "The given string is :" , string_1)

#(a)_find the length of the given input string
print( " The length of the string is : " , len(string_1))

#(b)_reverse the order of the given input string
print( " The string in reverse order is : " , string_1[-1::-1])

#(c)_storing "a case sensitive " in a new string
string_2= string_1[10:26]
print( " The required new string is : " , string_2)

#(d)_replace "a case sensitive" with "object oriented"
string_3 = string_1.replace("a case sensitive","object oriented")
print( " The altered string is :" , string_3)

#(e)_find index of substring "a" in the given input string
string_4 = string_1.find("a")
print( " The index of substring is :", string_4)

#(f)_remove the white spaces from the given input string
string_5 = string_1.replace(" " , "")
print( " The string after removing the white spaces is :" , string_5)

#Question_2

Name =input( " Enter your name : ")
SID =input( " Enter your SID : ")
Deptt =input( " Enter your department : ")
CGPA =input( " Enter your CGPA : ")

Letter = " Hey , ABC Here.\n" \
               "My SID is PQR.\n" \
               " I am from XYZ department and my CGPA is LMN .\n"

Letter = Letter.replace( "ABC" , Name )
Letter = Letter.replace( "PQR" , SID )
Letter = Letter.replace( "XYZ" , Deptt )
Letter = Letter.replace( "LMN" , CGPA )
print ( Letter )

#Question_3_calculate the following :

a=56
# 56=(111000)2
b=10
# 10=(1010)2
print( "a =", a )
print( "b =", b )

#(a)_calculate a&b
c = a&b
# & = bitwise AND operator
# c=a&b=56&10 = (111000)2 & (1010)2 = (001000)2 =8
print( " a&b = " , c)

#(b)_calculate a|b
d = a|b
# | = bitwise OR operator
# d=a|b=56|10 = (111000)2 | (1010)2 = (111010)2 = 58
print( " a|b = " , d)

 #(c)_calculate a^b
e = a^b
# ^ = bitwise XOR operator
# e=a^b=56^10 = (111000)2 ^ (1010)2 = (110010)2 =50
print( " a^b = " , e )

#(d)_left shift both a and b with 2 bits
ls_a = a<<2
# a<<2=(111000)2 <<2 = (11100000)2 = 224
print( "The value of a after  left shifting with 2 bits is :" , ls_a)
ls_b = b<<2
# b<<2=(1010)2 <<2 = (101000)2 = 40
print( "The value of b after left shifting with 2 bits is :" , ls_b)

#(e)_right shift a with 2 bits and b with 4bits
rs_a = a>>2
# a>>2=(111000)2 >>2 = (001110)2 = 14
print( "The value of a after right shifting with 2 bits is :" , rs_a)
rs_b = b>>4
# b>>4=(1010)2 >>4 = (0000)2 =0
print( "The value of b after right shifting with 4 bits is :" , rs_b)

#Question_4_WAPP to find the greatest of three numbers entered by the user

Num_1 = int(input( "Enter the first number :"))
Num_2 = int(input( "Enter the second number :"))
Num_3 = int(input( "Enter the third number :"))

if  Num_1>=Num_2 and Num_1>=Num_3 :
   Grt_num = Num_1
elif  Num_2>=Num_1 and Num_2>=Num_3 :
   Grt_num = Num_2
else :
   Grt_num = Num_3

print( " The greatest number is :" , Grt_num )

#Question_5_WAPP to check if  the word "name" is present in the string entered by the user

String = input( " Enter any string : " )
print(" The entered string is :" , String)

#check if the word "name" is present in the entered string using the "in" operator
result = "name" in String            # The "in" operator returns either True or False
if result==True :
    print(" YES , the word 'name' is present in the entered string. ")
else :
    print(" NO , the word 'name' is not present in the entered string")

#Question_6_WAPP to check if whether three input lengths can form a triangle or not

A = int(input( " Enter the length of first side : "))
B = int(input( " Enter the length of second side : "))
C = int(input( " Enter the lemgth of third side : "))

if  A>=B+C :
    print( "NO , line segments of entered lengths can't form a triangle.")
elif  B>=C+A :
    print( "NO , line segments of entered lengths can't form a triangle.")
elif  C>=A+B :
    print( "NO , line segments of entered lengths can't form a triangle.")
else :
    print( "YES , line segments of entered lengths can form a triangle.")
