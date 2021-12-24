class Teste():
    def __init__(self, valor): # método construtor da classe
        self.x = valor
    
    def get_valor(self):
        '''Método getter para retornar o valor do atributo x'''
        return self.x
    
    def set_valor(self, v):
        '''Método setter para atribuir um novo valor ao atributo x'''
        self.x = v
        
    
t1 = Teste(4)    
print(t1.get_valor())
t1.set_valor(5)
print(t1.get_valor())
