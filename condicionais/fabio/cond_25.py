def main():
    senha = obter_senha('Digite a senha: ')
    acesso_usuario(senha)


def obter_senha(label:str):
    return str(input(label))


def acesso_usuario(senha):
    if senha == '1234':
        print('Senha correta. Acesso liberado.')
    else:
        print('Senha incorreta. Acesso negado.')

main()