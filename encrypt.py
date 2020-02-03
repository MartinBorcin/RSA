#message = open("message.txt", "w")
text=str(input("Your message: "))
#message.write(text)
#message.close()

encryptedMessage = open("encryptedMessage.txt", "w")
encryptedMessage.write('')
encryptedMessage.close()

public = open("public_key.txt", "r")
def encrypt(x):
    return(pow(int(x),int(e),int(n)))
        
for i, line in enumerate(public):
    if i == 0:
        e = line
    elif i == 1:
        n = line
        break
public.close()

encryptedMessage = open ("encryptedMessage.txt", "a")
zlepenec=''
kluc=''
#print(len(text))
counter=0
for l in text:
    x=ord(l)
    zlepenec=str(zlepenec)+str(x)
    kluc=str(kluc)+str(len(str(x)))
    counter=counter+1
    if counter == 64:
#        print(zlepenec, "\n")
#        print(kluc, "\n")
        zlepenec=encrypt(zlepenec)
        kluc2=encrypt(kluc)
#        print("main: ", zlepenec, "\n")
        encryptedMessage.write(str(zlepenec) + "\n")
#        print("main: ", kluc2, "\n")
        encryptedMessage.write(str(kluc2)+'\n')
        zlepenec=''
        kluc = ''
        counter=0

#print(zlepenec, "\n")
#print(kluc, "\n")
zlepenec=encrypt(zlepenec)
kluc2=encrypt(kluc)
#print("zbytok: ", zlepenec, "\n")
encryptedMessage.write(str(zlepenec) + "\n")
#print("zbytok: ", kluc2, "\n")
encryptedMessage.write(str(kluc2))

encryptedMessage.close()

done = input('Your message has been successfully encrypted!')
