cars = ['ok', 'ok', 'ok', 'ok', 'faulty', 'ok', ]

#break
#continue
#else in loops
for car_status in cars:
    if car_status == 'faulty':
        print('faulty')
        continue
    print(f'This car is {car_status}')

for num in range(2, 10):
    if num % 2 == 0:
        print('even')
        continue
    print('uneven')

for num in range(2, 1000):
    for x in range(2, num):
        if num % x == 0:
            break
    #else will only run if loop never breaks
    else:
        print(f'prime {num}')
