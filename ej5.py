from PIL import Image
print('ingrese la ruta de la imagen a pegar')
namew = input()
wimage = Image.open(namew)
maxw = wimage.size
print('ingrese la ruta de la imagen en donde sera pegada la anterior')
name = input()
image = Image.open(name)
max = image.size
if max [0]< maxw[0] or max[1] < maxw[1]:
    wimage.resize((max[0]/2, max[1]/2))