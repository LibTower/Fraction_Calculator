from functions import Calculator
a = Calculator()
a.input()
print('Программа потдерживает 4 вида операций над дробями.')
print('Сложение [+] \nРазность [-] \nУмножение [*] \nДеление [/] \n')
print('Выберите одну из операций: ')
choise = input()

if(choise == '+'): 
    a.sum
elif(choise == '-'):
    a.difference
elif(choise == '*'):
    a.multiplication
elif(choise == '/'): 
    a.dividing

a.output()
