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
        if self.checkValor():
            self.valor += valor

    def subtracao(self, valor):
        if self.checkValor():
            self.valor -= valor

    def multiplicacao(self, valor):
        if self.checkValor():
            self.valor *= valor

    def divisao(self, valor):
        if self.checkValor():
            try:
                self.valor /= valor
            except ZeroDivisionError:
                print("Não pode dividir por zero.")

    def checkValor(self):
        if self.valor is not None:
            return True
        else:
            self.__erroSemRegistro()
            return False