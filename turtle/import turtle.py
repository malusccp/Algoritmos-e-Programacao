import turtle

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("lightpink")  # Cor de fundo da tela

# Criando a tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(10)

# Função para desenhar um coração
def desenhar_coracao():
    tartaruga.color("red")
    tartaruga.begin_fill()
    tartaruga.left(50)
    tartaruga.forward(133)
    tartaruga.circle(50, 200)  # Cria a parte curva do coração
    tartaruga.right(140)
    tartaruga.circle(50, 200)  # Cria a outra parte curva
    tartaruga.forward(133)
    tartaruga.end_fill()

# Função para escrever o nome "Luna" dentro do coração
def escrever_nome():
    tartaruga.penup()
    tartaruga.goto(0, -50)  # Posiciona a tartaruga para escrever
    tartaruga.pendown()
    tartaruga.color("white")
    tartaruga.write("Dudu e ElenTV", align="center", font=("Arial", 30, "bold"))

# Desenhando o coração
tartaruga.penup()
tartaruga.goto(0, -100)  # Posiciona para o coração
tartaruga.pendown()
desenhar_coracao()

# Escrevendo o nome "Luna"
escrever_nome()

# Finalizando
tartaruga.hideturtle()
turtle.done()