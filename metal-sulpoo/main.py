from models.funcionario import Funcionario
from models.setor import Setor

setor1 = Setor(1, "TA")
funcionario1 = Funcionario(1, "Joaquim", "Dev", -5500.00,setor1)
print("-"*30)
setor1.nome = "Tech"
setor1.apresentar

#COMPOSIÇÃO
#funcionario possui um setor
#produto possui um fornecedor
#produto pertence a um setor
#HERANÇA
#Gerente é um funcionario
#Supervisor é um funcionario
#ADM é um funcionario