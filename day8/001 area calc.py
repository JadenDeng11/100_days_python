import math
test_h=float(input("height of the wall: \n"))
test_w=float(input("width of the wall: \n"))
coverage=5

def area_clac(height,width):
    num01=(height*width)/coverage
    num02=math.ceil(num01)
    # math.ceil向上取整，to the ceiling
    num03=int(num02)
    print(f"the number of cans you should buy is: {num03}")

area_clac(height=test_h,width=test_w)