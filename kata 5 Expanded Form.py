# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    result = str()
    num = str(num)
    for i in range(len(num)):
        if num[i] != '0':
            result += f'{num[i] + "0"*(len(num)-1-i)} + '
    print(result[:-3])


expanded_form(70304)      #'70000 + 300 + 4'