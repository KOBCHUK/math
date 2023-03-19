
num = int(input('num = ')) 
number_1 = int(num/1000)
number_2 = int(num/100)%10
number_3 = int(num/10)%10
number_4 = int(num%10)
result_number = (number_4*1000)+(number_3*100)+(number_2*10)+number_1
print(f'result = {result_number}')




