#wap to take input of marks and display grade

marks = int(input("Enter marks : "))

if(marks<=100 and marks>=90) :
    print("Grade A")
elif (marks<90 and marks>=80) :
    print("Grade B")
elif (marks<80 and marks>=70) :
    print("Grade C")
else :
    print("Grade D")