class Gato:
    '''Classe para trabalhar com gatos'''
    tipo_animal = 'Felino' # atributo da classe
    
    def __init__(self, nome): # método construtor da classe
        '''Inicializa o objeto capturando o nome do animal'''
        self.nome = nome
        print('Seu gatinho se chama', self.nome)
    
    def peso_gato(self, peso): # método público da classe
        self.peso = peso
        if (self.peso > 5.0)    :
            print('Seu gato está gordinho!')
        elif (self.peso > 3.5):
            print('Peso parece normal!')
        else:
            print('O animal está abaixo do peso!')
            
    def _dieta_especial_gato(self): # método privado da classe
        self.msg = 'Tudo ok!'
        if (self.peso < 3.5):
            self.msg = 'Aumente a ração do felino!'
        if (self.peso >= 5.0):
            self.msg = 'Diminua a ração do felino!'
        return self.msg
    
    def dados_gato(self):
        print('O gato', self.nome, 'está com', self.peso, 'kg.')
        print(self._dieta_especial_gato())
            
            
nome_gato = input('Digite o nome do seu gato: ')            
g1 = Gato(nome_gato)

peso = float(input('Qual o peso do seu gato, em Kg? '))
g1.peso_gato(peso)

g1.dados_gato()

# help(g1)

print(g1.tipo_animal) # variável de classe
print(g1.nome)        # variável de instância     

Gato.tipo_animal = 'Pet'  # variável de classe
print(g1.tipo_animal)
