def file_open_dict(file):
    cook = list()
    cook_book = dict()
    with open('recipes.txt', 'rt', encoding='utf-8') as fg:
        for line in fg:
            line = line.strip()
            cook.append(line)
    for x in range(len(cook)):
        if cook[x].isdigit():
            items = list()
            key = cook[x-1]
            for y in range(1, int(cook[x])+1):
                ingredients_n = dict()
                ingredient = cook[x + y].split('|')
                ingredients_n['ingredient_name'] = ingredient[0]
                ingredients_n['quantity'] = int(ingredient[1])
                ingredients_n['measure'] = ingredient[2]
                items.append(ingredients_n)
            cook_book[key] = items
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    title_list = dict()
    for dish in dishes:
        for ingredients_n in cook_book[dish]:
            if ingredients_n['ingredient_name'] not in title_list:
                title_list[ingredients_n['ingredient_name']] = {
                        'measure': ingredients_n['measure'],
                        'quantity': ingredients_n['quantity'] * person_count
                }
            else:
                title_list[ingredients_n['ingredient_name']]['quantity'] = (
                        title_list[ingredients_n['ingredient_name']]['quantity']
                        + (ingredients_n['quantity'] * person_count))
    return title_list


if __name__ == "__main__":
    file = "recipes.txt"
cook_book = file_open_dict(file)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
