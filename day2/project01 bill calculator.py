print('Welcome to the bill calculator!')
bill=float(input('What is the totall bill? '))
Ptip=float(input('What percentage tips do you want to give?,10,12 or 15? '))
people=float(input('How many people to split the bill? '))

Ttip=bill*(Ptip/100)
Tbill=bill+Ttip
each_pay=Tbill/people

print(f"Each people should pay: {round(each_pay,2)}")