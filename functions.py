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


    def reducing_a_fraction_decorator(self, funct): ## Сокращение дроби через НОД
        def reducing_a_fraction (*args, **kwargs):
            Numerator, Denominator  = funct(*args, **kwargs)
            gcd = self.__GCD(Numerator, Denominator)
            if(gcd == 0):
                raise ZeroDivisionError('наибольший общий делитель равен 0')
            else:
                Numerator//=gcd
                Denominator//=gcd
            return Numerator, Denominator
        return reducing_a_fraction

    @reducing_a_fraction_decorator
    def sum(self): ##Операция сложения
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.__denominator1 == self.__denominator2):
            self.__ResultNum = self.__numerator1 + self.__numerator2 ## Сложение дробей с одним знаминателем 
            self.__ResultDen = self.__denominator1  
        else:
            self.__ResultDen = self.__LCM(self.__denominator1, self.__denominator2) ## Сложение дробей с разными знаминателями
            self.__ResultNum = self.__numerator1*(self.__ResultDen//self.__denominator1) + self.__numerator2*(self.__ResultDen//self.__denominator2) 
        return self.__ResultNum, self.__ResultDen

    @reducing_a_fraction_decorator
    def difference(self): ##Операция вычитания
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        if(self.__denominator1 == self.__denominator2):
            self.__ResultNum = self.__numerator1 - self.__numerator2 ## Сложение дробей с одним знаминателем
            self.__ResultDen = self.__denominator1  
        else:
            self.__ResultDen = self.__LCM(self.__denominator1, self.__denominator2) ## Сложение дробей с разным знаминателем
            self.__ResultNum = self.__numerator1*(self.__ResultDen//self.__denominator1) - self.__numerator2*(self.__ResultDen//self.__denominator2) 
        return self.__ResultNum, self.__ResultDen

    @reducing_a_fraction_decorator    
    def multiplication(self): ## Умножение дробей
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.__ResultNum = self.__numerator1 * self.__numerator2
        self.__ResultDen = self.__denominator1 * self.__denominator2
        return self.__ResultNum, self.__ResultDen

    @reducing_a_fraction_decorator
    def dividing(self): ## Деление дробей
        if type(self.__numerator1) not in [int] or type(self.__numerator2) not in [int] or type(self.__denominator1) not in [int] or type(self.__denominator2) not in [int]:
            raise ValueError('Было введено не число') 
        self.__ResultNum = self.__numerator1 * self.__denominator2
        self.__ResultDen = self.__denominator1 * self.__numerator2
        return self.__ResultNum, self.__ResultDen
    
    def input(self):
        print("Ведите числитель, а затем знаминатель первой дроби: ")
        self.__numerator1 = int(input())
        self.__denominator1 = int(input())
        print("Ведите числитель, а затем знаминатель второй дроби: ")
        self.__numerator2 = int(input())
        self.__denominator2 = int(input())

        print('Ваши дроби: ')
        print('\n', self.__numerator1, '     ', self.__numerator2, '\n', '-', '     ', '-', '\n', self.__denominator1, '     ', self.__denominator2)


    def output(self):
        print('Результат ')
        print('\n', self.__numerator1,  '     ',  self.__numerator2, '     ',  self.__ResultNum, '\n', '-',  '     ',  '-',  '  =  ',  '-', '\n', self.__denominator1, '     ', self.__denominator2, '     ', self.__ResultDen)

    