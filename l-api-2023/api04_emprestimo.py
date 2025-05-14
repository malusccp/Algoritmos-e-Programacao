# 4. [empréstimo.js] João precisa de um dinheiro emprestado para
# comprar um Notebook para estudar programação. Para isso, foi ao
# RSBank fazer uma simulação. As taxas de empréstimo do banco
# obedecem à regra dos Juros Compostos Mensais, ou seja, o valor é
# calculado cumulativamente mês a mês, ou seja, aplica-se os juros
# sobre o valor total no primeiro mês e esse passa a ser a base para o
# segundo mês.
# Porém a taxa de juros aplicada é calculada de acordo com o prazo
# de parcelamento (vide tabela) e à SELIC, atualmente em 13,75%
# (abril/2023). O usuário só pode parcelar o empréstimo em até 24x
# (min. 2 parcelas). Valor mínimo de empréstimo é de um salário
# mínimo. Valor máximo de parcela é 40% da Renda Mensal do
# Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre
# Operações Financeiras) pago ao Governo Federal antes de aplicar
# os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor
# total (independente do prazo) + 0,0082% por cada dia do prazo do
# empréstimo. Considere todos os meses com 30 dias. Os juros são
# aplicados sobre o valor a ser recebido pelo Cliente + IOF

# Prazo         Taxa
# Até 6x        50% da SELIC
# de 7x a 12x   75% da SELIC
# de 12x a 18x  100% da SELIC
# Acima de 18x  130% da SELIC

# ● Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
# desejados, valide os dados a serem recebidos.
# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO (se a
# renda mensal suporta a parcela)