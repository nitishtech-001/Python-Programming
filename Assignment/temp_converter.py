def celsius_fahrenheit(celsius):
    # formula is (f-32)/9 = c/5 so f = (9*c/5)+32
    fahrenheit = (9*celsius/5)+32
    return fahrenheit

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_fahrenheit(celsius)
    print(f"Celsius of {celsius} Equivalent Farenheit is {fahrenheit}")