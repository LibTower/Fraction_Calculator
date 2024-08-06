class Calculator:

    def __init__(self):
        self.__numerator1 = None
        self.__denominator1 = None

        self.__numerator2 = None
        self.__denominator2 = None

        self.__ResultNum = None
        self.__ResultDen = None


    def __LCM(self, a, b): ## Поиск наименьшего общего кратного двух чисел a и b
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


    def __GCD(self, a, b): ## Поиск наибольшего общего делителя двух чисел a и b
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


    def __reducing_a_fraction_decorator(self, funct): ## Сокращение дроби через НОД
        def __reducing_a_fraction (*args, **kwargs):
            Numerator, Denominator  = funct(*args, **kwargs)
            gcd = self.__GCD(Numerator, Denominator)
            if(gcd == 0):
                raise ZeroDivisionError('наибольший общий делитель равен 0')
            else:
                Numerator//=gcd
                Denominator//=gcd
            return Numerator, Denominator
        return __reducing_a_fraction

    @__reducing_a_fraction_decorator
    def __sum(self): ##Операция сложения
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.denominator1) not in [int] or type(self.denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.__denominator1 == self.__denominator2):
            self.__ResultNum = self.__numerator1 + self.__numerator2 ## Сложение дробей с одним знаминателем 
            self.__ResultDen = self.__denominator1  
        else:
            self.__ResultDen = self.__LCM(self.__denominator1, self.__denominator2) ## Сложение дробей с разными знаминателями
            self.__ResultNum = self.__numerator1*(self.__ResultDen//self.__denominator1) + self.__numerator2*(self.__ResultDen//self.__denominator2) 

    @__reducing_a_fraction_decorator
    def __difference(self): ##Операция вычитания
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.__denominator1 == self.__denominator2):
            self.__ResultNum = self.__numerator1 - self.__numerator2 ## Сложение дробей с одним знаминателем
            self.__ResultDen = self.__denominator1  
        else:
            self.__ResultDen = self.__LCM(self.__denominator1, self.__denominator2) ## Сложение дробей с разным знаминателем
            self.__ResultNum = self.__numerator1*(self.__ResultDen//self.__denominator1) - self.__numerator2*(self.__ResultDen//self.__denominator2) 

    @__reducing_a_fraction_decorator    
    def __multiplication(self): ## Умножение дробей
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.__ResultNum = self.__numerator1 * self.__numerator2
        self.__ResultDen = self.__denominator1 * self.__denominator2

    @__reducing_a_fraction_decorator
    def __dividing(self): ## Деление дробей
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.__ResultNum = self.__numerator1 * self.__denominator2
        self.__ResultDen = self.__denominator1 * self.__numerator2

    def input(self, n1, d1, n2, d2):
        self.__numerator1 = n1
        self.__denominator1 = d1

        self.__numerator2 = n2
        self.__denominator2 = d2


    def output(self):
        return self.__ResultNum, self.__ResultDen