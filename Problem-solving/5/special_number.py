def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def display_primes(num):
    primes = []
    for i in range(2, num):
        if is_prime(i):
            primes.append(i)
    return primes

# Get the input number
num = int(input("Enter a number greater than 100: "))

# Display the prime numbers
primes = display_primes(num)
for prime in primes:
    print(prime, end=', ')