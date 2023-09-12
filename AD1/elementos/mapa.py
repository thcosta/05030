from elementos.ponto_vazio import *
from elementos.ponto_mina import *
from elementos.ponto_dica import *
import random

__all__ = ['Mapa']

class Mapa:
  """
  Uma classe que representa o mapa do campo minado

  ...

  Attributes
  ----------
  nivel : int
    representa a dificuldade do mapa, número de minas e tamanho da matriz quadrada de pontos 
  _pontos : list(list)
    matriz de pontos do campo minado

  Methods
  -------
  montar()
    Cria os pontos do campo minado, podendo ser pontos do tipo mina, dica ou vazio
  imprimir()
    Mostra o mapa do campo minado mostrando apenas os pontos abertos
  revelar()
    Mostra o mapa do campo minado mostrando todos os pontos
  qtd_minas_descobertas()
    Retorna a quantidade de minas marcadas
  marcar_ponto(posicao_x, posicao_y)
    Marca o ponto do campo minado da coordenada x,y
  revelar_ponto(posicao_x, posicao_y)
    Abre o ponto do campo minado da coordenada x,y
  __minas()
    Retorna os pontos que são mina do mapa do campo minado
  __iniciar_mapa_vazio()
    Preenche todo o mapa do campo minado com os pontos do tipo vazio
  __criar_minas()
    Cria aleatoriamente as minas no mapa do campo minado
  __preencher_dicas()
    Cria, para cada mina do campo minado, os pontos do tipo dica que são vizinhos da mina
  """

  def __init__(self, nivel) -> None:
    """
    Parameters
    ----------
    nivel : int
      Representa a dificuldade do mapa, número de minas e tamanho da matriz quadrada de pontos
    _pontos : list(list)
      Matriz de pontos do campo minado
    """
    self.nivel = nivel
    self._pontos = list(range(self.nivel))
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
    """Cria os pontos do campo minado, podendo ser pontos do tipo mina, dica ou vazio"""
    self.__iniciar_mapa_vazio()
    self.__criar_minas()
    self.__preencher_dicas()

  def imprimir(self):
    """Mostra o mapa do campo minado mostrando apenas os pontos abertos"""
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
    """Mostra o mapa do campo minado mostrando todos os pontos"""
    for linha in self._pontos:
      print("|", end="")
      for ponto in linha:
        f'{ponto.imprimir()} '
        print("|", end="")
      print()

  def qtd_minas_descobertas(self) -> int:
    """Retorna a quantidade de minas marcadas
    Returns
    ----------
    int
      número de minas marcadas
    """
    minas_descobertas = list(filter(lambda mina: (mina.marcado()), self.__minas()))
    return len(minas_descobertas)
  
  def marcar_ponto(self, posicao_x, posicao_y):
    """Marca o ponto do campo minado da coordenada x,y
    Parameters
    ----------
    posicao_x : int
      A coordenada x do ponto
    posicao_y : int
      A coordenada y do ponto
    """
    ponto_selecionado = self.pontos[posicao_x][posicao_y]
    ponto_selecionado.marcar()
  
  def revelar_ponto(self, posicao_x, posicao_y):
    """Abre o ponto do campo minado da coordenada x,y
    Parameters
    ----------
    posicao_x : int
      A coordenada x do ponto
    posicao_y : int
      A coordenada y do ponto
    """
    ponto_selecionado = self.pontos[posicao_x][posicao_y]
    ponto_selecionado.abrir()

  def __minas(self) -> list:
    """Retorna os pontos que são mina do mapa do campo minado
    Returns
    -------
    list
      a lista de minas do campo minado
    """
    pontos = list(coluna for linha in self._pontos for coluna in linha)
    return list(filter(lambda ponto: isinstance(ponto, PontoMina), pontos))
  
  def __iniciar_mapa_vazio(self):
    """Preenche todo o mapa do campo minado com os pontos do tipo vazio"""
    for posicao_x in range(self.nivel):
      self._pontos[posicao_x] = list(range(self.nivel))
      for posicao_y in range(self.nivel):
        nova_ponto_vazio = PontoVazio(self, posicao_x, posicao_y)
        self._pontos[posicao_x][posicao_y] = nova_ponto_vazio
  
  def __criar_minas(self):
    """Cria aleatoriamente as minas no mapa do campo minado"""
    i = 0
    while(i < self.nivel):
      i+=1
      posicao_x = random.randint(0, self.nivel-1)
      posicao_y = random.randint(0, self.nivel-1)
      if isinstance(self._pontos[posicao_x][posicao_y], PontoMina): 
        i-=1
        continue
      self._pontos[posicao_x][posicao_y] = PontoMina(self, posicao_x, posicao_y)
  
  def __preencher_dicas(self):
    """Cria, para cada mina do campo minado, os pontos do tipo dica que são vizinhos da mina"""
    for mina in self.__minas():
      vizinhos = mina.vizinhos();
      for vizinho in vizinhos:
        if isinstance(vizinho, PontoVazio):
          posicao_x = vizinho.posicao_x
          posicao_y = vizinho.posicao_y
          self._pontos[posicao_x][posicao_y] = PontoDica(self, posicao_x, posicao_y)
        