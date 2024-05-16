def boasVindas(nome, idade):
    print(" {}, ta esculhambado hein, nem parece q tu tem  {} anos".format(nome, idade))

def ePar(numero):
    if (numero%2) == 0:
        print("{} é par".format(numero))
    else:
        print("{} é impar".format(numero))
if __name__== "__main__":
    # nome = input("fala o mussarelo, qual teu nome? ")
    # idade = int(input("e tu tem quantos anos ? bixo do mato "))
    # boasVindas(nome, idade)
    
    ePar(int(input("Digite o número; ")))
