import math


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f"Error. Expected a valid real number, got {input(prompt)} instead")


def solve_quadratic(a, b, c):
    if a == 0:
        print("Це не квадратне рівняння (a не може бути 0)")
        return None

    D = b ** 2 - 4 * a * c
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        print("There are 0 roots")


def main():
    print("Розв’язання квадратного рівняння ax² + bx + c = 0")
    a = get_float("a = ")
    b = get_float("b = ")
    c = get_float("c = ")
    solve_quadratic(a, b, c)


if __name__ == "__main__":
    main()
