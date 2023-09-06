from elementos.ponto import Ponto

class ExplosaoMina(Exception):
    """Exceção levantada quando mina é aberta.

    Attributes:
        message -- explicação do erro
    """

    def __init__(self, message="Mina Detonada! Booommm!"):
        self.message = message
        super().__init__(self.message)

class PontoMina(Ponto):
  simbolo = "*"

  def __init__(self, mapa, posicao_x, posicao_y) -> None:
    super().__init__(mapa, posicao_x, posicao_y)
    self._simbolo = type(self).simbolo

  def abrir(self):
    self._aberto = True
    raise ExplosaoMina()