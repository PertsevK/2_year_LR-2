from math import factorial


def task_if6():
    """Two numbers are given. Bring out more of them"""
    try:  # Перевірка
        num1 = float(input("Enter a Number: "))  # Введення першого числа
        num2 = float(input("Enter a Number: "))  # Введення другого числа
        if num1 >= num2:  # Порівняння
            print("Answer: ", num1)
        else:
            print("Answer: ", num2)
    except ValueError:  # Якщо помилка
        print("FLOAT expected!")


def task_geom19():
    """Geometry 19"""
    try:  # Перевірка
        r = float(input("Enter a Radius: "))  # Введення радіуса
        if r < 0:
            raise ValueError
        # Працюємо не з однією точкою, а зі списком
        for i in range(int(input("Enter point amount: "))):
            x = float(input(f"Enter x{i+1}: "))  # Введення координат
            y = float(input(f"Enter y{i+1}: "))
            if x >= 0 and x <= r and y >= x - 2 * r and (x - r) * (x - r) + (y - r) * (y - r) >= r:
                print(f"The point {i+1} is in the area")  # Якщо входить в область
            else:
                print(f"The point {i+1} is not in the area")  # Якщо не входить
    except ValueError:  # Якщо помилка
        print("FLOAT expected!")


def task_series10():
    """Check the series (variant 10) for convergence"""
    n = 1  # Початкове значення n
    s = u = 2.0  # Значення ряду в точці n=1
    e = 1e-10  # g = 1e+10 - точність
    while abs(u) > e:  # abs(u) < g
        print(u)
        n += 1
        try:
            u = (factorial(n) - 3 ** n) / n ** n  # Формула
        except ZeroDivisionError:
            print("Division by zero!")
            return False
        else:
            s += u
    else:
        print("Series converge to: ", s)  # "Maximum sum is:"
        return True

