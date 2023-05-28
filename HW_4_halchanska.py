#STRING:
#Give an example of a simple string
import copy

t='Hello world'
print(t)
#Give an example of a multi-line string (Poem, hoku - to show formatting)
tt = 'Love, like a mountain-wind upon an oak,\nFalling upon me, shakes me leaf and bough.'
print(tt)
#Give an example of a string with escaping characters ignored (Raw)/raw string
raw_stringA = r'Monkey see \ monkey do'
print(raw_stringA)

raw_stringB = 'Monkey see \\ monkey \\ do'
print(raw_stringB)

raw_stringC = R'Monkey see \ monkey \ do'
print(raw_stringC)

print('')

#Give an example of formatting long lines/long string
long_string_format = 'Red Pandas are normally solitary creatures but come together in pairs in the breeding season.\n' \
                     'The females use sticks and leaves to build nests in hollow trees.\n'\
    'After a gestation of about 134 days, females can deliver between one to four cubs but usually litters are two cubs.'
print(long_string_format)

#Lists:
#Create a simpl list/import copy
#Create a variable with a reference to the first list

simple_list_1 = []
print(id(simple_list_1))
print(simple_list_1)

simple_list_2 = list()
print("simple_list_2 id {}" .format (id(simple_list_2)))
print("simple_list_2 values {}" .format(simple_list_2))

list_3 = simple_list_2
print("list_3 id {}" .format(id(list_3)))
print("list_3 values {} " .format(list_3))

#Create a shallow copy of the first list
shallow_copy = copy.copy(simple_list_2)
print('Shallow copy list id {}' .format(id(shallow_copy)))
print('Shallow copy list values {}' .format(shallow_copy))

#Create a deep (full) (Deep copy) of the first list
deep_copy = copy.deepcopy(simple_list_2)
print('Deep copy list id){}' .format(id(deep_copy)))
print('Deep copy list values {}'.format(deep_copy))

#all list
print('' * 30)
print('list 2 id {}' .format(id(list_3)))
print('list copy id{}' .format(id(simple_list_2)))
print('list 1 id {}' .format(id(simple_list_1)))
print('list deep id {}' .format(id(deep_copy)))
#.append
print(list)
print('list2 id {}'.format(id(simple_list_2)))
print('list copy id {}'.format(id(deep_copy)))
print('shallow list copy id {}'.format(id(shallow_copy)))
print('deep copy list id {}'.format(id(deep_copy)))

#DICTOONARY:
#EMPTY DICTIONARY
big_dictionary = {}
print(big_dictionary)
print('')

#Створити новий словник з 2-3 парами ключ:значення
dictionary_new ={
    'tea': 'coffe',
    'juice': 'water'
}
print(dictionary_new)
print('')

#Додати одну пару ключ:значення до першого словника
big_dictionary['number'] = '222'
print(big_dictionary)
print('')

#Додати до першого словника другий словник використовуючи .update()
big_dictionary.update(dictionary_new)
print(big_dictionary)
print('')

#видалити один елемент словника за допомогою .pop()
remove_tea = dictionary_new.pop('tea')
print('Remowed element {}'.format(remove_tea))
print(dictionary_new)
print('')

#Видалити один елемент за допомогою .popitem()
remove_item = big_dictionary.popitem()
print('Remove item {}' .format(remove_item))
print(big_dictionary)
print('')

#Зробити глибоку копію першого словника в нову змінну
import copy
dictionary_deep_copy = copy.deepcopy(big_dictionary)
print('Deep copy dictionary id {}'
      .format(id(dictionary_deep_copy)))
print('Deep copy dictionary values {}'
      .format(dictionary_deep_copy))

dictionary_deep_copy['1_dictionary'] = big_dictionary
print(dictionary_deep_copy)
print('')

#keys & values
new_key = dictionary_deep_copy.keys()
print(new_key)
print('')

new_value = dictionary_deep_copy.values()
print(new_value)
print('')

#ternary if
number = 4
variable = None
if number * 2 == 8:
    variable = True
else:
    variable = False
    print('The number {} is even: {}' .format(number, variable))
    ternary_variable = True if number * 2 == 8 else False
    print('The number {} is even: {}' .format(number,
                                              ternary_variable))
    print('')

# task 5 nested structures
# 3-dimensional list
first_nested_list = [1,2,3,[10,11,12],4,5,[13]]
print('Nested list id {}' .format(id(first_nested_list)))
print('Nested list id {}'.format(first_nested_list))
import copy
second_copy_nested = copy.copy(first_nested_list)
print('Shallow copied nested list id {}'
      .format(id(second_copy_nested)))
print('Shallow copied nested list {}'
      .format(second_copy_nested))


second_copy_nested [6].append(14)
print('Updated nested list id {}'
      .format(id(second_copy_nested)))
print('Updated nested list {}'.format(second_copy_nested))


print('Nested list id {}' .format(id(first_nested_list)))
print('Nested list {}' .format(first_nested_list))
print('Updated nested list id {}'
      .format(id(second_copy_nested)))
print('Updated nested list {}'.format(second_copy_nested))
print('')


# list with nested dictionary

nested_book = [1,2,3, {'singer': 'Tata', 'type': 'musician'}, 4,5]
print(nested_book)
print('')

# dictionary with nested list
nested_dictionary = {'singer': 'Tata', 'type': 'musician',
                     'nested list':[1,2,3,4]}
print(nested_dictionary)
print('')

# list from dictionary
list_from_dictionary = nested_dictionary.pop('nested list')
print('Popped value is {}' .format(list_from_dictionary))
print(list_from_dictionary)
print('')

#task 6 bitwise operators
#bitwise AND
www = bin(4)
print(www)

www_1=int(www,2)
print(www_1)
print('')

# & AND
print(bin(10))
print(bin(10))
print(bin(10 &10))
print(int(bin(10 &10), 2))

print(' ')

print(bin(10))
print(bin(8))
print(bin(10 &8))
print(int(bin(10 &8), 2))

print(' ')
# | OR
print(bin(8))
print(bin(8))
print(bin(8 | 8))
print(int(bin(8 | 8), 2))

print(' ')
print(bin(6))
print(bin(5))
print(bin(6 &5))
print(int(bin(6 &5), 2))

print(' ')
# ^ XOR
print(bin(11))
print(bin(11))
print(bin(11 ^ 11))
print(int(bin(11 ^ 11), 2))

print(' ')
print(bin(100))
print(bin(75))
print(bin(100 ^ 75))
print(int(bin(100 ^ 75), 2))
# ~ NOT
print(' ')
print(bin(10))
print(bin(10))
print(bin(10 & ~10))
print(int(bin(10 & ~10), 2))

print(' ')
print(bin(100))
print(bin(75))
print(bin(100 & ~75))
print(int(bin(100 & ~75), 2))
print('')
# bitwise shift to the left <<
print(bin(256))
print(bin(256 <<1))
print(bin(256 <<2))
print(bin(256 <<3))
print(' ')


# bitwise shift to the right  >>
print(bin(100))
print(bin(100 >>1))
print(bin(100 >>2))
print(bin(100 >>3))
print(' ')

#task 6 bitwise operators for string
# different strings
ccc = "I am"
ccc_2 = " a student"
bytes1 = ccc.encode()
bytes2 = ccc_2.encode()

int1 = int.from_bytes(bytes1)
int2 = int.from_bytes(bytes2)

operator_and = int1 & int2
operator_or = int1 | int2
operator_xor = int1 ^ int2
operator_not = ~int1

convert_bytes1 = operator_and.to_bytes(max(len(bytes1), len(bytes2)))
convert_bytes2 = operator_or.to_bytes(max(len(bytes1), len(bytes2)))
convert_bytes3 = operator_xor.to_bytes(max(len(bytes1), len(bytes2)))

print(f'And: {convert_bytes1}')
print(f'OR: {convert_bytes2}')
print(f'XOR: {convert_bytes3}')
print(operator_not)
print("")

# option 2
sss_4= 'Yunna'
ddd_5 = 'Halchanska'
bytes_11 = sss_4.encode()
bytes_22= ddd_5.encode()

int_11 = int.from_bytes(bytes_11)
int_22 = int.from_bytes(bytes_22)

print(bin(int_11 & int_22))
print(bin(int_11 | int_22))
print(bin(int_11 ^ int_22))
print(bin(int_11 & ~int_22))
print("")

# same strings
ggg_1 = 'Dog'
kkk_2 = 'Dog'
bytes3 = ggg_1.encode('ascii')
bytes4= kkk_2.encode('ascii')

int3 = int.from_bytes(bytes3)
int4 = int.from_bytes(bytes4)

operator_and = int3 & int4
operator_or = int3 | int4
operator_xor = int3 ^ int4

convert_bytes4 = operator_and.to_bytes(max(len(bytes3), len(bytes4)))
convert_bytes5 = operator_or.to_bytes(max(len(bytes3), len(bytes4)))
convert_bytes6 = operator_xor.to_bytes(max(len(bytes3), len(bytes4)))

print(f'And: {convert_bytes4}')
print(f'OR: {convert_bytes5}')
print(f'XOR: {convert_bytes6}')
print("")

# option 2
hhh_1 = 'sun'
fff_2 = 'cloud'
bytes_33 = hhh_1.encode()
bytes_44= fff_2.encode()

int_33 = int.from_bytes(bytes3)
int_44 = int.from_bytes(bytes4)

print(bin(int_33 & int_44))
print(bin(int_33 | int_44))
print(bin(int_33 ^ int_44))
print(bin(int_33 & ~int_44))
print("")
# left shift
sss_4 = "test"
bytes_1 = sss_4.encode()
print(bytes_1)
int_1 = int.from_bytes(bytes_1)
print(int_1)
print(bin(int_1 <<1))
print(bin(int_1 <<2))
print(bin(int_1 <<3))
print(" ")

#right shift
ddd_5 = "test"
bytes_2 = ddd_5.encode()
print(bytes_2)
int_2 = int.from_bytes(bytes_2)
print(int_2)
print(bin(int_2 >>1))
print(bin(int_2 >>2))
print(bin(int_2 >>3))



