# bmi calculator
# Get user input
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))
gender = input("Enter your gender (M/F):")
# Calculate BMI
bmi = weight/height*height
# determine age category
age = int(input("Enter your age :"))
if age <= 10:
    print("Category : children")
elif age <= 20:
    print("Category : Teenage")
else:
    print("Category : Adult")
# Determine BMI category
bmi_category = None
if bmi > 0:
    if bmi <= 16:
        print("Category : Severe thinners")
    elif bmi <= 17.5:
        print("Category : Moderate thinners")
    elif bmi <= 18.5:
        print("Category : Mild thinners")
    elif bmi <= 25:
        print("Category : Normal ")
    elif bmi <= 30:
        print("category : Over weight")
    else:
        print("Category  : Obese")
# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {bmi_category}")
