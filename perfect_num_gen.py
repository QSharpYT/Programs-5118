import math

def perfect_numbers(n):
    perfect_nums = []
    for num in range(2, n + 1):  # Start from 2 as 1 is not considered a perfect number
        if is_perfect(num):
            perfect_nums.append(num)
    return perfect_nums

def is_perfect(num):
    if num <= 1:
        return False
    
    sum_of_divisors = 1  # Start with 1 as it's always a divisor
    sqrt_num = int(math.sqrt(num))
    
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:  # Avoid adding the square root twice
                sum_of_divisors += num // i
    
    return sum_of_divisors == num

# Prompt the user to enter a number to generate perfect numbers up to
try:
    gener_betw = int(input("What number do you want to generate perfect numbers up to? "))
    if gener_betw < 2:
        print("Please enter a number greater than or equal to 2.")
    else:
        print(perfect_numbers(gener_betw))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
