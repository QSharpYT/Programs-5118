from decimal import Decimal, getcontext
def chudnovsky_algorithm(n):
    getcontext().prec = n + 10
    l = 13591409
    x = 1
    k = 6
    c = 426880 * Decimal(10005).sqrt()
    m = 1
    s = l
    for i in range(1, n):
        m = (k**3 - 16*k) * m // i**3
        l += 545140134
        x *= -262537412640768000
        s += Decimal(m * l) / x
        k += 12
        if str(s).count('.')>1:
          break
    pi = c / s
    return str(pi)[:n+2]
digits = input("How many digits of Pi past 3. do you want?")
try:
    print(chudnovsky_algorithm(int(digits)))
except Exception as e:
    print("Error: ", e)