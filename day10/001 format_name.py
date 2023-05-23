f_name = input('your first name \n')
l_name = input('your last name \n')
def format_name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

output = format_name(f_name,l_name)
print(output)
