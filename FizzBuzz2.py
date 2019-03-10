print("1からNまでのFizzBuzz")

number = int(input(f"1つの自然数を入れてね > "))

for N in range(1, number + 1):
    if N % 15 == 0:
        print("FizzBuzz")

    elif N % 3 == 0:
        print("Fizz")

    elif N % 5 == 0:
        print("Buzz")

    else:
        print(N)
