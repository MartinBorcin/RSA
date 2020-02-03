private = open("private_key.txt", "r")
encryptedMessage = open("encryptedMessage.txt", "r")

def decrypt(x):
    return(pow(int(x), int(d), int(n)))
           
for i, line in enumerate(private):
    if i == 0:
        d = line
    elif i == 1:
        n = line
        break
private.close()

counter=0
rozlepenec=''
slovo=''
zlepenec=''
kluc=''
for i, line in enumerate(encryptedMessage):
    if i % 2 == 0:
        zlepenec = zlepenec + str(decrypt(line))
##        print(zlepenec)
##        print(len(kluc))

    elif i % 2 == 1:
        kluc = kluc + str(decrypt(line))
##        print(kluc)
##        print(len(kluc))
        
for l in range(len(str(kluc))):
    for i in range(int(kluc[l])):
        rozlepenec=str(rozlepenec)+str(zlepenec[counter])
        counter=counter+1
    char=chr(int(rozlepenec))
    rozlepenec=""
    slovo=slovo+str(char)
print(slovo)


done=input('\ndone!')

