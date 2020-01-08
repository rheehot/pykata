def prime_number_generator(start, stop):
    for i in range(start, stop + 1):
        if check_prime_number(i):
            yield i



def check_prime_number(number):
    sqrt_number = int(number ** 1/2)
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    return True


g = prime_number_generator(50, 100)
print(type(g))
for i in g:
    print(i)

