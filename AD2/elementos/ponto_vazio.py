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
  __abrir_vizinhos__()
    Abre os pontos vizinhos
  """
  
  simbolo = r'imagens/0.png'
  
  def abrir(self):
    """Abre o ponto e manda abrir os pontos vizinhos"""
    super().abrir()
    self.__abrir_vizinhos__()

  def __abrir_vizinhos__(self):
    """Abre os pontos vizinhos"""
    vizinhos = self.vizinhos()
    for vizinho in vizinhos:
      if (not vizinho.aberto()):
        vizinho.abrir()

