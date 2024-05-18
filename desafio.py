def calcular_area_circunferencia(raio):
    pi = 3.14
    return pi*raio**2

if __name__ == "__main__":
    print(calcular_area_circunferencia(float(input("digite o raio:"))))