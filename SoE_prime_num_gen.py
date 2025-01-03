def Sieve_of_Eratosthenes(n):
    #Makes lists for the prime numbers, the composite numbers, and the numbers not sorted yet
    notSorted = []
    notPrimes = []  #Also known as composite numbers
    primes = []
    p = 2  #Making the smallest prime to find multiples later in the code
    for i in range(2,n+1):
        notSorted.append(i)
    for p in range(2,n+1):
        for x in range(2,n+1):
            #Here is where we find all the multiples from the variable p
            notPrimes.append(x * p)
            p = p + 1 
    for a in range(len(notSorted)):
        if not notSorted[a] in notPrimes:
            primes.append(notSorted[a])
    print(primes)
ui = input("Generate primes up to")
Sieve_of_Eratosthenes(int(ui))
