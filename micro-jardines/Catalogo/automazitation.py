import os
import sys
from shutil import copy, copyfile
import fileinput


print(str(os.listdir()))

while True:
    folderName = str(input("Enter product folder name: "))
    if os.path.exists("./micro-jardines/Catalogo/Media/" + folderName):
        break
    else:
        print("Please enter a valid director!")





workingDirectory = "./micro-jardines/Catalogo/Media/" + folderName 

print(str(os.listdir(workingDirectory)))


#Define variables for file 
    #folderName
    #workingDirectory
    #templateFile = ""
    #displayName = ""
    #thumnailImg-src = ""
    #sildeshowImg-src = ""
    #htmlFileName

#Create .html file in corresponding media dir

copyfile("./micro-jardines/Catalogo/template.html", workingDirectory + "/" + folderName + ".html")

#Sub in values in product page
os.chdir(workingDirectory)
open(folderName + ".html")
#Create slideshow for each img

#Create button for each img

#Sub in reference values in cataloge.html
