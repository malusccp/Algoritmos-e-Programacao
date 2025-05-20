import utils

def main():
    num1 = utils.get_integer_number_min('Número 1: ', 0)
    num2 = utils.get_integer_number_min('Número 2: ', 0)

    print(f'O MDC dos números {num1} e {num2} -> {mdc(num1,num2)}')



def mdc(num1: int, num2: int):
    if num2 == 0:
     return num1
    else:
       return mdc(num2, (num1%num2))
    
main()
    
