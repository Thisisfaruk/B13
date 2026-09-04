#Problem 1: Student Grade Calculator

name = input("Enter your name: ")
sub1 = int (input ("Enter Sub1 Marks :"))
sub2 = int (input ("Enter Sub2 Marks :"))
sub3 = int (input ("Enter Sub3 Marks :"))

total = sub1 + sub2 + sub3
avg = total / 3

print (f"Student Name: {name}, Total Marks: {total}, Average Marks: {avg:.2f}")

if avg >= 80:
    print ("A+")
elif avg>=70:
    print ("A")
elif avg >= 60:
    print ("B")
elif avg>=50:
    print("C")
else:
    print ("Fail")