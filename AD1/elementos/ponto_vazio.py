from elementos.ponto import *

__all__ = ['PontoVazio']

class PontoVazio(Ponto):
  """
  Uma classe que representa um ponto do tipo vazio no campo minado
  Extende a classe Ponto
  ...

  Attributes
  ----------
  simbolo : str
    simbolo - que é mostrado no mapa 

  Methods
  -------
  abrir()
    Abre o ponto e manda abrir os pontos vizinhos
  __abrir_vizinhos()
    Abre os pontos vizinhos
  """
  
  simbolo = "-"
  
  def abrir(self):
    """Abre o ponto e manda abrir os pontos vizinhos"""
    super().abrir()
    self.__abrir_vizinhos()

  def __abrir_vizinhos(self):
    """Abre os pontos vizinhos"""
    vizinhos = self.vizinhos()
    for vizinho in vizinhos:
      if (not vizinho.aberto()):
        vizinho.abrir()

