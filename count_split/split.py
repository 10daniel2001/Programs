def comportamento_split():
    frse = "estou usando python"
    teste = frse.split()
    print(repr(teste))
    # Será gerado uma lista com a string acima


def contar_palavra():
    frase = "python para script, python para automaçâo"
    print("Contagem direta = ", frase.count('python')) # Apenas duas palavras
    # Método count diretamente

    contador = 0
    list_termo = frase.split()

    for linha in list_termo:
        if linha == 'python':
            contador += 1
    print("Contagem correta = ", contador)

def main():
    comportamento_split()
    contar_palavra()



if __name__=="__main__":
    main()