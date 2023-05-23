print('Welcome to the BMI calculator 2.0!')
height=float(input('your height is(m): '))
weight=float(input('your weight is(kg): '))

BMI=weight/(height**2)

if BMI<18.5:
    print('your are underweight')
elif 18.5<=BMI<25:
    print('you are normal weight')
elif 25<=BMI<30:
    print('you are overweight')
elif 30<=BMI<35:
    print('you are obese')
else:
    print('you are clinically obese!')