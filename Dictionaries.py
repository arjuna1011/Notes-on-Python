# Dictionaries are indentified with curly brackets.

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaga XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)
# Very similar to indexing lists.

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get("er5")
print(learner)

# Iterating over a Dictionary

for key in vehicles:
    print(key, vehicles[key], sep=", ")
    
# The better and more efficient way: 

for key, value in vehicles.items():
    print(key,value, sep=", ")
    
# Adding to dictionaries:

vehicles["starfighter"] = "Lockhead F-104"
print(vehicles)

# Chaning values in a dictionary:
vehicles["virago"] = "Yamaha XV535"
print(vehicles)

# Removing items from a dictionary:
del vehicles['starfighter']
print(vehicles)

result = vehicles.pop("jimny")
print(result)

# ===================================================================

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}
def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dictionary."""
    if item in data:
        data[item] += amount
    else:
        data[item] = amount    
    
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
    
while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
        
    choice = input(": ")
    
    if choice == "0":
        break    
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}.")
        print("Checking ingredients....")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t You need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)


# setdefault method

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

z_qualitity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_qualitity}")

print()
print("`pantry` now contains....")

for key, value in sorted(pantry.items()):
    print(key, value)