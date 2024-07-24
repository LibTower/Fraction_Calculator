def LCM(a, b): ## Функция ищет наименьший общий делитель двух чисел поданых на вход
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return(m // (a + b))

print('Введите числитель первой дроби: ')
numerator1 = int(input())
print('Введите знаменатель первой дроби: ')
denominator1 = int(input())
print('Введите числитель второй дроби: ')
numerator2 = int(input())
print('Введите знаменатель второй дроби: ')
denominator2 = int(input())

print('Ваши дроби: ')
print('\n', numerator1, '     ', numerator2, '\n', '-', '     ', '-', '\n', denominator1, '     ', denominator2)

print('Выбирите опирацию: ')
print('1 - операция сложения\n2 - операция вычитания\n')
choise = int(input())

if(choise == 1): ## операция сложения
    if(denominator1 == denominator2): ## операция сложения при одинаковом знаминателе 
        resultNum = numerator1 + numerator2  ##складываем числители
        print('Результат сложения:') ## выводим на экран все вырожение
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', denominator2)
    else: ## Операция сложения при разных знаминателях
        resultDem = LCM(denominator1, denominator2) ## с помощью функции поиска НОК находим общий знаминатель двух дробей
        ##Находим числитель результата. Для этого числители двух преведущих дробей 
        ##домножаем на то число, на которое необходимо домножить их знаминатели, для того что бы они стали равны
        ##знаминателю результата.
        resultNum = numerator1*(resultDem//denominator1) + numerator2*(resultDem//denominator2) 
        print('Результат сложения:') ## выводим на экран все вырожение
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', resultDem)
elif(choise == 2): ## операция вычитания. Аналогична сложению но числители вычитаются из друг друга.
    if(denominator1 == denominator2):
        resultNum = numerator1 - numerator2
        print('Результат вычитания:')
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', denominator2)
    else:
        resultDem = LCM(denominator1, denominator2)
        resultNum = numerator1*(resultDem//denominator1) - numerator2*(resultDem//denominator2)
        print('Результат вычитания:')
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', resultDem)
 
