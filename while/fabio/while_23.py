import uteis

def main():
    n = uteis.get_integer_number_min("Digite a quantidade de funcionários: ", 0)
    print(">>>>>> FICHA DOS FUNCIONÁRIOS <<<<<<")

    uteis.linhas()
    ler_funcionarios(n)

 
def ler_funcionarios(n:int) -> float:
    contador = 0
    while contador < n:
     codigo_func = uteis.get_integer_number_min("Digite o código do funcionário: ", 0)

     horas_trabalhadas = uteis.get_integer_number_min("Digite a quantidade de horas trabalhadas: ", 1)
     dependentes = uteis.get_integer_number_min("Digite a quantidade de dependentes financeiros: ", 0)
     contador += 1
     print(f"Código funcionário:{codigo_func}\nHoras trabalhadas: {horas_trabalhadas}\nDependentes: {dependentes}")
     uteis.linhas()
     calcular_salario_liquido(horas_trabalhadas, dependentes)
     uteis.linhas()
     
    
def calcular_salario_liquido(horas_trabalhadas: int, dependentes: int) -> float:
   salario_bruto = (12 * horas_trabalhadas) + (40 * dependentes)
   desconto_inss = salario_bruto * 0.085
   desconto_ir = salario_bruto * 0.05
   salario_liquido = ((salario_bruto * 0.915) * 0.95)
   print(f"Descontos:\nINSS: {desconto_inss:.2f}\nIR: {desconto_ir: .2f}") 
   print(f"SALÁRIO LÍQUIDO: {salario_liquido:.2f}")




main()
