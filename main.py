# Умножение и сумма
# Верните результат умножения если, сумма умножения равна или
# больше 1000, в противном случае верните значение суммы двух чисел.

def sum_mult (a, b):
    sum = a + b
    mult = a * b
    if mult >= 1000:
        return mult
    else:
        return sum

num1 = float(input("введите первое число: "))
num2 = float(input("введите второе число: "))

print(sum_mult(num1, num2))


