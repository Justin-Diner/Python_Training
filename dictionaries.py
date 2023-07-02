# To declare a dictionary you can do:
pond = dict(
    depth=10, 
    area="210 square feet",
    fish=["Mary", "Bob", "Barry"]
)

print(pond)

alligator = dict(([
    ('lifespan', 50),
    ('length', 3.4),
    ('lengthUnits', 'm'),
    ('species', ["American Alligator", "Chinese Alligator"]),
    ('funFact', "As an alligator's teeth are won down, they are replaced."),
]))

print(alligator)

keys = ["name", "home runs", "strikeouts", "rbi"]
values = ["Babe Ruth", 7214, 1330, 2214]

player = dict(zip(keys, values))
print(player)
print(dir(dict))

# Remember that you can spread dictionaries with ** 
def concatenate_dictionaries(lst):
    new_dict = {}
    for dict in lst:
        new_dict = { **new_dict, **dict }
    return new_dict

# Using .update
def concatenate_dictionaries2(lst):
    new_dict = {}
    for dict in lst:
        new_dict.update(dict)
    return new_dict

# Very manual solution
def concatenate_dictionaries3(lst):
    new_dict = {}
    for dict in lst:
        for key in dict.keys():
            new_dict[key] = dict[key]
    return new_dict

lst = [
    {
        'a': 'this',
        'b': 'is'
    },
    {
        'c': 'the',
        'd': 'merged'
    },
    {
        'd': 'dictionary'
    }
]

print(concatenate_dictionaries(lst))
"""
Prints: 
{
    a: 'this',
    b: 'is',
    c: 'the',
    d: 'dictionary'
}
"""
