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
  nivel : int
    é o nível de dificuldade do jogo
  janela_inicio : JanelaInicio object
    é a primeira janela do jogo
  janela_mapa : JanelaJogo object
    é a segunda janela do jogo
  dicas_disponiveis: int
    é o número de dicas disponiveis

  Methods
  -------
  jogar()
    Roda o jogo 
  __iniciar_janela_inicial__()
    Abre a primeira janela do jogo e seta o evento do botão Iniciar
  __iniciar_janela_mapa__()
    Abre a segunda janela do jogo, esconde a primeira janela e seta os eventos da segunda janela
  __setar_eventos_mapa__()
    Seta os eventos dos mapa e dos botões da segunda janela
  __evento_iniciar__()
    Define o evento do botão Iniciar
  __evento_selecionar__()
    Define o evento de seleção de um ponto do mapa
  __evento_reiniciar__()
    Define o evento do botão Reiniciar
  __evento_recomecar__()
    Define o evento do botão Novo Jogo
  __evento_dica__()
    Define o evento do botão Dica
  __minas_descobertas__()
    Verifica se todas as minas foram descobertas
  """

  def __init__(self) -> None:
    self.nivel = None
    self.mapa = None
    self.janela_inicio = None
    self.janela_mapa = None
    self.dicas_disponiveis = None
    self.__iniciar_janela_inicial__()

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

  def jogar(self):
    """Roda o jogo"""
    self.janela_inicio.janela.mainloop()

  def __iniciar_janela_inicial__(self):
    """Abre a primeira janela do jogo e seta o evento do botão Iniciar"""
    self.janela_inicio = janelas.JanelaInicio()
    self.janela_inicio.botao_iniciar.bind(janelas.EVENTO_CLICK, self.__evento_iniciar__)

  def __iniciar_janela_mapa__(self):
    """Abre a segunda janela do jogo, esconde a primeira janela e seta os eventos da segunda janela"""
    self.janela_mapa = janelas.JanelaJogo(self.nivel)
    self.mapa = mapa.Mapa(self.nivel, self.janela_mapa.frame_grid)
    self.janela_inicio.esconder()
    self.__setar_eventos_mapa__()

  def __setar_eventos_mapa__(self):
    """Seta os eventos dos mapa e dos botões da segunda janela"""
    for posicao_x in range(self.nivel):
      for posicao_y in range(self.nivel):
        ponto = self.mapa.pontos[posicao_x][posicao_y]
        ponto.frame.botao.bind("<Button-1>", lambda _evento, ponto=ponto: self.__evento_selecionar__(ponto))
    self.janela_mapa.botao_reiniciar.bind(janelas.EVENTO_CLICK, self.__evento_reiniciar__)
    self.janela_mapa.botao_recomecar.bind(janelas.EVENTO_CLICK, self.__evento_recomecar__)
    self.janela_mapa.botao_dica.bind(janelas.EVENTO_CLICK, self.__evento_dica__)

  def __evento_iniciar__(self, _evento):
    """Verifica se o nivel é válido
        Se for, abre a segunda janela do jogo
        Se não for, mostra mensagem de nível inválido
    """
    nivel =  self.janela_inicio.campo_nivel.get()
    if not nivel.isnumeric() or int(nivel) <= 0:
        messagebox.showerror(title="Erro!", message="O nível deve ser um número inteiro positivo!")
        return
    self.nivel = int(nivel)
    self.__iniciar_janela_mapa__()

  def __evento_selecionar__(self, ponto):
    """Abre o ponto selecionado
        Se for mina, mostra mensagem de fim de jogo com partida perdida e exibe todo o mapa
        Se não for e não houver mais pontos fechados sem mina, mostra mensagem de fim de jogo com partida ganha e exibe todo o mapa
    """
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
    """Fecha todos os ponto abertos e reinicia as dicas"""
    for posicao_x in range(self.nivel):
      for posicao_y in range(self.nivel):
        ponto = self.mapa.pontos[posicao_x][posicao_y]
        ponto.fechar()
        self.dicas_disponiveis = self.nivel - 1
        ponto.frame.botao.bind("<Button-1>", lambda _evento, ponto=ponto: self.__evento_selecionar__(ponto))

  def __evento_recomecar__(self, _evento):
    """Fecha a segunda janela e mostra a primeira janela novamente"""
    self.janela_inicio.mostrar()
    self.janela_mapa.esconder()

  def __evento_dica__(self, _evento):
    """Se houver dica disponível
        Escolhe um ponto aletório que não é mina e abre o ponto
        Mostra a quantidade disponível de dicas após a jogada
    """
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
    """Verifica se todas as minas já foram encontradas

    Returns
    ----------
    bool
      retorna True se todas as minas foram encontradas
      retorna False se ainda há minas a serem encontradas
    """
    return self.mapa.qtd_minas_descobertas() == self.mapa.nivel

def jogar():
  """ Roda o jogo do campo minado até que o jogador escolha sair"""
  campo_minado = CampoMinado()
  campo_minado.jogar()

jogar()
