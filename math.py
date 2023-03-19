
number = int(input('number = '))
num_1 = int(number/1000)
num_2 = int((number/100)%10)
num_3 = int((number/10)%10)
num_4 = int(number%10)
mult = num_1*num_2*num_3*num_4
print(mult)

