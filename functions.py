class Calculator:

    def __init__(self, numerator1, denominator1, numerator2, denominator2):
        self.numerator1 = numerator1
        self.denominator1 = denominator1

        self.numerator2 = numerator2
        self.denominator2 = denominator2

        self.ResultNum = None
        self.ResultDen = None


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
    def sum(self): ##Операция сложения
        if type(self.numerator1) not in [int] or type(self.numerator2) not in [int] or type(self.denominator1) not in [int] or type(self.denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.denominator1 == self.denominator2):
            self.ResultNum = self.numerator1 + self.numerator2 ## Сложение дробей с одним знаминателем 
            self.ResultDen = self.denominator1  
        else:
            self.ResultDen = self.__LCM(self.denominator1, self.denominator2) ## Сложение дробей с разными знаминателями
            self.ResultNum = self.numerator1*(self.ResultDen//self.denominator1) + self.numerator2*(self.ResultDen//self.denominator2) 

    @__reducing_a_fraction_decorator
    def difference(self): ##Операция вычитания
        if type(self.numerator1) not in [int] or type(self.numerator2) not in [int] or type(self.denominator1) not in [int] or type(self.denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.denominator1 == self.denominator2):
            self.ResultNum = self.numerator1 - self.numerator2 ## Сложение дробей с одним знаминателем
            self.ResultDen = self.denominator1  
        else:
            self.ResultDen = self.__LCM(self.denominator1, self.denominator2) ## Сложение дробей с разным знаминателем
            self.ResultNum = self.numerator1*(self.ResultDen//self.denominator1) - self.numerator2*(self.ResultDen//self.denominator2) 

    @__reducing_a_fraction_decorator    
    def multiplication(self): ## Умножение дробей
        if type(self.numerator1) not in [int] or type(self.numerator2) not in [int] or type(self.denominator1) not in [int] or type(self.denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.ResultNum = self.numerator1 * self.numerator2
        self.ResultDen = self.denominator1 * self.denominator2

    @__reducing_a_fraction_decorator
    def dividing(self): ## Деление дробей
        if type(self.numerator1) not in [int] or type(self.numerator2) not in [int] or type(self.denominator1) not in [int] or type(self.denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.ResultNum = self.numerator1 * self.denominator2
        self.ResultDen = self.denominator1 * self.numerator2
