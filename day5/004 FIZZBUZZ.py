for number in range(1,101):
    if number%3==0:
        number='FIZZ'
        print(number)

    elif number%5==0:
        number='BUZZ'
        print(number)

    elif number%3==0 and number%5==0:
        number='FIZZBUZZ'
        print(number)

    else:
        print(number)
