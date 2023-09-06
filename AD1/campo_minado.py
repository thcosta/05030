from elementos.mapa import Mapa
from elementos.ponto import Ponto
from elementos.ponto_mina import PontoMina, ExplosaoMina
from elementos.ponto_vazio import PontoVazio
from elementos.ponto_dica import PontoDica

class CampoMinado:

  def __init__(self) -> None:
    self.mapa = None

  @property
  def mapa(self) -> int:
    return self._mapa
  
  @mapa.setter
  def mapa(self, mapa):
    self._mapa = mapa

  # @classmethod
  # def iniciar(self):
    
  def iniciar(self):
    nivel = input('Qual o nível de dificuldade desejado? ')
    self.mapa = Mapa(int(nivel))
  
  def jogar(self):
    i = 0
    valor_maximo = self.mapa.nivel
    while(self._deve_continuar()):
      i+=1
      try:
        print('\nMapa Atual:')
        self.mapa.imprimir()
        print()
        print(f'# {i} Próxima jogada...')
        coordenadas = input('Qual coordenada - no formato: x,y - do próximo ponto selecionado? ')
        x,y = map(lambda value: int(value), coordenadas.split(',')) 
        if(x < 1 or x > valor_maximo or y < 1 or y > valor_maximo):
          print('Coordenada inválida, tente novamente...\n')
          continue
        print('Qual sua próxima jogada?')
        opcao = input('Se quiser marcar digite M ou se quiser revelar digite R: ')
        if(opcao.upper() == 'M'):
          self.mapa.marcar_ponto(x-1,y-1)
        elif(opcao.upper() == 'R'):
          self.mapa.revelar_ponto(x-1,y-1)
        else:
          print('Opção inválida, tente novamente...\n')
          continue
      except ExplosaoMina as erro:
        print(erro, 'Você perdeu!')
        self.mapa.revelar()
        return
    print('Você ganhou, parabéns!\n')
    self.mapa.revelar()

  def _deve_continuar(self) -> bool:
    return self.mapa.qtd_minas_marcadas() != self.mapa.nivel

  def revelar(self):
    self.mapa.revelar()

campo_minado = CampoMinado()
campo_minado.iniciar()
# campo_minado.revelar()
campo_minado.jogar()