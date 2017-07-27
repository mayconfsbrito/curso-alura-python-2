# -*- coding: UTF-8 -*-

class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self): 
        self.saldo = self.saldo * 0.10
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus = bonus

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + self.bonus