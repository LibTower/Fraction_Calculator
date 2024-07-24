print('Введите числитель первой дроби: ')
numerator1 = input()
print('Введите знаменатель первой дроби: ')
denominator1 = input()
print('Введите числитель второй дроби: ')
numerator2 = input()
print('Введите знаменатель второй дроби: ')
denominator2 = input()

print('Ваши дроби: ')
print('\n', numerator1 + '     ' + numerator2, '\n', '-' + '     ' + '-', '\n', denominator1+ '     ' + denominator2)

print('Выбирите опирацию: ')
print('1 - опирация сложения\n2 - опирация вычитания\n')
choise = input()

if(choise == 1):
    print('*')
    if(denominator1 == denominator2):
        print('*')
        resultNumerator = numerator1 + numerator2
        print('Результат сложения:\n')
        print('\n', numerator1 + '     ' + numerator2 + '     ' + resultNumerator, '\n', '-' + '     ' + '-' + '     ' + '-', '\n', denominator1 + '     ' + denominator2 + '     ' + denominator2)
