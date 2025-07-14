
print("Welcome to myGrader space!")
print("--" * 30)
grade = float(input("Enter your grade: "))


if grade >=90 and grade <=100:
    print("You got an A, you passed!")
elif grade >=80 and grade <90:
    print("You got a B, you passed!")
elif grade >=70 and grade <80:
    print("You got a C, you passed!")
elif grade >=60 and grade <70:
    print("You got a D, you failed!")
elif grade >=0 and grade <60:
    print("You got an F, you failed!")
else:
     print("Unrecognized score, please try again!")
