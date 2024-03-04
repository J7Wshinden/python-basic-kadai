var=15

if var%3==0 & var%5!=0:
    print('Fizz')
elif var%5==0 & var%3!=0:
    print('Buzz')
elif var%15==0:
    print('FizzBuzz')
else:
    print(var)
