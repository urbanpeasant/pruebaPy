#https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
def expanded_form(num):
    list = []
    i = len(str(num)) -1
    for n in str(num):
        if n != "0":
            list.append(n + "0" * i)
        i -= 1
    return " + ".join(list)
print(expanded_form(89005))















'''
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

nota: All numbers will be whole numbers greater than 0.
'''



