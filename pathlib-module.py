from pathlib import Path

# absolute path 
# C:\Program Files\Microsoft\AppFolder
# /usr/local/bin/myapp

# relative path
path1 = Path("ecommerce")
if not path1.exists():
	path1.mkdir() # create a folder named ecommerce
	print("ecommerce folder created")
else:
	path1.rmdir()
	print("ecommerce folder deleted")
	
	
path2 = Path("anotherFolder")

print(path1.exists())
print(path2.exists())

path3 = Path()
print("\nsearch for all files .py")
for file in path3.glob('*.py'):
	print(file)


