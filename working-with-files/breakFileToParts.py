'''
use this code to beak big txt files in smaller parts.
i.e here we choose to have 200000 lines (articles) in each filepart.

author: vaios stergiopoulos
date: 30 Jan 2021
'''

def breakParts(textFile):
    filepath = textFile
    with open(filepath) as fp:
       line = fp.readline()
       partsCounter = 1
       cnt = 1
       partName = f'part_{partsCounter}_{textFile}.txt'
       while line:
           f = open(partName, "a")
           f.write(line)
           f.close()
           line = fp.readline()
           cnt += 1
           if cnt == 200000:
               cnt = 1
               partsCounter += 1
               partName = f'part_{partsCounter}_{textFile}.txt'



## MAIN PROGRAM ##

breakParts('dblp.v12.json')
