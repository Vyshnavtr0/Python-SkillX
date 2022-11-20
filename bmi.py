n=int(input("Enter the number of students : "))
for i in range(n):
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    height=eval(input("Enter your height in metres : "))
    weight=eval(input("Enter your weight in kilograms : "))
    bmi=weight/(height**2)
    print("Yours BMI is :",bmi)
    if bmi <= 18.4:
        print("You are underweight.")
    elif bmi <= 24.9:
        print("You are healthy.")
    elif bmi <= 29.9:
        print("You are over weight.")
    elif bmi <= 34.9:
        print("You are severely over weight.")
    elif bmi <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")
    
