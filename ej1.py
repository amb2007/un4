from PIL import Image
print('ingrese la url de una imagen')
name = input()
imagen = Image.open(name)
imagen.show()
res = imagen.size
pixels = imagen.size[0] * imagen.size[1]
formato = imagen.format
ruta = imagen.filename
print(name, res, pixels, formato, ruta)
