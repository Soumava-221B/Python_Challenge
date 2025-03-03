"""
Python Code Challenge #1: Find Prime Factors
Your goal is to implement a function, get_prime_factors(), that takes an integer value as the input argument and returns a list containing all of its prime factors.

Example Test Output
>>> get_prime_factors(630)
[2, 3, 3, 5, 7]
"""

def prime_factors(number):
    factors = []
    divisor = 2
    
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors

if __name__ == '__main__':
    print(prime_factors(630))  # [2, 3, 3, 5, 7]
    print(prime_factors(13))  # [13]