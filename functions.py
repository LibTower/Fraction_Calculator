def LCM(a, b): ## Поиск наименьшего общего кратного двух чисел a и b
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return(m // (a + b))

def GCD(a, b): ## Поиск наибольшего общего делителя двух чисел a и b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return (a + b)

def reducing_a_fraction(Numerator, Denominator): ## Сокращение дроби через НОД
    gcd = GCD(Numerator, Denominator)
    Numerator//=gcd
    Denominator//=gcd
    return Numerator, Denominator

def sum(numerator1, denominator1, numerator2, denominator2): ##Операция сложения
    if(denominator1 == denominator2):
        resultNum = numerator1 + numerator2 ## Сложение дробей с одним знаминателем 
        resultDen = denominator1  
    else:
        resultDen = LCM(denominator1, denominator2) ## Сложение дробей с разными знаминателями
        resultNum = numerator1*(resultDen//denominator1) + numerator2*(resultDen//denominator2) 
    return resultNum, resultDen

def difference(numerator1, denominator1, numerator2, denominator2): ##Операция вычитания
    if(denominator1 == denominator2):
        resultNum = numerator1 - numerator2 ## Сложение дробей с одним знаминателем
        resultDen = denominator1  
    else:
        resultDen = LCM(denominator1, denominator2) ## Сложение дробей с разным знаминателем
        resultNum = numerator1*(resultDen//denominator1) - numerator2*(resultDen//denominator2) 
        return resultNum, resultDen
    
def multiplication(numerator1, denominator1, numerator2, denominator2): ## Умножение дробей
    resultNum = numerator1 * numerator2
    resultDen = denominator1 * denominator2
    return resultNum, resultDen

def dividing(numerator1, denominator1, numerator2, denominator2): ## Деление дробей
    resultNum = numerator1 * denominator2
    resultDen = denominator1 * numerator2
    return resultNum, resultDen
