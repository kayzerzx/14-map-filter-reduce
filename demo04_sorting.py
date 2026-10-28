names = ["Evan", "Jace", "Zach", "Mykyta", "Isaac", "allyn"]
#we can sort the list with .sort method
#note: this changes the actual order of your list
print(names)
names.sort() #defualts to alphabetical (all capitals first)
print(names)

#sort it reverse order:
names.sort(reverse=True)
print(names)

other_names = ("blake", "michael", "abigale", "josie", 
               "ryan", "josh", "duane", "john")

#other_names.sort() #cant change a tuple
#print(other_names)
#but we can sort a tuple if we use sorted:
sorted_other_names = sorted(other_names)
#sorted returns a new list instead of sorting in a line
print(sorted_other_names)
print(dict(enumerate(sorted_other_names)))
print(dict(zip(["A", "B", "C", "D", "E", "F", "G", "H"], other_names)))

#sort by lrngth of string:
len_of_names_sorted = sorted(other_names, key=len)
print(len_of_names_sorted)

from functools import reduce
count_vowels = lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s)))
print(count_vowels("dog"))

most_vowels = sorted(other_names, key =
                     lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s))), reverse=True)
 
print(most_vowels)
#Idk about this one tho i just added reverse

def get_last_letter(word):
    return word[-1]

sorted_by_last_letter = sorted(other_names, key=get_last_letter)
print(sorted_by_last_letter)