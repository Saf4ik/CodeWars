# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


def primeFactors(n):
    divider = 2
    form = {}
    while n > 1:
        if n % divider == 0:
            n = int(n / divider)
            if divider in form:
                form[divider] += 1
            else:
                form[divider] = 1
        else:
            divider += 1
    s = ""
    for k,v in form.items():
        if v > 1:
            s += "".join(f'({str(k)}**{str(v)})')
        else:
            s += "".join(f'({str(k)})')
    return s

