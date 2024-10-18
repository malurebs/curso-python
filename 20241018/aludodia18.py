#condig: utf-8
#cauculo de combustível

def cauculocombustivel():
    tempo_gasto = int(input())
    velocidade_media= int(input())
    consumo = (tempo_gasto*velocidade_media)/12
    print("{0:.3f})".format(consumo))


if __name__ == "__main__":
    cauculocombustivel()