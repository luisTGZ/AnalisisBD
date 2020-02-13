mport time
f = open("actividades1.txt", "r")
crear= open("act2.txt","w")

while(True):
    linea2= f.readline()
    linea = linea2.split("|")
    #print(linea)
    for conteo, string  in enumerate(linea):
        if conteo <= 6:
            crear.write(string +"|")

        elif conteo == 7:
            a = True
            b=1
            for conteo2, string2 in enumerate(string):

                if conteo2 == (len(string)- 1):#cuando se llega al ultimo elemnto de la palabra de la psicion 7, el campo other
                    crear.write(string2 + "|")

                if string2 == "\"":# cambia el valor de a cuando que se encuentre unas comillas
                    a = not a
                    if b==1:
                        string2=""
                    if b==2:
                        string2 = "|"


                if (a == False): # si es el valor contario al la vez que encuentre las comillas escribe

                    crear.write(string2)
                    b=2
        elif conteo == 8:
            crear.write(string )
    if not linea2:
        break

f.close()
crear.close()