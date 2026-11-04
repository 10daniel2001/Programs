arquivo = open("dss.txt", "r")

conteudo = arquivo.read()

print("Lendo o conteudo ")
print(repr(conteudo)) # Printando o conteúdo do txt

arquivo.close()

reeler = open("dss.txt", "r")

outra_leitura = reeler.readline()

print("Lendo linhas")
print(repr(outra_leitura))