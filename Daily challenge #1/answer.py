__author__ = 'Bnizzle'


def return_binary(n):
    return '{0:08b}'.format(n)


def make_opposite(n, t):
    for num in n:
        if num == 1:
            opposite1.append(int(0))
        else:
            opposite1.append(int(1))

    for num in t:
        if num == 1:
            opposite2.append(int(0))
        else:
            opposite2.append(int(1))


response1 = int(input("Please enter the first number: "))
response2 = int(input("Please enter the second number:"))
a = return_binary(response1)
b = return_binary(response2)
i = 0
com = 0
array1 = []
array2 = []
opposite1 = []
opposite2 = []
count = 0
total = 8

for digit in a:
    array1.append(int(digit))
print array1
for digit in b:
    array2.append(int(digit))
print array2

while i != 8:
    if array1[i] == array2[i]:
         count += 1
    i += 1
per = float(count) / total * 100

make_opposite(array1, array2)

opposite_num1 = int(''.join(map(str, opposite1)))
opposite_num2 = int(''.join(map(str, opposite2)))

opp1 = (int(str(opposite_num1), 2))
opp2 = (int(str(opposite_num2), 2))

'''
    50% Compatibility
    100 should avoid 155
    42 should avoid 213
'''

print ('%r%% Compatibility' % per)
print response1, 'should avoid', opp1
print response2, 'should avoid', opp2