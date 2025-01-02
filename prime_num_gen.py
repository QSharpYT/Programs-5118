from __future__ import print_function
import sys

def generate_primes(limit):
    try:
        # Validate input
        if not isinstance(limit, int) or limit < 2:
            raise ValueError("Limit must be an integer greater than or equal to 2")

        # Initialize the sieve array
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False

        # Implement the Sieve of Eratosthenes
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, limit + 1, i):
                    sieve[j] = False

        # Generate the list of primes
        primes = [num for num in range(2, limit + 1) if sieve[num]]
        return primes

    except MemoryError:
        print("Error: Not enough memory to generate primes up to this limit.")
        return None
    except Exception as e:
        print("An unexpected error occurred: {0}".format(str(e)))
        return None

def main():
    try:
        if sys.version_info[0] < 3:
            limit = int(raw_input("Generate Primes up to: "))
        else:
            limit = int(input("Generate Primes up to: "))
        
        primes = generate_primes(limit)
        
        if primes is not None:
            print("Primes up to {0}: {1}".format(limit, primes))
    
    except ValueError as ve:
        print("Invalid input: {0}".format(str(ve)))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print("An unexpected error occurred: {0}".format(str(e)))
    finally:
        print("Program execution completed.")

if __name__ == "__main__":
    main()
