import xlrd
from io import  open
#================ acceder texto
archivoTXT=open("archivoProfes.txt","w")

#============= acceder excel
file="C:/Users/Luis/Desktop/Software Tesis/Tesis/profes.xlsx"
Abrir= xlrd.open_workbook(file)
sheet= Abrir.sheet_by_name("Hoja1")

#============== acciones en ambos documentos
a=sheet.nrows
consulta=" "


for i in range(100):# se hace una ieracio por cada fila del excel
    if i>0:
        actual= sheet.cell_value(i, 0)# cell_value(fila columna)
        if type(actual)== float:
            actual2 = str(int(actual))
        else:
            actual2 = actual

        consulta = consulta + "shortname=" + str(actual2)+" or "
        archivoTXT.write(consulta)

print(consulta)
archivoTXT.close()