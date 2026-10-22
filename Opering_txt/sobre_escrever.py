def main():
       print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
       frases = []
       while True:
              entrada = input(">  ")
              if entrada.lower() == "sair":
                     break
              frases.append(entrada)

       with open("dss,txt", "w") as arquivo:
              for frase in frases:
                     arquivo.write(frase + "\n")
        
       print("Arquivo original criado. Agora vamos manipular os dados.")  

       dados_alterado = []
       with open("dss.txt", "r") as arquivos:
              for linha in arquivos:
                     dados_alterado.append(linha.strip().upper())



if __name__=="__main__":
       main()