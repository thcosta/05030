from abc import ABC, abstractmethod
# from elementos.mapa import Mapa

__all__ = ['Ponto']

# classe abstrata
class Ponto(ABC):
  """
  Uma classe abstrata que representa um ponto no mapa do campo minado

  ...

  Attributes
  ----------
  mapa : Mapa object
    o mapa do campo minado no qual o ponto está localizado
  posicao_x : int
    a coordenada x do ponto no mapa
  posicao_y : int
    a coordenada y do ponto no mapa
  _aberto : bool
    representa se o ponto está aberto (True) ou não (False)
  _marcado : bool
    representa se o ponto está marcado (True) ou não (False)
  _simbolo : str
    é símbolo mostrado quando o ponto está aberto no mapa

  Methods
  -------
  abrir()
    Seta o ponto como aberto
  aberto()
    Verifica se o ponto está aberto
  marcar()
    Seta o ponto como marcado
  marcado()
    Verifica se o ponto está marcado
  vizinhos()
    Retorna os vizinhos do ponto
  imprimir()
    Imprime o símbolo do ponto
  """
    
  simbolo = ""

  def __init__(self, mapa, posicao_x, posicao_y) -> None:
    """
    Parameters
    ----------
    mapa : Mapa object
      O mapa do campo minado no qual o ponto está localizado
    posicao_x : int
      A coordenada x do ponto no mapa
    posicao_y : int
      A coordenada y do ponto no mapa
    _aberto : bool
      Representa se o ponto está aberto (True) ou não (False)
    _marcado : bool
      Representa se o ponto está marcado (True) ou não (False)
    _simbolo : str
      É símbolo mostrado quando o ponto está aberto no mapa
    """
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
    """Seta o ponto como aberto e desmarcado

    Raises
    ------
    ValueError
      Se o ponto já estiver aberto, retorna erro 'Ponto já revelado!'
    """
    if (not self._aberto):
      self._aberto = True
      self._marcado = False
    else:
      raise ValueError("Ponto já revelado!")

  def aberto(self) -> bool:
    """Verifica se o ponto está aberto
    Returns
    ----------
    bool
      representa se o ponto está aberto (True) ou não (False)
    """
    return self._aberto == True

  def marcar(self):
    """Seta o ponto como marcado ou desmarcado

    Raises
    ------
    ValueError
      Se o ponto já estiver aberto, retorna erro 'Ponto já revelado!'
    """
    if (not self._aberto):
      self._marcado = not self._marcado
    else:
      raise ValueError("Ponto já revelado!")
  
  def marcado(self) -> bool:
    """Verifica se o ponto está marcado
    Returns
    ----------
    bool
      representa se o ponto está marcado (True) ou não (False)
    """
    return self._marcado == True
  
  def vizinhos(self) -> list:
    """Retorna os pontos vizinhos
    Returns
    ----------
    list
      lista de pontos vizinhos
    """
    vizinhos = list()
    for i in range(self.posicao_x - 1, self.posicao_x + 2):
      if i < 0 or i >= self.mapa.nivel: continue
      for j in range (self.posicao_y - 1, self.posicao_y + 2):
        if j < 0 or j >= self.mapa.nivel: continue
        if (i == self.posicao_x) and (j == self.posicao_y): continue
        vizinhos.append(self.mapa.pontos[i][j])
    return vizinhos

  def imprimir(self):
    """Imprime o símbolo do ponto"""
    print(self._simbolo, end="")