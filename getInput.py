print('hello world! ' * 2)
lang = 'python'

price = 10
price2 = 50

print('\nvaios goes ' + lang)
print(price + price2)

num = input('\nEnter a number: ')
print(num)

#Try using raw_input instead of input for strings
onoma = raw_input('\nEnter name: ') 
print('hello ' + onoma + ' my friend')

# input and raw_input always takes input as a string example '1982' not 1982
birth_date= input('\nbirth date: ')
age = 2020 - int(birth_date)
print('age: '  + str(age))



