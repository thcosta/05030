from elementos.ponto_vazio import PontoVazio
from elementos.ponto_mina import PontoMina
from elementos.ponto_dica import PontoDica
import random

class Mapa:

  def __init__(self, nivel) -> None:
    self.nivel = nivel
    self._pontos = list(range(self.nivel))
    self._minas = list()
    self.montar()

  @property
  def nivel(self) -> int:
    return self._nivel
  
  @nivel.setter
  def nivel(self, nivel):
    if not isinstance(nivel, int) or nivel < 0:
        raise ValueError("nível deve ser um número inteiro")
    self._nivel = nivel
  
  @property
  def pontos(self) -> int:
    return self._pontos

  def montar(self):
    self.__iniciar_mapa_vazio()
    self.__criar_minas()
    self.__preencher_dicas()

  def imprimir(self):
    for linha in self._pontos:
      print("|", end="")
      for ponto in linha:
        if (ponto.aberto()):
          ponto.imprimir()
        elif (ponto.marcado()):
          print('X', end="")
        else:
          print(' ', end="")
        print("|", end="")
      print()

  def revelar(self):
    for linha in self._pontos:
      print("|", end="")
      for ponto in linha:
        f'{ponto.imprimir()} '
        print("|", end="")
      print()

  def qtd_minas_marcadas(self) -> int:
    minas_marcadas = list(filter(lambda mina: mina.marcado(), self._minas))
    return len(minas_marcadas)
  
  def marcar_ponto(self, posicao_x, posicao_y):
    ponto_selecionado = self.pontos[posicao_x][posicao_y]
    ponto_selecionado.marcar()
  
  def revelar_ponto(self, posicao_x, posicao_y):
    ponto_selecionado = self.pontos[posicao_x][posicao_y]
    ponto_selecionado.abrir()
  
  def __iniciar_mapa_vazio(self):
    for posicao_x in range(self.nivel):
      self._pontos[posicao_x] = list(range(self.nivel))
      for posicao_y in range(self.nivel):
        nova_ponto_vazio = PontoVazio(self, posicao_x, posicao_y)
        self._pontos[posicao_x][posicao_y] = nova_ponto_vazio
  
  def __criar_minas(self):
    i = 0
    while(i < self.nivel):
      i+=1
      posicao_x = random.randint(0, self.nivel-1)
      posicao_y = random.randint(0, self.nivel-1)
      if isinstance(self._pontos[posicao_x][posicao_y], PontoMina): 
        i-=1
        continue
      self._pontos[posicao_x][posicao_y].remover()
      nova_mina = PontoMina(self, posicao_x, posicao_y)
      self._minas.append(nova_mina)
      self._pontos[posicao_x][posicao_y] = nova_mina
  
  def __preencher_dicas(self):
    for mina in self._minas:
      self.__iniciarVizinhosMina(mina)
  
  def __iniciarVizinhosMina(self, mina):
    vizinhos = mina.vizinhos();
    for vizinho in vizinhos:
      if isinstance(vizinho, PontoVazio):
        posicao_x = vizinho.posicao_x
        posicao_y = vizinho.posicao_y
        vizinho.remover()
        self._pontos[posicao_x][posicao_y] = PontoDica(self, posicao_x, posicao_y)  


        