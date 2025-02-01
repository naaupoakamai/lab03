is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = [2, 3, 4, 5, 10, 13, 17, 19, 23, 29, 30, 31, 37, 40]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)

