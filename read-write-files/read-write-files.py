# Author: Vaios Stergiopoulos

file1 = open('tess.txt', 'r')

Lines = file1.readlines()
text=''
for line in Lines:
	line = line.rstrip('\n')
	newline = f"\'{line}\', "
	text += newline

file1.close()

print(text)
file2 = open('result.txt', 'w')
file2.write(text)
file2.close()
