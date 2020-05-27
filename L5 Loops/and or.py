type = input("Are you a student, staff or parent? ")

if type == "student":
    grade = int(input("What is your grade? "))
    if grade >= 90 and grade < 100:
        print("You are a good student!")
    elif grade > 100:
        print("Your grade must be less than 100.")
    else:
        print("You have the potential to be a good student!")
else:
    print("You are not a student!")
