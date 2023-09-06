from elementos.ponto import Ponto
from elementos.ponto_mina import PontoMina

class PontoDica(Ponto):
  def __init__(self, mapa, posicao_x, posicao_y) -> None:
    super().__init__(mapa, posicao_x, posicao_y)
    self._simbolo = f'{self.qtd_minas_vizinhas()}'

  def qtd_minas_vizinhas(self) -> int:
    vizinhos = self.vizinhos()
    qtd = 0
    for vizinho in vizinhos:
        if isinstance(vizinho, PontoMina):  
          qtd+=1
    return qtd