height=float(input('input your height(m)'))
weight=float(input('input your weight(kg)'))

BMI=weight/(height**2)

print(round(BMI,2))
# 四舍五入到两位小数（round the number），如果不四舍五入直接取整，把round改成int。
