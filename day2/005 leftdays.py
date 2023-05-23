age=int(input('input your ages: '))
# input会把输入的内容默认为strings，所以需要int先转化为整数再进行下面的计算
ly=90-age
lm=ly*52
ld=ly*365

print(f"you has {ld} days, {lm} months and {ly} years left")
