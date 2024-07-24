def LCM(a, b):
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
print('1 - опирация сложения\n2 - опирация вычитания\n')
choise = int(input())

if(choise == 1):
    if(denominator1 == denominator2):
        resultNum = numerator1 + numerator2
        print('Результат сложения:')
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', denominator2)
    else:
        resultDem = LCM(denominator1, denominator2)
        resultNum = numerator1*(resultDem//denominator1) + numerator2*(resultDem//denominator2)
        print('Результат сложения:')
        print('\n', numerator1,  '     ',  numerator2, '     ',  resultNum, '\n', '-',  '  +  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', resultDem)