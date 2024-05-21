def criararquivo():

    frase = input("Digite a frase: ")
    with open("arquivo.txt", "w") as file:
        file.write (frase)

print("arquivo criado com exito")

criararquivo()