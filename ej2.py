from PIL import Image
import os
cont = 0
imagen = Image.open('toytory.png')
imagen.show()

if os.path.exists('toytory.png') :
    cont = cont + 1
    imagen.save(f'toytory{cont}.png')