"""
fizzbuzz

Write a python script which prints the numbers from 1 to 100,
but for multiples of 3 print "fizz" instead of the number,
for multiples of 5 print "buzz" instead of the number,
and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.
"""

for i in range(1,101):
    str = ""
    if i % 3 == 0:
        str = str + "fizz"
    if i % 5 == 0:
        str = str + "buzz"
    if str == "":
        print(i)
    else:
        print(str)
