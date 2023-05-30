#1 Tuple
#a Створити кортеж котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
tuple = (1, 2, 3, 4, 5, 6, 7)
print(tuple)

#2 Set
#a Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7
set_1 = {1, 2, 3, 4, 4, 5, 6, 7}
print(set_1)
#b Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11
set_2 = {5,5, 6, 7,11, 8, 9, 10, 11}
print(set_2)

#c Розширити перший сет за допомогою коменди .add(0)
set_1.add(0)
print(set_1)

#d Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
set_1.intersection_update(set_2)
print(set_1)

set_new = set_1.intersection()
print('set_new{}'.format(set_new))
print('set_1{}'.format(set_1))

#e Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
print(set_2)
print(set_new)

set_difference = set_new.difference(set_2)
print(set_difference)

print('set_difference{}'.format(set_difference))
print('set_new{}'.format(set_new))

#f Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
set_symmetric = set_new.symmetric_difference(set_2)
print(set_symmetric)
