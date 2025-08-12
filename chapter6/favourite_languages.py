favourite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

list_of_people = ['bill', 'jen', 'sarah', 'edward', 'phil']


for person in list_of_people:
    if person in favourite_languages.keys():
        print(f"{person.title()}, thank you for responding.")
    else:
        print(f"{person.title()}, you have not taken the quiz")