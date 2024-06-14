from PIL import Image
print('ingrese la ruta de la imagen')
name = input()
print('ingrese el angulo a rotar su imagen')
alpha = int(input())
imagen = Image.open(name)
imgrotada = imagen.rotate(alpha)
imgrotada.show()
imgrotada.save('toytoryRot.png')