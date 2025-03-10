import math
import sys


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error. Expected a valid real number.")


def solve_quadratic(a, b, c):
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    D = b ** 2 - 4 * a * c
    print(f"Equation: ({a}) x^2 + ({b}) x + ({c}) = 0")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Two roots:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print("One root:")
        print(f"x1 = {x}")
    else:
        print("No real roots")


def read_coefficients_from_file(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("Invalid file format")
            a, b, c = map(float, parts)
            return a, b, c
    except FileNotFoundError:
        print(f"File {filename} does not exist")
        sys.exit(1)
    except ValueError:
        print("Invalid file format")
        sys.exit(1)


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        a, b, c = read_coefficients_from_file(filename)
    else:
        print("Solving quadratic equation ax² + bx + c = 0")
        a = get_float("a = ")
        b = get_float("b = ")
        c = get_float("c = ")

    solve_quadratic(a, b, c)


if __name__ == "__main__":
    main()
