from elementos.ponto import *
from elementos.ponto_mina import *

__all__ = ['PontoDica']

class PontoDica(Ponto):
  """
  Uma classe que representa um ponto do tipo dica no campo minado
  Extende a classe Ponto
  ...

  Attributes
  ----------
  simbolo : str
    simbolo N que é mostrado no mapa, onde N é o número de minas vizinhas ao ponto

  Methods
  -------
  __qtd_minas_vizinhas()
    Retorna a quantidade de minas vizinhas ao ponto
  """
  
  def __init__(self, mapa, posicao_x, posicao_y) -> None:
    super().__init__(mapa, posicao_x, posicao_y)
    self._simbolo = f'{self.__qtd_minas_vizinhas()}'

  def __qtd_minas_vizinhas(self) -> int:
    """Retorna a quantidade de minas vizinhas ao ponto
    Returns
    ----------
    int
      número de minas vizinhas
    """
    minas = list(filter(lambda vizinho: isinstance(vizinho, PontoMina), self.vizinhos()))
    return len(minas)