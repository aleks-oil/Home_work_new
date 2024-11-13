print('Практическое задание "Неизменяемые и изменяемые объекты. Кортежи и списки"')
immutable_var = 1,2,"a","b" # создание кортежа - неизменяемый тип данных
print(immutable_var, type(immutable_var))
immutable_var_1 = (1,2,3,4)
print(immutable_var_1)

mutable_list = [1,2,3,'a','b']
print(mutable_list, type(mutable_list))
mutable_list[0] = 5 # изменение элемента списка через индекс элемента
print(mutable_list)
mutable_list.extend(['c','d','e',1]) # изменение списка добавлением элемента
print(mutable_list)
