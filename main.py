my_dict={'Denis': 1997,'Petya': 1987,'Ira': 1999}
print( my_dict)
#Создали переменную  my_dict и присвоили словарь с индексами и их значениями
print( my_dict.get('Denis'))
#Вывели значение ключа ('Denis') 1997 спомощью команды .get
print( my_dict.get('Vasiliy'))
#Вывели несуществующее значение ('Vasiliy'), без ошибки с результатом None
my_dict.update({'Senya': 2000,
                 'Ylia': 2004})
print(my_dict)
#С помощью команды .update добавили две произвольные пары того же формата
#my_dict.pop('Petya')
#print(my_dict)
#С помощью команды .pop мы убрали пару 'Petya' из словаря
a = my_dict.pop('Petya')
print(a)
#Присвоили переменной (a) переменную my_dict.pop где выйснили значение удаленного индекса 'Petya'
print(my_dict)

my_set={3,3,3,5,5,'Грушаа','a','a'}
#Создали переменную my_set и присвоили ей множество разных и повторяющих значений
print(my_set)
#Отобразили уникальные значения
my_set=set(my_set)
print(my_set.add('r'))
print(my_set)
my_set=set(my_set)
print(my_set.add(9))
print(my_set)
#Добавили два произвольных элемента в множество 'r','t'
print(my_set.remove(3))
print(my_set)
#Удалили элемент (3) с помощью команды .remove