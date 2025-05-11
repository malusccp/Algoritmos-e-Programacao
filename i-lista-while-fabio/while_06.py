import uteis
def main():
    tabuada = 1
    comeco = 1
    final = 10
    uteis.linhas()
    escrever_tabuada(tabuada, comeco, final)

def escrever_tabuada(tabuada: int, comeco: int, final: int):
    while comeco <= final:
        print(f' TABUADA DO {comeco} ')
        while tabuada <= final:
            resultado = comeco * tabuada
            print(f'{comeco} x {tabuada} = {resultado}')

            tabuada += 1
        uteis.linhas()
        tabuada = 1
        comeco += 1



main()