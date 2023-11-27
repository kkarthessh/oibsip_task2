def calculate_bmi(weight,height):
    bmi=weight/height*height
    return bmi
def classify_bmi(bmi):
    if bmi<18.5:
        print("Category : Under Weight")
    elif bmi<=18.5 and bmi>25:
        print("Category : Normal Weight")
    elif bmi<=25 and bmi>30:
        print("Category : Over Weight")
    else:
        print("Category : Obese")
def main():
    try:
        weight=float(input("enter the weight in kilogram:"))
        height=float(input("enter the height in meter:"))
        age=int(input("enter the age:"))
        gender=input("enter the gender Type:")
        if weight<=0 or height<=0:
            print("Invalid input??,enter the positive value!!")
        else:
            bmi=calculate_bmi(weight,height)
            category=classify_bmi(bmi)
            print(f"\n your bmi is : {bmi:.2f}")
    except ValueError:
        print("Invalid input??,please enter the numeric value!!")
if __name__=="__main__":
    main()