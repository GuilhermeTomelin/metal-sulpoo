from models.funcionario import Funcionario
from models.setor import setor

setor1 = setor(1, "TA")
funcionario1 = Funcionario(1, "Joaquim", "Dev", 5500.00, "TI")

funcionario1.apresentar()