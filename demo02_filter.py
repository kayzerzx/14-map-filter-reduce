"""
filter: similar to map, only the function returns the value to determin true or false
"""

names = ["isaac", "david", "jace", "zach", "evan"]

def is_not_zach(name):
    return name.lower().strip() != "zach"

print(names)
cleaned_list = list(filter(is_not_zach, names)) #returns a filter object
print(cleaned_list)

even_better = filter(lambda name: name.lower().strip != "jace", cleaned_list)
print(list(even_better))


grades = [
    {"student": "evan", "score": 12},
    {"student": "isaac", "score": 83},
    {"student": "kaine", "score": 90},
    {"student": "blake", "score": 79},
    {"student": "michael", "score": 89},
    {"student": "zach", "score": 4},
]

#filter this list down to only passing students:
passing_students = list(filter(lambda grade: grade["score"] >= 60, grades))
 
print(passing_students)