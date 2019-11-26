import pytest
from Calculadora_v1 import Calculadora

def testGetUnsetValue():
    calc = Calculadora()
    assert calc.getValor() == None

def testUnsetValue():
    calc = Calculadora()
    calc.soma(1)

def testSoma():
    calc = Calculadora(50)
    calc.soma(5)
    assert calc.getValor() == 55

def testSubtracao():
    calc = Calculadora(88)
    calc.subtracao(17)
    assert calc.getValor() == 71

def testMultiplicacao():
    calc = Calculadora(3)
    calc.multiplicacao(15)
    assert calc.getValor() == 45

def testDivisao():
    calc = Calculadora(10)
    calc.divisao(5)
    assert calc.getValor() == 2

def testDivisionByZero():
    calc = Calculadora(10)
    calc.divisao(0)