n = int(input())
named_cities = []
starting_letter = ''
i = 0
while i<n:
    city = input().lower()
    if i == 0:
        starting_letter = city[0]
    if city in named_cities or city[0] != starting_letter:
        print("REPEAT")
    else:
        print("OK")
        named_cities.append(city)
        i += 1
        starting_letter = city[-1]

