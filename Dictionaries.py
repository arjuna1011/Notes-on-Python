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