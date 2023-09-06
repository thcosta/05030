from abc import ABC, abstractmethod
# from elementos.mapa import Mapa

# classe abstrata
class Ponto(ABC):
  simbolo = ""

  def __init__(self, mapa, posicao_x, posicao_y) -> None:
    self.mapa = mapa
    self.posicao_x = posicao_x
    self.posicao_y = posicao_y
    self._aberto = False
    self._marcado = False
    self._simbolo = type(self).simbolo
  
  @property
  def mapa(self) -> int:
    return self._mapa
  
  @mapa.setter
  def mapa(self, mapa):
    self._mapa = mapa

  @property
  def posicao_x(self) -> int:
    return self._posicao_x
  
  @posicao_x.setter
  def posicao_x(self, posicao_x):
    if not isinstance(posicao_x, int) or posicao_x < 0:
        raise ValueError("posicao_x deve ser um número inteiro")
    self._posicao_x = posicao_x

  @property
  def posicao_y(self) -> int:
    return self._posicao_y
  
  @posicao_y.setter
  def posicao_y(self, posicao_y):
    if not isinstance(posicao_y, int) or posicao_y < 0:
        raise ValueError("posicao_y deve ser um número inteiro")
    self._posicao_y = posicao_y

  @property
  def simbolo(self) -> str:
    return self._simbolo
  
  def abrir(self):
    self._aberto = True
    self.desmarcar()

  def aberto(self) -> bool:
    return self._aberto == True

  def marcar(self):
    self._marcado = not self._marcado
  
  def desmarcar(self):
    self._marcado = False
  
  def marcado(self) -> bool:
    return self._marcado == True
  
  def vizinhos(self) -> list:
    vizinhos = list()
    for i in range(self.posicao_x - 1, self.posicao_x + 2):
      if i < 0 or i >= self.mapa.nivel: continue
      for j in range (self.posicao_y - 1, self.posicao_y + 2):
        if j < 0 or j >= self.mapa.nivel: continue
        if (i == self.posicao_x) and (j == self.posicao_y): continue
        vizinhos.append(self.mapa.pontos[i][j])
    return vizinhos

  def remover(self):
    self.mapa = None
    del self

  def imprimir(self):
    print(self._simbolo, end="")