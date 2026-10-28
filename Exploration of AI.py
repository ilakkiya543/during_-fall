name=input("Enter Student name:")
n=int(input("Enter number of subject:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject {i}: "))
    total+=mark
    percentage= total/n
if percentage>=90:
    performance="Outstanding"
    grade="A"
elif percentage>=80:
    performance =" Excellent"
    grade="B"
elif percentage >=70:
     performance=  "Very Good"
     grade='C' 
elif percentage >=60:
    performance="Good"
    grade="D"

elif percentage >=50:
    performance="Average"
    grade="E" 
else:
    grade="F"
    performance=" Needs Improvement"
    print("\n ---Academic performance---")
    print("student name:",name)
    print("total mark:",total)
    print("percentage:",round(percentage,2),"%")
    print("Grade:",grade)
    print("Performance:",performance)            

