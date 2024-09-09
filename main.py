my_dict = {"Денис": 1984, "Анна": 1978, "Ульяна": 2010, "Варя": 2013, "Ева": 2014}
print('Семья', my_dict)
print ('Год рождения Анны:', my_dict['Анна'])
print ('Год рождения Ивана:', my_dict.get('Иван', 'таких данных нет'))
my_dict.update({'Лиза': 2003, 'Владик': 2000, 'Саша': 1986})
removed_year = my_dict.pop('Владик')
print ('Значение удалённого элемента \'Владик\':', removed_year)
print ('Измененный словарь:', my_dict)


my_set = {2, 3, 5, 7, 'Изумление', 9, 2, 3, 5, 7, True, list, set, 2, 3, 'Изумление', 5, 9, set, list, True, 3, 5, 9, 7}
print ('Множество:', my_set)
my_set.add ('string')
my_set.add (4)
my_set.discard (2)
my_set.discard ('Изумление')
print ('Измененное множество:', my_set)