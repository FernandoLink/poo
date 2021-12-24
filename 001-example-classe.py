class Cubo: # cabeçalho da classe
    ''' Classe para calcular o cubo de um número '''
    # pass -> classe sem nenhuma função
    def __init__(self, valor): # método construtor da classe
        self.x = valor
        print('Objeto criado!')
    def calcula_cubo(self): 
        cubo = self.x * self.x * self.x
        return 'Cubo calculado ' + str(cubo)


teste = Cubo(10) # instanciar a classe
print(type(teste))
print(type(Cubo))
print(type(teste.__init__))
print(teste.calcula_cubo()) # chamada do método da instância da classe teste
