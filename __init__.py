class Bvsmatrix:
    print('='*100)
    funcionario=0
    trabalhando=False
    indicado=''
    def __init__(self,f,t,i):
        self.funcionario=f
        self.trabalhando=t
        self.indicado=i
    def mostrar(self):
        print('Professor: JOSÉ ALBERTO RODRIGUES VERSÃO 1.0.3 24/09/2021:')
        print('Projetos CRUD no site do ava & sae ..: https://github.com/professorjar')
        print('C..: INSERT R..:Read U..:UPDATE   D..: DELETE')
        print('Funcionário..........................: ' + str(self.funcionario))
        estado = 'sim' if self.trabalhando else 'Não'
        print('Trabalhando..........................: ' + estado)
        print('Indicado.............................: ' + (self.indicado))
        print('Projetos..: https://professorjar.github.io/gerenciamentodeprojetos/index.html')
        print('=' *100)
fu1=Bvsmatrix(927,False,'Sim,por Morpheus')
fu1.mostrar()