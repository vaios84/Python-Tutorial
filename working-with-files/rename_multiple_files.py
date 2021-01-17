# Python3 code to rename multiple files in a directory or folder 

# importing os module 
import os 
import os.path
import pathlib
from os import path

# Function to rename a .txt file
def renameFile(filename):
		changed_fname = filename[9:]  # remove first 9 chars 
		file = pathlib.Path(filename)
		if file.exists():
			os.rename(filename, changed_fname)
			print('file renamed')
		else:
			print('file not found')


for i in range(1,4):
		renameFile('output-' + str(i) + '-cf-train-10-users.dat')
		renameFile('output-' + str(i) + '-cf-train-1-users.dat')
		renameFile('output-' + str(i) + '-cf-test-10-users.dat')
		renameFile('output-' + str(i) + '-cf-test-1-users.dat')
		renameFile('output-' + str(i) + '-cf-train-10-items.dat')
		renameFile('output-' + str(i) + '-cf-train-1-items.dat')
		renameFile('output-' + str(i) + '-cf-test-10-items.dat')
		renameFile('output-' + str(i) + '-cf-test-1-items.dat') 





