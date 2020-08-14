import json

#data = []
newf = open("s2-corpus-000-cs.txt", "a")
with open('s2-corpus-000') as f:
    for line in f:
        #data.append(json.loads(line))
	json.loads(line)
        if "Computer Science" in line:
		newf.write(line)
		        
newf.close()      
