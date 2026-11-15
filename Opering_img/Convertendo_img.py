# Pillow para abrir imagens
# Numpy para convert em array

from PIL import Image
import numpy as np

# Image.open para abrir a imagem ou o caminho ate ela !
img = Image.open("teste_img.jpg")
img.show() # mostrar a imagem

# Converte a imagem em dados binarios
img_data = np.array(img)
img_binary = img_data.tobytes()

# Salvar os dados binaríos em um arquivo
with open("original_binary.bin", "wb") as file:
    file.write(img_binary)

# Copiar o arquivo binario
with open("original_binary.bin", "rb") as orig_file:
    data = orig_file.read()



