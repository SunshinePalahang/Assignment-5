def getgradePercentage():
    grade_percentage = input("Enter Grade Percentage: ")
    if grade_percentage == "INC":
        print(f"Description: Incomplete")
    elif grade_percentage == "W":
        print(f"Description: Withdrawn")
    elif grade_percentage == "D":
        print(f"Description: Dropped")
    else:
        roundUp = round(float(grade_percentage))
        if roundUp >= 97 and roundUp <= 100:
            print(f"Grade/Mark: 1.0 \nDescription: Excellent")
        elif roundUp >= 94 and roundUp <= 96:
            print(f"Grade/Mark: 1.25 \nDescription: Excellent")
        elif roundUp >= 91 and roundUp <= 93:
            print(f"Grade/Mark: 1.50 \nDescription: Very Good")
        elif roundUp >= 88 and roundUp <= 90:
            print(f"Grade/Mark: 1.75 \nDescription: Very Good")
        elif roundUp >= 85 and roundUp <= 87:
            print(f"Grade/Mark: 2.0 \nDescription: Good")
        elif roundUp >= 82 and roundUp <= 84:
            print(f"Grade/Mark: 2.25 \nDescription: Good")
        elif roundUp >= 79 and roundUp <= 81:
            print(f"Grade/Mark: 2.50 \nDescription: Satisfactory")
        elif roundUp >= 76 and roundUp <= 78:
            print(f"Grade/Mark: 2.75 \nDescription: Satisfactory")
        elif roundUp == 75:
            print(f"Grade/Mark: 3.0 \nDescription: Passing")
        else:
            print(f"Grade/Mark: 5.0 \nDescriptiion: Failure")

gradePercentage = getgradePercentage()
print("Done")

