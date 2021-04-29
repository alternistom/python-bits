f = open("nameofthe.txt", "a")

for line in listToWriteToFile:
    f.write(str(line)+"\n")
        
f.close()