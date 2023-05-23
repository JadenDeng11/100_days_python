sum01=0
# range后面的括号内的内容意思是从1循环到101-1也就是100，间隔'step'为2
for num in range(0,101,2):
    sum01+=num
print(sum01)

sum02=0
for num in range(0,101):
    if num%2==0:
        sum02+=num
print(sum02)