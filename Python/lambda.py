people = [
    {"name": "Kerim", "country": "Romania"},
    {"name": "Rahym", "country": "Romania"},
    {"name": "Dovlet", "country": "Turkey"},
    {"name": "Sukur", "country": "Turkey"}
]

people.sort(key = lambda person: person["country"])

print(people)