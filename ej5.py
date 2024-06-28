from PIL import Image
namew = input('ingrese la ruta de la imagen a pegar \n')
wimage = Image.open(namew)
name = input('ingrese la ruta de la imagen en donde sera pegada la anterior \n')
image = Image.open(name)
print(image.size)
wimage.resize((30, 30))
posicion = int(input('elija una posicion arriba a la izquiera(1), arriba a la derecha(2), abajo a la izquierda(3), abajo a la derecha(4) \n'))
if posicion == 1:
    image.paste(wimage, (0,0))
elif posicion == 2:
    image.paste(wimage, (image.size[0]-wimage.size[0],0))
elif posicion == 3:
    image.paste(wimage, (0,image.size[1]-wimage.size[1]))
elif posicion == 4:
    image.paste (wimage,(image.size[0]-wimage.size[0],image.size[1]-wimage.size[1]))
image.show()