class Funcionario:
    def __init__(self,salario , nome): 
        self.salario = salario
        self.nome = nome

    def decimo_terceiro(self, meses_trabalhados):
        return meses_trabalhados / self.nome 

f = Funcionario("João", 3600)
print("13º salário:", f.decimo_terceiro(8))  # 2400.0
