import os
import sys

os.chdir(".\micro-jardines\Catalogo" )
print(str(os.listdir()))

while True:
    folderName = str(input("Enter product folder name: "))
    print('./' + folderName)
    if os.path.exists(folderName):
        break
    else:
        print("Please enter a valid director!")
  
print('Succes')
#Create .html file in corresponding media dir


#Paste HTML template 

#Define variables for file 
    #folderName = ""
    #templateFile = ""
    #displayName = ""
    #thumnailImg-src = ""
    #sildeshowImg-src = ""
    #htmlFileName = ""

#Sub in values in product page

#Sub in reference values in cataloge.html
