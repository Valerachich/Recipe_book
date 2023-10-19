import pprint
with open('Recipes.txt', encoding='utf-8') as f:
    data = f.read()


def listing(d):
    cook_book = {}
    li = d.split('\n\n')
    for l in li:
        dish = l[0:l.find('\n')]
        l = l[l.find('\n') + 1:]
        dish_list = []
        for i in range(int(l[0:l.find('\n')])):
            name = l[l.find('\n')+1:l.find("|")-1]
            l = l[l.find('|')+2:]
            quan = int(l[:l.find('|')-1])
            l = l[l.find('|')+2:]
            mes = l[:l.find('\n')]
            dish_list.append({'ingredient_name': name, 'quantity': quan, 'measure': mes})
        cook_book_add = {dish: dish_list}
        cook_book.update(cook_book_add)

    return cook_book


cook_book = listing(data)
pprint.pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    q = {}
    for i in dishes:
        for j in range(len(cook_book.get(i))):
            if cook_book.get(i)[j].get('ingredient_name') not in list(shop_list):
                quan = {'measure': cook_book.get(i)[j].get('measure'), 'quantity': cook_book.get(i)[j].get('quantity') * person_count}
                shop_list_add = {cook_book.get(i)[j].get('ingredient_name'): quan}
                shop_list.update(shop_list_add)

            else:
                q = shop_list.get(cook_book.get(i)[j].get('ingredient_name')).get('quantity')
                quan = {'measure': cook_book.get(i)[j].get('measure'), 'quantity': cook_book.get(i)[j].get('quantity') * person_count + q}
                shop_list_add = {cook_book.get(i)[j].get('ingredient_name'): quan}
                shop_list.update(shop_list_add)
    return shop_list


answer = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)

pprint.pprint(answer)


# with open('1.txt', encoding='utf-8') as f1:
#     data_1 = f1.readlines()
#     file_name1 = '1.txt'
# with open('2.txt', encoding='utf-8') as f2:
#     data_2 = f2.readlines()
# with open('3.txt', encoding='utf-8') as f3:
#     data_3 = f3.readlines()
# with open('4.txt', encoding='utf-8') as f4:
#     data_4 = f4.readlines()


def file_union(file_list):
    file_name_list = []
    data_list = []
    for i in file_list:
        with open(i, encoding='utf-8') as f1:
            data1 = f1.readlines()
            data_list.append(data1)
            file_name_list.append(i)

    data_list_sorted = sorted(data_list, key=len)
    for j in data_list_sorted:
        answer2 = file_name_list[data_list.index(j)] + '\n' + str(len(j)) + '\n' + ''.join(j) + '\n'
        with open('1234.txt', 'a', encoding='utf-8') as f2:
            f2.write(answer2)
    with open('1234.txt', encoding='utf-8') as f3:
        data_3 = f3.read()

    return print(data_3)


file_union(['1.txt', '2.txt', '3.txt', '4.txt'])
