"""days in month"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    # 定义方法一定要有参数
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days_02 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not is_leap(year):
        # 调用方法一定要有参数
        days = month_days[month-1]
        return days
    else:
        days = month_days_02[month-1]
        return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
