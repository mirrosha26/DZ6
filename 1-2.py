import os
dir_path = 'example_1-2'
filename = 'test.txt'
path = os.path.join(dir_path,filename)
cook_book = {}
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        dish = line.strip()
        dish_count = file.readline()
        cook_book[dish] =[]
        for ingredient in range(int(dish_count)):
            emp = file.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            dictor = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure }
            cook_book[dish] += [dictor]
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    purchase = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in purchase:
                purchase[name]['quantity'] += ingredient['quantity']*person_count
            else:
                purchase[name] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']*person_count }
    print(purchase)

# Тест
dishes, person_count = ['Омлет','Утка по-пекински'],2
get_shop_list_by_dishes(dishes, person_count)



