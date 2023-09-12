from elementos import *

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
  revelar()
    Mostra o mapa do campo minado mostrando todos os pontos
  __deve_continuar()
    Verifica se todas as minas já foram marcadas
  __nova_jogada(valor_maximo)
    Roda a nova jogada
  __ler_coordenadas(posicao_x, posicao_y)
    Solicita as coordenadas da nova jogada    
  __escolher_jogada()
    Escolhe o tipo de jogada, revelar - R ou marcar - M
  """
  def __init__(self) -> None:
    self.mapa = None

  @property
  def mapa(self) -> int:
    return self._mapa
  
  @mapa.setter
  def mapa(self, mapa):
    self._mapa = mapa
  
  def iniciar(self):
    """Pergunta o nível de dificuldade do jogo e monta o campo minado"""
    while(True):
      try:
        nivel = input('Qual o nível de dificuldade desejado? ')
        self.mapa = mapa.Mapa(int(nivel))
        break
      except ValueError:
        print('Nível inválido! Tente novamente...')

  def jogar(self):
    """Pergunta as jogadas e revela ou marca os pontos de acordo com as entradas do jogador.
    Quando uma mina é revelada o método termina com o jogo como perdido.
    Quando todas as minas são marcadas o jogo termina como ganho.
    """
    index = 1
    ganhou = True
    while(self.__deve_continuar()):
      print('\nMapa Atual:')
      self.mapa.imprimir()
      print(f'\n# {index} Próxima jogada...')
      if(not self.__nova_jogada(self.mapa.nivel)): 
        ganhou = False
        break
      index+=1
    if(ganhou):
      print('\nVocê ganhou, parabéns!\n')
    self.revelar()

  def revelar(self):
    """Mostra o mapa do campo minado mostrando todos os pontos"""
    self.mapa.revelar()

  def __deve_continuar(self) -> bool:
    """Verifica se todas as minas já foram marcadas

    Returns
    ----------
    bool
      retorna True se todas as minas foram marcadas
      retorna False se ainda há minas a serem marcadas
    """
    return self.mapa.qtd_minas_descobertas() != self.mapa.nivel
  
  def __nova_jogada(self, valor_maximo) -> bool:
    """Roda a nova jogada. 
    Lê as coordenadas e o tipo e executa a rodada.

    Returns
    ----------
    bool
      retorna True se a jogada foi executada com sucesso ou se não foi possível entender a jogada
      retorna False se a jogada foi executada mas uma mina foi selecionada
    """
    try:
      posicao_x, posicao_y = self.__ler_coordenadas(valor_maximo)
      self.__escolher_jogada(posicao_x, posicao_y)
      return True
    except ValueError as erro:
      print(erro, 'Tente novamente...')
      return True
    except ponto_mina.ExplosaoMina as erro:
      print(f'\n{erro}', 'Você perdeu!\n')
      return False
    
  def __ler_coordenadas(self, valor_maximo) -> (int,int):
    """Solicita as coordenadas da nova jogada

    Raises
    ------
    ValueError
      Se a coordenada for inválida, retorna erro 'Coordenada inválida!'

    Returns
    ----------
    int,int
      retorna as coordenadas x,y setadas pelo jogador
    """
    coordenadas = input('Qual coordenada - no formato: x,y - do próximo ponto selecionado? ')
    x,y = map(lambda value: int(value), coordenadas.split(',')) 
    if(x < 1 or x > valor_maximo or y < 1 or y > valor_maximo):
      raise ValueError('Coordenada inválida!')
    return x,y
    
  def __escolher_jogada(self, posicao_x, posicao_y):
    """Solicita o tipo de jogada revelar - R ou marcar - M.
    Executa o tipo de jogada solicitado.

    Raises
    ------
    ValueError
      Se a opção for inválida, retorna erro 'Opção inválida!'
    """
    print('Qual sua próxima jogada?')
    opcao = input('Se quiser marcar digite M ou se quiser revelar digite R: ').upper()
    if (opcao !=  'M'and opcao != 'R'):
      raise ValueError('Opção inválida!')
    elif(opcao == 'M'):
      self.mapa.marcar_ponto(posicao_x-1,posicao_y-1)
    else:
      self.mapa.revelar_ponto(posicao_x-1,posicao_y-1)


def jogar():
  """ Roda o jogo do campo minado, criando novas partida até que o jogador escolha sair"""
  while True:
    campo_minado = CampoMinado()
    campo_minado.iniciar()
    campo_minado.jogar()
    opcao = input('\nDeseja jogar novamente? S/N ').upper()
    if(opcao != 'S'):
      print('Até a próxima!')
      break

jogar()
