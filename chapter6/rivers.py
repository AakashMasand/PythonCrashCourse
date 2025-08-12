rivers_and_countries = {
    'Nile': 'Egypt',
    'Mississippi': 'United States',
    'Yangtze': 'China',
    'Amazon': 'Brazil',
    'Ganges': 'India'
}

for river, country in rivers_and_countries.items():
    print(f"\n{river.title()} runs through {country.title()}")


for river in rivers_and_countries:
    print(f"\n {river.title()}")

for river, countries in rivers_and_countries.items():
    print(f"\n {countries.title()}")