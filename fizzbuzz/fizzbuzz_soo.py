# Soo's fizzbuzz 
###

for number in range(0,30):
    if number % 15 == 0:
        print('fizzbuzz')
    if number % 3 == 0:
        print('fizz')
    if number % 5 == 0:
        print('buzz')
    else:
        print(number)
