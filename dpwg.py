import sys
import os

inputFile = sys.argv[1]

# Read targetDomains and serialize them into an array by cutting them off after "." -> www.example.com -> ['www', 'example', 'com']

with open(inputFile, "r") as file:
    fileContent = file.read()
    wordsArray = fileContent.split(".")
    uniqueWordsArray = list(dict.fromkeys(wordsArray))

# Write to outputFile 

with open("dpwgOutput.txt", "w") as file:
    for i in range(len(uniqueWordsArray)):
       file.write(uniqueWordsArray[i] + "\n") 


# Read  outputFile and for every line(word) that contains "-" -> split it, creating new entries: testing-example --> ['testing', 'example']

with open("dpwgOutput.txt", "r") as file:
    uniqueWordsArray2 = [] 
    for line in file:
        if "-" in line:
            wordsArray = line.split("-")
            uniqueWordsArray2 += wordsArray

# Append the rest to the same outputFile

with open("dpwgOutput.txt", "a") as file:
    for i in range(len(uniqueWordsArray2)):
        if "\n" not in uniqueWordsArray2[i]:
            file.write(uniqueWordsArray2[i] + "\n")
        else:
            file.write(uniqueWordsArray2[i])


# Remove duplicates and handle outputFile

os.system("cat dpwgOutput.txt | duplicut -o final")
os.system("cat final > dpwgOutput.txt && rm final")
