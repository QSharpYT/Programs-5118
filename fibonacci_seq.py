def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage
try:
    num_terms = int(input("Enter how many numbers you want: "))
    print(fibonacci(num_terms))
except NameError:
    print("Please enter a valid number")
finally:
    print("Program executed successfully")