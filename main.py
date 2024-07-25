import functions

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

print('Программа потдерживает 4 вида операций над дробями.')
print('Сложение [+] \nРазность [-] \nУмножение [*] \nДеление [/] \n')
print('Выберите одну из операций: ')
choise = input()

if(choise == '+'): 
    Num, Den = functions.sum(numerator1, denominator1, numerator2, denominator2)
elif(choise == '-'):
    Num, Den = functions.difference(numerator1, denominator1, numerator2, denominator2)   
elif(choise == '*'):
    Num, Den = functions.multiplication(numerator1, denominator1, numerator2, denominator2)  
elif(choise == '/'): 
    Num, Den = functions.dividing(numerator1, denominator1, numerator2, denominator2)   
print('Результат ')
print('\n', numerator1,  '     ',  numerator2, '     ',  Num, '\n', '-',  ' ', choise, '  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', Den)

Num, Den = functions.reducing_a_fraction(Num, Den)

print('Результат ')
print('\n', numerator1,  '     ',  numerator2, '     ',  Num, '\n', '-',  ' ', choise, '  ',  '-',  '  =  ',  '-', '\n', denominator1, '     ', denominator2, '     ', Den)



