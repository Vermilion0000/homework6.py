my_dikt = {'Yaroslav': 2004, 'Vermilion': 2019, 'Barbara': 2005}
print(my_dikt)
print(my_dikt['Vermilion'])
print(my_dikt.get('Max'))
my_dikt.update({'Max': 2004, 'Vladimir': 2004})
print(my_dikt)
delete = my_dikt.pop('Vladimir')
print(delete)
print(my_dikt)

my_set = {1, 1, 2, 2, 'Vermilion', 'Vermilion', 3.14, 3.14}
print(my_set)
my_set.update({8, 9, 8, 65})
my_set.remove('Vermilion')
print(my_set)
