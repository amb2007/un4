from PIL import Image
import os
lista = []
cont = 0
print('ingrese el nombre de la imagen')
name = input()
print('ingrese la posicion en x de inicio para recortar la imagen')
coordx = int(input())
lista.append(coordx)
print('ingrese la posicion en y de inicio para recortar la imagen')
coordy = int(input())
lista.append(coordy)
print('ingrese el ancho del corte')
ancho = int(input())
lista.append(ancho)
print('ingrese el largo del corte')
largo = int(input())
lista.append(largo)
tupla = tuple(lista)
imagen = Image.open(name)
imgcutted = imagen.crop(tupla)
if os.path.exists('carpeta de recortados') :
    cont = cont + 1
    os.chdir('carpeta de recortados')
    imgcutted.save(f'toytoryCut{cont}.png')
else:
    cont = cont + 1
    os.mkdir('carpeta de recortados')
    os.chdir('carpeta de recortados')
    imgcutted.save(f'toytoryCut{cont}.png')