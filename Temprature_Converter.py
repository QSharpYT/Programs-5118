#Variables for pre-decleration
opt = None
#Functions
def cf(c): return (c * 9 / 5) + 32
def fc(f): return (f - 32) * 5 / 9
def ck(c): return c + 273.15
def kc(k): return k - 273.15
def fk(f): return ck(fc(f))
def kf(k): return cf(kc(k))
#Main Code + Variables amd Lists
print("""Temperature Converter:
1. °C → °F
2. °F → °C
3. °C → K
4. K → °C
5. °F → K
6. K → °F""")
while True:
    try:
        print("Type 'exit' to exit the Temperature Converter")
        opt = input("Choose (1-6): ")
        if opt == 'exit':
            break
        val = float(input("Enter value: "))
        conv = [cf, fc, ck, kc, fk, kf]
        units = ["°F", "°C", "K", "°C", "K", "°F"]
        print(f"Result: {conv[int(opt)-1](val):.2f}{units[int(opt)-1]}")
    except:
        print("Invalid input.")
print("Temprature Convertor exited")