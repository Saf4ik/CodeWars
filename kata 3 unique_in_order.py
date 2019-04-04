# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(str):
    if len(str) == 0:
        return str
    res = [str[0]]
    for i in range(1,len(str)):
        if str[i] != str[i-1]:
            res.append(str[i])
    print(res)




unique_in_order('AAAABBBCCDAABBB')