"""
Voce deve criar uma classe carro que vai possir dois ttributsos compostos por outras duas classes
1- Motor
2- Direcao

O motor tera a responsabilidade de controlar a velocidade
Ele oferece as seguintes atributis:
1- Atributo de dado VELOCIDADE
2- O Metodo ACELERAR que devera incrementar a velocidade de uma unidade
3- Metodo FREAR que devera decrementar a velocidade em duas unidades

A direcao tera a responsabilidade de controlar a direca.
Ela oferece os seguintes atributos:
1- VALOR de direção com valores possiveis: Norte, Sul, Leste, Oeste
2- Metodo GIRAR_A_ESQUERDA que devera girar a direcao para a esquerda
3- Metodo GIRAR_A_DIREITA que devera girar a direcao para a direita

  N
O   L
  S
  Exemplo:
     # Testando motor
     >>> motor = Motor()
     >>> motor.velocidade
     0
     >>> motor.acelerar()
     >>> motor.velocidade
     1
     >>> motor.acelerar()
     >>> motor.velocidade
     2
     >>> motor.acelerar()
     >>> motor.velocidade
     3
     >>> motor.frear()
     >>> motor.velocidade
     1
     >>> motor.frear()
     >>> motor.velocidade
     0
     >>> motor.frear()
     >>> motor.velocidade

     # Testando a direcao
     >>> direcao = Direcao()
     >>> direcao.valor

     'Norte'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Leste'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Sul'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'Leste'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor
     'Norte'
     >>> direcao.girar_a_esquerda()
     >>> direcao.valor

     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     1
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     2
     >>> carro.frear()
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     'Norte'
     >>> carro.girar_a_direita()
     >>> carro.calcular_direcao()
     'Leste'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     'Norte'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
     'Oeste'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
ROTACAO_A_DIREITA_DCT = {NORTE: LESTE, LESTE: SUL, SUL: OESTE}
ROTACAO_A_ESQUERDA_DCT = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE}


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = ROTACAO_A_DIREITA_DCT[self.valor]

    def girar_a_esquerda(self):
        self.valor = ROTACAO_A_ESQUERDA_DCT[self.valor]
