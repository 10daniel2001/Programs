# Pillow para abrir imagens
# Numpy para convert em array

from PIL import Image
import numpy as np

def main():
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


    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)

    # Manipulação dos dados do arquivo binário cópia
    # Exemplo: Inverter os bytes

    with open("copy_img.bin", "rb") as fll:
        data = bytearray(fll.read())

    # Inverte todos os bytes
    dataa = data[::-1]

    with open("copy_img.bin", "wb") as fild:
        fild.write(dataa)


    modificando_dados = np.frombuffer(dataa, dtype=np.uint8).reshape(img_data.shape)
    modifi_img = Image.fromarray(modificando_dados)

    # Após iniciar este codigo algumas abas do navegador será aberta, uma conténdo a imagem original
    # A outra com a imagem modficada por este codigo

if __name__=="__main__":
    main()