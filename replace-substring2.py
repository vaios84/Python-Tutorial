#read input file
fin = open("in", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace(' ', '\', \'')
#close the input file
fin.close()
#open the input file in write mode
fin = open("in", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()
