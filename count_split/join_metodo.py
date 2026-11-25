
def  frase():
    texto = ["Lista", "De", "Compras", "Para o ano novo"]
    # Criei uma lesta de string
    etxt = ', '.join(texto) # Join receber a variavel com a lista de string, como parâmetro

    with open("test_join.txt", "w") as file: # Funçâo open para o arquivo txt
        file.write(etxt)

    print("\n")

    etct2 = "\n".join(texto)
    with open("test_join2.txt", "w") as dfile:
        dfile.write(etct2)

def main():
    frase()




if __name__=="__main__":
    main()
