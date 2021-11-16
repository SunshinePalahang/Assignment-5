#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good
def getgradePercentage():
    grade_percentage = input("Enter Grade Percentage: ")
    if grade_percentage == "INC":
        print(f"Description: Incomplete")
    elif grade_percentage == "W":
        print(f"Description: Withdrawn")
    elif grade_percentage == "D":
        print(f"Description: Dropped")
    


gradePercentage = getgradePercentage()


#step 1: ask for the grade percentage

