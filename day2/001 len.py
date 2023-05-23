num=len(input('What is your name'))

new_num=str(num)

print('your name has '+ new_num +' characters')

# 字符串不能和数组等相加，必须都先转化为数组。但如果用,取代+就不需要转化为字符串
# 比如 print('your name has ',num ,' characters')，这样就不需要前面的str函数