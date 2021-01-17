# Python3 code to rename multiple files in a directory or folder 

# importing os module 
import os 

# Function to rename a .txt file
def renameFile(filename):
		changed_fname = filename[9:]  # remove first 9 chars
		
		# rename() function will 
		# rename all the files 
		os.rename(filename, changed_fname) 



renameFile('output-1-cf-test-1-items.dat')


