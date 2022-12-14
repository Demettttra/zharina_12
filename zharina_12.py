def summa(a,b):    return a+b
def vychet(a,b):    return a-b
def proiz(a,b):    return a*b
def chast(a,b):    return a/b
while True:
    a = float(input('Введите число: '))
    b = float(input('Введите ещё одно число: '))
    c = input('Укажите арифметический знак либо 0 для завершения: ')
    if c=='+':    print(summa(a,b))
    if c=='-':    print(vychet(a,b))
    if c=='*':    print(proiz(a,b))
    if c=='/':
        try:    print(chast(a,b))
        except ZeroDivisionError:    print('На ноль делить нельзя!!!')
    if c=='0':
        print('Вычисления окончены')
        break
