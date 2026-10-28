"""
the map() function is used to apply a given function to every item in a collection
(collections: list, tuple, set, disctionary)
"""


celsius_temps = [0,10,20.30,40]

#conver there all to a list of fahrenheit

#fehrenheit_temps = [(x*9/5) +32 for x in celsius_temps]

def c_to_f(temp):
    return (temp * 9/5) + 32

fahrenheit_temps = map(c_to_f, celsius_temps)
print(fahrenheit_temps) # map object
#convert maps object to list 
print(list(fahrenheit_temps))

#do the same thing but with a lambda
fahrenheit_temps2 = map(lambda temp: (temp * 9/5) + 32, celsius_temps)
print(list(fahrenheit_temps2)) #map object
#conver to list
#fahrenheit_temps2 = list(fahrenheit_temps2)

#why would we use map
# - save time, no nned for long for loops
# - cleaner code 
# - works great with lambda
# - efficient

names = [
    {"fname": "frank", "lname": "williams", "age": 52},
    {"fname": "david", "lname": "smith", "age": 15},
    {"fname": "jace", "lname": "larkin", "age": 16},
    {"fname": "k", "lname": "luh", "age": 103},
    {"fname": "duane", "lname": "olesnanik", "age": 31}
]

#without list comprehension: map these names to be lastname, Firstinital, 
# zero padded age (52, 052), if was were 7, 007

codes = list(map(lambda dict: f"{dict["lname"]}{dict["fname"][0]}{str(dict["age"]).rjust(3,"0")}",names))
print(codes)

names = [
{"fname":"frank", "lname":"Williams", "age":52},
{"fname":"david", "lname":"smith", "age":15},
{"fname":"jace", "lname":"larkin", "age":16},
{"fname":"K", "lname":"luh", "age":103},
{"fname":"duane", "lname":"olesnanik", "age":31}
]
def func(ell):
    return ell.get("lname")+ell.get("fname")[0]+(str(ell.get("age")).rjust(3,"0"))
aaaa = map(func,names )
print(list(aaaa))

for a in aaaa:
    print(a)
