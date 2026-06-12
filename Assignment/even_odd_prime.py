def is_even(num):
    return num%2 == 0

def is_odd(num):
    return not is_even(num)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num**0.5):
        if num%i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        num = int(input("Enter a number: "))
        print(f"{num} is Even : ",is_even(num))
        print(f"{num} is Odd : ",is_odd(num))
        print(f"{num} is Prime : ",is_prime(num))

        wana_try_again = input("Wana try again (y/n) : ")
        if wana_try_again.lower() == 'n':
            break
    print("Thank you...")