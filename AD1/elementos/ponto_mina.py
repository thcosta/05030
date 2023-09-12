from elementos.ponto import *

__all__ = ['ExplosaoMina', 'PontoMina']

class ExplosaoMina(Exception):
  """Exceção levantada quando mina é aberta.

  Attributes
  ----------
  message : str
      explicação do erro (default 'Mina Detonada! Booommm!')
  """
  
  def __init__(self, message="Mina Detonada! Booommm!"):
      self.message = message
      super().__init__(self.message)

class PontoMina(Ponto):
  """
  Uma classe que representa um ponto do tipo mina no campo minado
  Extende a classe Ponto
  ...

  Attributes
  ----------
  simbolo : str
    simbolo * que é mostrado no mapa 

  Methods
  -------
  abrir()
    Abre o ponto e manda explodir o campo
  """
  simbolo = "*"
  
  def abrir(self):
    """Abre o ponto e manda explodir o campo"""
    self._aberto = True
    raise ExplosaoMina()