import random
names=input("Give me everybody's name, seperated by a comma: ")


names_list=names.split(", ")
# split可以将input里的内容去除", "后输出为一个list


names_pay=random.choice(names_list)
print(names_pay)