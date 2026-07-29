from models.funcionario import Funcionario
from models.setor import Setor

setor1 = Setor(1, "TA")
funcionario1 = Funcionario(1, "Joaquim", "Dev", -5500.00,setor1)
print("-"*30)
setor1.nome = "Tech"
setor1.apresentar
#Parece que estamos acessando o atributo diretamente
#Entretanto o python executa o método definido @nome.setter
#Permitindo que ocorra validações
setor1.nome = "" #devolve erro