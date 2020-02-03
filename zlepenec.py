zlepenec=''
kluc=''
text=str(input('text: '))
for l in text:
    x=ord(l)
    zlepenec=str(zlepenec)+str(x)
    kluc=str(kluc)+str(len(str(x)))

print(zlepenec)
print(kluc)
counter=0
rozlepenec=''

slovo=""
for l in range(len(str(kluc))):
    for i in range(int(kluc[l])):
        rozlepenec=str(rozlepenec)+str(zlepenec[counter])
        counter=counter+1
    char=chr(int(rozlepenec))
    rozlepenec=""
    slovo=slovo+str(char)
print(slovo)

done = input('done')

window.mainloop()
