import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    res = [ sub['name'] for sub in spicy_foods]
    ##print(res)
    return res

def get_spiciest_foods(spicy_foods):
    newList = []
    for i in spicy_foods:
        if i['heat_level'] > 5:
            newList.append(i)
    return newList

def print_spicy_foods(spicy_foods):
    string = ''
    for item in spicy_foods:
        string += item['name']
        string += ' (' + item['cuisine'] + ') '
        heat_level = '| Heat Level: '+ ('🌶' * item['heat_level'])
        string += heat_level
        print(string)
        string = ''


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if cuisine == item['cuisine']:
            return item

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emoji = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")


def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food['heat_level']
    average_heat = total_heat / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

##get_names(spicy_foods)
##get_spiciest_foods(spicy_foods)
##ipdb.set_trace()
##print_spicy_foods(spicy_foods)
get_average_heat_level(spicy_foods)