num = 1124
copy = num
sum = 0
product = 1

while(num>0):
    print(num)
    last_digit = num % 10
    num = num // 10
    sum = sum + last_digit
    product = product * last_digit
    
if(sum == product):
    print(f"{copy} is a spy number")
else:
    print(f"{copy} is not a spy number")
    


