from models.funcionario import Funcionario
from models.setor import Setor

setor1 = Setor(1,"TA")
funcionario1 = Funcionario(1,"Joaquim","Dev",10.00,setor1)

funcionario1.aumentar_salario(100)
funcionario1.apresentar()

