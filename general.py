import math


def solve_quadratic(a, b, c):
    if a == 0:
        print("Це не квадратне рівняння (a не може бути 0)")
        return None

    D = b ** 2 - 4 * a * c
    print(f"Дискримінант: {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None


def main():
    print("Розв’язання квадратного рівняння ax² + bx + c = 0")
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    result = solve_quadratic(a, b, c)

    if result is None:
        print("Рівняння не має дійсних коренів.")
    else:
        print("Корені рівняння:", result)


if __name__ == "__main__":
    main()
