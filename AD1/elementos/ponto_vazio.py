from elementos.ponto import Ponto

class PontoVazio(Ponto):
  simbolo = "-"
  
  def abrir(self):
    super().abrir()
    self.abrir_vizinhos()

  def abrir_vizinhos(self):
    vizinhos = self.vizinhos()
    for vizinho in vizinhos:
      if (not vizinho.aberto()):
        vizinho.abrir()

