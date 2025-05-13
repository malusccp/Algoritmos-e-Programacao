import utils

def main():
    turno = utils.string('Digite o turno que o aluno estuda: ')

    if turno.upper() == 'M':
        return print('Bom dia!')
    if turno.upper() == 'V':
        return print('Boa tarde!')
    if turno.upper() == 'N':
        return print('Boa noite!')
    else:
        return print('Valor Inválido!')
    
main()