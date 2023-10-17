import tkinter as tk

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
  frame_grid: tk.Frame object
    o frame do grid onde o ponto está vinculado
  frame: tk.Frame object
    o frame do ponto
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
  """
    
  simbolo = ""

  def __init__(self, mapa, posicao_x, posicao_y, frame_grid) -> None:
    """
    Parameters
    ----------
    mapa : Mapa object
      O mapa do campo minado no qual o ponto está localizado
    frame_grid: tk.Frame object
      O frame do grid onde o ponto está vinculado
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
    self.frame_grid = frame_grid
    self._aberto = False
    self._marcado = False
    self._simbolo = type(self).simbolo
    self.__construir_frame__()
  
  @property
  def mapa(self) -> object:
    return self._mapa
  
  @mapa.setter
  def mapa(self, mapa):
    self._mapa = mapa
  
  @property
  def frame(self) -> object:
    return self._frame
  
  @frame.setter
  def frame(self, frame):
    self._frame = frame

  @property
  def simbolo(self) -> str:
    return self._simbolo

  def posicao_x(self) -> int:
    return self.frame.posicao_x

  def posicao_y(self) -> int:
    return self.frame.posicao_x

  def mostrar(self):
    """Mostra o conteúdo do ponto na janela"""
    frame = self.frame
    imagem = tk.PhotoImage(file=self.simbolo)
    frame.imagem = imagem
    frame.botao.unbind("<Button-1>")
    campoImagem = tk.Label(**{"anchor": "center", "master": frame.botao, "image": imagem })
    campoImagem.pack()
  
  def abrir(self):
    """Seta o ponto como aberto e desmarcado"""
    if (not self._aberto):
      self._aberto = True
      self._marcado = False
      self.mostrar()
  
  def fechar(self):
    """Seta o ponto como fechado e desmarcado, ocultando o conteúdo do ponto"""
    self._aberto = False
    self._marcado = False
    self.frame.grid_remove()
    self.__construir_frame__()

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

  def __construir_frame__(self):
    """Constroi e adiciona o ponto na janela com o conteúdo oculto"""
    self.frame = tk.Frame(master=self.frame_grid, width=65, height=65)
    self.frame.grid(row=self.posicao_x, column=self.posicao_y)
    imagem = tk.PhotoImage(file='imagens/vazio.png')
    self.frame.imagem = imagem
    self.frame.botao = tk.Button(**{
      "fg": "white",
      "compound": "right",
      "activeforeground": "white",
      "relief": tk.RIDGE,
      "master": self.frame,  
      "image": imagem, 
      "width": 65, 
      "height": 65
    })
    self.frame.botao.pack()