import sys

def LCM(a, b): ## Поиск наименьшего общего кратного двух чисел a и b
    if type(a) not in [int] or type(b) not in [int]:
        raise ValueError('Было введено не число') 
    if (a == 0 and b == 0):
        raise ZeroDivisionError('Нет общего кратного больше 0')
    else:
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return(m // (a + b))


def GCD(a, b): ## Поиск наибольшего общего делителя двух чисел a и b
    if type(a) not in [int] or type(b) not in [int]:
        raise ValueError('Было введено не число') 
    if (a == 0 and b == 0):
        raise ZeroDivisionError('Нет общего делителя больше 0')
    else:
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return (a + b)


def reducing_a_fraction_decorator(funct): ## Сокращение дроби через НОД
    def reducing_a_fraction (*args, **kwargs):
        Numerator, Denominator  = funct(*args, **kwargs)
        gcd = GCD(Numerator, Denominator)
        if(gcd == 0):
            raise ZeroDivisionError('наибольший общий делитель равен 0')
        else:
            Numerator//=gcd
            Denominator//=gcd
        return Numerator, Denominator
    return reducing_a_fraction


def sum(numerator1, denominator1, numerator2, denominator2): ##Операция сложения
    if type(numerator1) not in [int] or type(numerator2) not in [int] or type(denominator1) not in [int] or type(denominator2) not in [int]:
        raise ValueError('Было введено не число') 
    if(denominator1 == denominator2):
        resultNum = numerator1 + numerator2 ## Сложение дробей с одним знаминателем 
        resultDen = denominator1  
    else:
        resultDen = LCM(denominator1, denominator2) ## Сложение дробей с разными знаминателями
        resultNum = numerator1*(resultDen//denominator1) + numerator2*(resultDen//denominator2) 
    return resultNum, resultDen

def difference(numerator1, denominator1, numerator2, denominator2): ##Операция вычитания
    if type(numerator1) not in [int] or type(numerator2) not in [int] or type(denominator1) not in [int] or type(denominator2) not in [int]:
        raise ValueError('Было введено не число') 
    if(denominator1 == denominator2):
        resultNum = numerator1 - numerator2 ## Сложение дробей с одним знаминателем
        resultDen = denominator1  
    else:
        resultDen = LCM(denominator1, denominator2) ## Сложение дробей с разным знаминателем
        resultNum = numerator1*(resultDen//denominator1) - numerator2*(resultDen//denominator2) 
    return resultNum, resultDen
    
def multiplication(numerator1, denominator1, numerator2, denominator2): ## Умножение дробей
    if type(numerator1) not in [int] or type(numerator2) not in [int] or type(denominator1) not in [int] or type(denominator2) not in [int]:
        raise ValueError('Было введено не число') 
    resultNum = numerator1 * numerator2
    resultDen = denominator1 * denominator2
    return resultNum, resultDen

def dividing(numerator1, denominator1, numerator2, denominator2): ## Деление дробей
    if type(numerator1) not in [int] or type(numerator2) not in [int] or type(denominator1) not in [int] or type(denominator2) not in [int]:
        raise ValueError('Было введено не число') 
    resultNum = numerator1 * denominator2
    resultDen = denominator1 * numerator2
    return resultNum, resultDen
