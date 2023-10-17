from elementos import *
import tkinter.messagebox as messagebox
import random

class CampoMinado:
  """
  Uma classe que representa o jogo campo minado

  ...

  Attributes
  ----------
  mapa : Mapa object
    é o mapa do jogo 

  Methods
  -------
  iniciar()
    Pergunta o nível de dificuldade do jogo e monta o campo minado
  jogar()
    Pergunta as jogadas e revela ou marca os pontos de acordo com as entradas do jogador
  __deve_continuar()
    Verifica se todas as minas já foram marcadas
  __nova_jogada(valor_maximo)
  """

  def __init__(self) -> None:
    self.nivel = None
    self.mapa = None
    self.janela_inicio = None
    self.janela_mapa = None
    self.dicas_disponiveis = None
    self.__iniciar_janela_inicial__()

  def jogar(self) -> None:
    self.janela_inicio.janela.mainloop()

  @property
  def mapa(self) -> mapa.Mapa:
    return self._mapa
  
  @mapa.setter
  def mapa(self, mapa):
    self._mapa = mapa

  @property
  def nivel(self) -> int:
    return self._nivel

  @nivel.setter
  def nivel(self, nivel):
    self._nivel = nivel
    self.dicas_disponiveis = nivel - 1 if nivel and nivel > 1 else 0

  def __iniciar_janela_inicial__(self):
    self.janela_inicio = janelas.JanelaInicio()
    self.janela_inicio.botao_iniciar.bind(janelas.EVENTO_CLICK, self.__evento_iniciar__)

  def __iniciar_janela_mapa__(self):
    self.janela_mapa = janelas.JanelaJogo(self.nivel)
    self.mapa = mapa.Mapa(self.nivel, self.janela_mapa.frame_grid)
    self.janela_inicio.esconder()
    self.__setar_eventos_mapa__()

  def __setar_eventos_mapa__(self):
    for posicao_x in range(self.nivel):
      for posicao_y in range(self.nivel):
        ponto = self.mapa.pontos[posicao_x][posicao_y]
        ponto.frame.botao.bind("<Button-1>", lambda _evento, ponto=ponto: self.__evento_selecionar__(ponto))
    self.janela_mapa.botao_reiniciar.bind(janelas.EVENTO_CLICK, self.__evento_reiniciar__)
    self.janela_mapa.botao_recomecar.bind(janelas.EVENTO_CLICK, self.__evento_recomecar__)
    self.janela_mapa.botao_dica.bind(janelas.EVENTO_CLICK, self.__evento_dica__)

  def __evento_iniciar__(self, _evento):
    nivel =  self.janela_inicio.campo_nivel.get()
    if not nivel.isnumeric() or int(nivel) <= 0:
        messagebox.showerror(title="Erro!", message="O nível deve ser um número inteiro positivo!")
        return
    self.nivel = int(nivel)
    self.__iniciar_janela_mapa__()

  def __evento_selecionar__(self, ponto):
    try:
      ponto.abrir()
      if(self.__minas_descobertas__()):
        self.mapa.revelar()
        messagebox.showinfo(title="Ganhou!", message='Você ganhou, parabéns!')
    except ponto_mina.ExplosaoMina as error:
      self.mapa.revelar()
      messagebox.showerror(title="Erro!", message=error)
    except ValueError as error:
      messagebox.showwarning(title="Erro!", message=error)

  def __evento_reiniciar__(self, _evento):
    for posicao_x in range(self.nivel):
      for posicao_y in range(self.nivel):
        ponto = self.mapa.pontos[posicao_x][posicao_y]
        ponto.fechar()
        ponto.frame.botao.bind("<Button-1>", lambda _evento, ponto=ponto: self.__evento_selecionar__(ponto))

  def __evento_recomecar__(self, _evento):
    self.janela_inicio.mostrar()
    self.janela_mapa.esconder()

  def __evento_dica__(self, _evento):
    if(self.dicas_disponiveis > 0 and not self.__minas_descobertas__()):
      while(True):
        posicao_x = random.randint(0, self.nivel-1)
        posicao_y = random.randint(0, self.nivel-1)
        ponto = self.mapa.pontos[posicao_x][posicao_y]
        if not isinstance(ponto, ponto_mina.PontoMina) and not ponto.aberto(): 
          self.__evento_selecionar__(ponto)
          self.dicas_disponiveis-=1
          if(not self.__minas_descobertas__()):
            mensagem = f'Você ainda possui {self.dicas_disponiveis} dicas!'
            if(self.dicas_disponiveis == 1):
              mensagem = f'Você ainda possui 1 dica!'
            elif(self.dicas_disponiveis <= 0):
              mensagem = f'Não há mais dicas disponíveis!'
            messagebox.showwarning(title="Aviso!", message=mensagem)
          break
    else:
      messagebox.showwarning(title="Erro!", message='Não há mais dicas disponíveis!')

  def __minas_descobertas__(self) -> bool:
    """Verifica se todas as minas já foram marcadas

    Returns
    ----------
    bool
      retorna True se todas as minas foram marcadas
      retorna False se ainda há minas a serem marcadas
    """
    return self.mapa.qtd_minas_descobertas() == self.mapa.nivel

def jogar():
  """ Roda o jogo do campo minado, criando novas partida até que o jogador escolha sair"""
  campo_minado = CampoMinado()
  campo_minado.jogar()

jogar()
