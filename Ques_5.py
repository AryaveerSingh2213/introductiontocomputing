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