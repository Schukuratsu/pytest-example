class Calculadora:
    'Funcionamento de uma calculadora básica desenvolvida para ser testada com o pytest'

    def __init__(self, valor = None):
        self.valor = valor

    def setValor(self, valor = None):
        self.valor = valor

    def getValor(self):
        return self.valor

    def printValor(self):
        print("Valor atual: " + str(self.valor))

    def __erroSemRegistro(self):
        print("Calculadora não possui um valor no registro")

    def soma(self, valor):
        if self.valor is not None:
            self.valor += valor
        else:
            self.__erroSemRegistro()

    def subtracao(self, valor):
        if self.valor is not None:
            self.valor -= valor
        else:
            self.__erroSemRegistro()

    def multiplicacao(self, valor):
        if self.valor is not None:
            self.valor *= valor
        else:
            self.__erroSemRegistro()

    def divisao(self, valor):
        if self.valor is not None:
            self.valor /= valor
        else:
            self.__erroSemRegistro()