from abc import ABC, abstractmethod
class Endereco(ABC):
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado
    def get_cidade(self):
        return self.cidade
    def set_cidade(self,nova_cidade):
        self.cidade = nova_cidade
        return self.cidade
    def get_estado(self):
        return self.estado
    def set_estado(self,novo_estado):
        self.estado = novo_estado
        return self.estado

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self,nova_idade):
        self.idade = nova_idade
    def insere_endereco(self,endereco):
        self.enderecos.append(endereco)
    def mostra_enderecos(self):
        if len(self.enderecos) <= 0:
            print("Sem endereço cadastrado")
        else:
            print(self.nome)
            for endereco in self.enderecos:
                print(f"{endereco.get_cidade()}, {endereco.get_estado()}")
    def remove_endereco(self,cidade):
        for endereco in self.enderecos:
            if endereco.get_cidade() == cidade:
                self.enderecos.remove(endereco)
            else:
                print("Input inválidado")

if __name__ == "__main__":
    cliente1 = Cliente("Edu", 30)
    endereco1 = Endereco("Carlândia","Goiás")
    endereco2 = Endereco("Brasília","Distrito Federal")
    cliente1.insere_endereco(endereco1)
    cliente1.insere_endereco(endereco2)
    cliente1.mostra_enderecos()
    cliente1.remove_endereco("Carlândia")
    cliente1.mostra_enderecos()











