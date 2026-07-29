from models.funcionario import Funcionario
from models.setor import setor

setor1 = setor(1, "TA")
funcionario1 = Funcionario(1, "Joaquim", "Dev", 5500.00, "TI")
funcionario1.apresentar()

#COMPOSIÇÃO
#funcionario possui um setor
#produto possui um fornecedor
#produto pertence a um setor
#HERANÇA
#Gerente é um funcionario
#Supervisor é um funcionario
#ADM é um funcionario