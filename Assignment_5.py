# Assignment_5                                                                                                           
                                                                                                                         
# Question_1 : WAPP to make a GUI based GST Tax Finder Calculator which takes original cost and net price as an input    
# from the user and display the GST result                                                                               
from tkinter import *                                                                                                    
                                                                                                                         
                                                                                                                         
# created a function to calculate the tax by acquiring the values using .get()                                           
def get_vals():                                                                                                          
    tax = (int(Net_price.get()) - int(Original_cost.get())) * 100 / int(Original_cost.get())                             
    print("The tax is", tax)                                                                                             
    return tax                                                                                                           
                                                                                                                         
                                                                                                                         
win = Tk()                                                                                                               
win.title("GST Tax Finder Calculator")                                                                                   
win.geometry('400x400')                                                                                                  
# Labels                                                                                                                 
lbl = Label(win, text="Tax Calculator")                                                                                  
lbl.pack()                                                                                                               
lbl1 = Label(win, text="Net Price:")                                                                                     
lbl1.place(x=50, y=50)                                                                                                   
lbl2 = Label(win, text="Original Cost:")                                                                                 
lbl2.place(x=50, y=110)                                                                                                  
                                                                                                                         
Net_price = StringVar()                                                                                                  
Original_cost = StringVar()                                                                                              
# Entries                                                                                                                
en1 = Entry(win, textvariable=Net_price)                                                                                 
en1.place(x=177, y=57)                                                                                                   
en2 = Entry(win, textvariable=Original_cost)                                                                             
en2.place(x=177, y=117)                                                                                                  
# Button                                                                                                                 
Button(text="Submit", command=get_vals).place(x=170, y=170)                                                              
win.mainloop()                                                                                                           
                                                                                                                         
# Question_2 :WAPP to create a GUI based Calendar using Tkinter module that displays the calendar w.r.t. the year        
# entered by the user                                                                                                    
                                                                                                                         
from tkinter import *                                                                                                    
import calendar                                                                                                          
                                                                                                                         
                                                                                                                         
def show_calendar():                                                                                                     
    win_2 = Tk()                                                                                                         
    win_2.config(background="white")                                                                                     
    win_2.title("Calendar")                                                                                              
    win_2.geometry("500x500")                                                                                            
                                                                                                                         
    year = int(year1.get())                                                                                              
    cal_co = calendar.calendar(year)                                                                                     
    cal_year = Label(win_2, text=cal_co).grid(row=5, column=1, padx=20)                                                  
                                                                                                                         
    win_2.mainloop()                                                                                                     
                                                                                                                         
                                                                                                                         
win = Tk()                                                                                                               
win.geometry("600x300")                                                                                                  
win.title("Calendar")                                                                                                    
# Label                                                                                                                  
lbl = Label(win, text="Calendar", bg="dark green", fg="white").pack()                                                    
lbl1 = Label(win, text="Enter an Year").place(x=250, y=75)                                                               
# Entry                                                                                                                  
year1 = StringVar()                                                                                                      
en1 = Entry(win, textvariable=year1).place(x=200, y=100)                                                                 
# Button                                                                                                                 
button = Button(win, text="Submit", command=show_calendar).place(x=257, y=137)                                           
win.mainloop()                                                                                                           
                                                                                                                         
# Question_3 : WAPP to create a GUI based calculator using Tkinter module which can perform basic arithmetic operations  
                                                                                                                         
from tkinter import *                                                                                                    
                                                                                                                         
root = Tk()                                                                                                              
root.title("Calculator")                                                                                                 
root.geometry("600x400")                                                                                                 
                                                                                                                         
                                                                                                                         
def sum_vals():                                                                                                          
    print("The sum of the two numbers is:", int(Number_1.get()) + int(Number_2.get()))                                   
                                                                                                                         
                                                                                                                         
def multiply_vals():                                                                                                     
    print("The product of the two numbers is:", int(Number_1.get()) * int(Number_2.get()))                               
                                                                                                                         
                                                                                                                         
def subtract_vals():                                                                                                     
    print("The difference of the two numbers is-", int(Number_1.get()) - int(Number_2.get()))                            
                                                                                                                         
                                                                                                                         
def divide_vals():                                                                                                       
    print("The division of the two numbers is:", int(Number_1.get()) / int(Number_2.get()))                              
                                                                                                                         
                                                                                                                         
# Labels                                                                                                                 
lbl11 = Label(root, text=" Basic Calculator").place(x=180, y=10)                                                         
lbl22 = Label(root, text="Enter the numbers, then select the operation").place(x=110, y=50)                              
lbl1 = Label(root, text="Number 1:").place(x=110, y=110)                                                                 
lbl2 = Label(root, text="Number 2:").place(x=110, y=170)                                                                 
# Entries                                                                                                                
Number_1 = StringVar()                                                                                                   
Number_2 = StringVar()                                                                                                   
en1 = Entry(root, textvariable=Number_1).place(x=180, y=110)                                                             
en2 = Entry(root, textvariable=Number_2).place(x=180, y=170)                                                             
# Buttons                                                                                                                
sum_button = Button(root, text="+", command=sum_vals).place(x=150, y=240)                                                
multiply_button = Button(root, text="*", command=multiply_vals).place(x=210, y=240)                                      
subtract_button = Button(root, text="-", command=subtract_vals).place(x=270, y=240)                                      
division_button = Button(root, text="/", command=divide_vals).place(x=330, y=240)                                        
                                                                                                                         
root.mainloop()                                                                                                          
                                                                                                                         
                                                                                                                         
# Question_4 : WAPP to create a list of marks for n no. of students entered by the user. Sort the list using             
# merge/quick sort algorithm and print the final sorted list                                                             
                                                                                                                         
def quick_sort(arr):                                                                                                     
    less = []                                                                                                            
    equal = []                                                                                                           
    greater = []                                                                                                         
                                                                                                                         
    if len(arr) > 1:                                                                                                     
        pivot = arr[0]                                                                                                   
        for xx in arr:                                                                                                   
            if xx < pivot:                                                                                               
                less.append(xx)                                                                                          
            elif xx == pivot:                                                                                            
                equal.append(xx)                                                                                         
            elif xx > pivot:                                                                                             
                greater.append(xx)                                                                                       
                                                                                                                         
        return quick_sort(less) + equal + quick_sort(greater)                                                            
    else:                                                                                                                
        return arr                                                                                                       
                                                                                                                         
                                                                                                                         
k = 0                                                                                                                    
a = []                                                                                                                   
while k < 1:                                                                                                             
    marks = int(input("Enter the marks :"))                                                                              
    a.append(marks)                                                                                                      
    yes_no = input("Enter y to continue further or n to stop here :")                                                    
    if yes_no == 'n':                                                                                                    
        k = 1                                                                                                            
ar = quick_sort(a)                                                                                                       
print("The sorted array is :", ar)                                                                                       
                                                                                                                         
# Question_5 : WAPP to create an integer array containing duplicates entered by the user and then perform as directed:   
# (a) Sort the input array                                                                                               
                                                                                                                         
a = []                                                                                                                   
n = 0                                                                                                                    
                                                                                                                         
while n < 1:                                                                                                             
    x = int(input("Enter a number:"))                                                                                    
    a.append(x)                                                                                                          
    choice = input("Press y if you wish to add more elements to the array or n to stop here:")                           
    if choice == 'n':                                                                                                    
        n = 1                                                                                                            
                                                                                                                         
                                                                                                                         
# Using bubble sort                                                                                                      
def bubble_sort(arr):                                                                                                    
    z = len(arr)                                                                                                         
    while z > 0:                                                                                                         
        for i in range(len(arr) - 1):                                                                                    
            if arr[i] >= arr[i + 1]:                                                                                     
                temp = arr[i + 1]                                                                                        
                arr[i + 1] = arr[i]                                                                                      
                arr[i] = temp                                                                                            
            else:                                                                                                        
                continue                                                                                                 
        z -= 1                                                                                                           
                                                                                                                         
                                                                                                                         
bubble_sort(a)                                                                                                           
print(a)                                                                                                                 
print("The array has been successfully sorted")                                                                          
                                                                                                                         
# (b) Using binary search , search the element entered by the user                                                       
print("Now binary search:")                                                                                              
                                                                                                                         
                                                                                                                         
def binary_search(low, high, arr, b):                                                                                    
    while low <= high:                                                                                                   
        mid = (low + high) // 2                                                                                          
        if b > mid:                                                                                                      
            return binary_search(arr[mid + 1], high, arr, b)                                                             
        elif b < mid:                                                                                                    
            return binary_search(low, arr[mid - 1], arr, b)                                                              
        else:                                                                                                            
            return mid                                                                                                   
    return 0                                                                                                             
                                                                                                                         
                                                                                                                         
item = int(input("Enter the number to be searched :"))                                                                   
pos = binary_search(0, len(a) - 1, a, item)                                                                              
if pos == -1:                                                                                                            
    print("Error ! The entered number is not present in the array.")                                                     
else:                                                                                                                    
    print("The entered number has been found at", pos, "position.")                                                      
                                                                                                                         
# (c) Count the number of occurrences of that number.                                                                    
                                                                                                                         
count = 0                                                                                                                
for ii in a:                                                                                                             
    if ii == item:                                                                                                       
        count += 1                                                                                                       
    else:                                                                                                                
        continue                                                                                                         
print("The number", item, "has occurred", count, "time(s)")                                                              
                                                                                                                         