import converters

from converters import kg_to_lbs

print(f"{converters.kg_to_lbs(80)} lbs")

print(f"{converters.lbs_to_kg(200)} kgr")

# No converters prefix, because I used the from word and imported specifically this function
print(kg_to_lbs(120)) 
