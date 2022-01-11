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