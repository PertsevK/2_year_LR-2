from math import factorial


def task_if6():
    """Two numbers are given. Bring out more of them"""
    try: # Перевірка
        num1=float(input("Enter a Number: ")) # Введення першого числа
        num2=float(input("Enter a Number: ")) # Введення другого числа
        if num1>=num2: # Порівняння
            print("Answer: ", num1)
        else:
            print("Answer: ", num2)    
    except: # Якщо помилка
        print("FLOAT expected!")
        
def task_geom19():
    """Check the series (variant 19) for convergence"""
    try: # Перевірка
        r=float(input("Enter a Radius: ")) # Введення радіуса
        if r>0:
            x=float(input("Enter x: ")) # Введення координат
            y=float(input("Enter y: "))
            if x>=0 and x<=r and y>=x-2*r and (x-r)*(x-r)+(y-r)*(y-r)>=r:
                print("The point is in the area") # Якщо входить в область
            else: print("The point is not in the area") # Якщо не входить
        else: print("r must be positive")
    except: # Якщо помилка
        print("FLOAT expected!")
        
def task_series10():
    """Check the series (variant 10) for convergence"""
    n = 1 # Початкове значення n
    s = u = 2.0 # Значення ряду в точці n=1
    e = 1e-10 # g = 1e+10 - точність
    while abs(u) > e: #abs(u) < g
        print(u)
        n += 1
        if ((n/2)**n) == 0:
            break
        u = (factorial(n)-3**n)/n**n # Формула
        s += u
    else:
        print ("Series converge to: ",s) #"Maximum sum is:"
        return True
    print("Division by zero!")
    return False


# Меню
choice = int(input("Please, choose the task 1-3 (0-EXIT): "))
while choice:
    if choice==1:
        task_if6()
    elif choice==2:
        task_geom19()
    elif choice==3:
        if task_series10():
            print ("OK!")
    else:
        print("Wrong task number!")
    choice = int(input("Please, choose the task again (0-EXIT): "))
print("Good by!")
