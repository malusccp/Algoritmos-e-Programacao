def main():
    senha = obter_senha('Digite a senha escolhida: ')
    if oito_caracteres(senha) and tem_maiuscula(senha) and tem_minuscula(senha) and numero(senha) and caracteres_especiais(senha):
        print(f'{senha} é válida')
    else:
        print(f'{senha} é inválida. Tente novamente')
        return main()


def obter_senha(label:str):
    return input(label)

def oito_caracteres(senha):
    caracteres = 0
    for caractere in senha:
         caracteres = caracteres + 1
    if caracteres >= 8:
        return True
    else:
        return False
    
def tem_maiuscula(senha):
    for letra in senha:
        if letra >= 'A' and letra <= 'Z':
            return True
    return False

def tem_minuscula(senha):
    for letra in senha:
         if letra >= 'a' and letra <= 'z':
             return True
    return False

def numero(senha):
    for letra in senha:
        if letra >= '0' and letra <= '9':
            return True
    return False

def caracteres_especiais(senha):
    especiais = '!@#$%&*'
    for letra in senha:
        if letra in especiais:
            return True
    
main()