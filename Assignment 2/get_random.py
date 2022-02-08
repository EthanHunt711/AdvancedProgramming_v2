from random import randint
"""The lists are identical in size and range of the numbers but since the numbers are randomly 
selected it is possible that the target value might appear in one and not the other(s)"""

l_1 = []
# after 994 the maximum recursion limit is reached.
# changing the limit is possible but not makes no difference in this case.
for i in range(0, 100):
    n = randint(1, 100000)
    l_1.append(n)

l_2 = []
for i in range(0, 400):
    n = randint(1, 100000)
    l_2.append(n)

l_3 = []
for i in range(0, 600):
    n = randint(1, 100000)
    l_3.append(n)

l_4 = []
for i in range(0, 800):
    n = randint(1, 100000)
    l_4.append(n)

l_5 = []
for i in range(0, 994):
    n = randint(1, 100000)
    l_5.append(n)

lists = [l_1, l_2, l_3, l_4, l_5]
