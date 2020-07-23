numbers = [1,5,7,5,8,1,9,6,4,7,13,9,7,1,36,3,5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
