def fahrenheit_to_celsius(f):
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Enter:"))
c = fahrenheit_to_celsius(f)

print(f"{f} °F = {c:.2f} °C")