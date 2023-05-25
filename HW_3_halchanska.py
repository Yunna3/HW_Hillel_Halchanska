#2-Створити файл де показати форматування рядків за допомогою '{}'.format() та f'{}'
puppy_name = 'JEK'
breed = 'Labrador'
print('Puppy_name:' + puppy_name)
print(f'Puppy_name: {puppy_name}, {breed}')
print('Puppy_name:{}' .format(puppy_name))
print('Full Puppy_name: {1} {0}' .format(puppy_name, breed))
print(r'Raw string')

#3-Показати роботу методів типу даних Рядок (на приклад .split(), .upper(), .lower(), .capitalize(), .find()*)
sentence = 'Hello my world'
words = sentence.split()
print(words)
# upper()
words = sentence.upper()
print(words)
#lower()
words = sentence.lower()
print(words)
#.capitalize()
words = sentence.capitalize()
print(words)
#.find
words = sentence.find
print(words)
###
words = sentence.casefold()
print(words)
#4--Створити файл де показати роботу зі списками
#a створити список
#list = list() #stvorenya spusky
#print('List initiated via list (): {}' .format(list))
list = list
print('List of developed projects (): {}' .format(list))
list_1 = list
print('old_list (): {}' .format(list))

#b копіювати через .copy()
list = ['hey', 1, 2, 3, 4]
new_list = list.copy()
print('copy_list:' , new_list)

#c додати елемент до списку.

new_list = list
new_list.append(111)
print('List of developed projects 111: {}' .format(list))

#d вставити елемент а певне місце. (Задача на використання методу .insert(), говорив, але не встиг показати) (Задача з зірочкою*)
clas = [8, 9, 10]
clas.insert(3, 4)
print(clas)

#e додати один список до іншого 2 способами *
new_list_new = ['dog', 'cat', 'monkey']
white = ','
white = white.join(new_list_new)
print('Show white2', white)
#II way

pt1 = ['1', '5', '7', '9']
print('Show count', pt1)
lor2 = ' '
lor = lor2.join (pt1)
print('show information', lor)
#f команда .pop()

pop_letter = new_list.pop(4)
print('Pop letter{}'.format(pop_letter))

#g видалити елемент за значенням і за індексом.
tviy_list =[23, 45, 19, 'KNR']
tviy_list.remove(45)
print(tviy_list)

cat = tviy_list.pop(2)#2 zabira ostannyu
print(cat)
print(tviy_list)
#h показати як дістати значення елемента за його індексом. ???
element = [1, 4, 5, 7, 8, 9]
element [0]
element [5]
y= len(element)-7
element [y]

# 5-slices [::]
#a За допомогою даної конструкції перевернути рядок
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
print(is_palindrome('slices'))
#1
text = 'slices' [::-1]
print(text)
#b За допомогою даної конструкції перевернути список
if __name__ =='__main__' :
    a = [1, 2, 3, 4, 5]
    a.reverse()
    print(a)

#c повернути частину списку від 2 до 7 елементу з кроком 2?
list_k=[1, 2, 3, 4, 5, 6, 7]
returned_part_list = list_k[2:4:5]
print(returned_part_list)
#d поварнути частину рядка (вважати рядок списком)
my_list = ['Friday', 'Thusday', 'Sunday']
delimiter = ''
output = delimiter.join (my_list)
print(output)