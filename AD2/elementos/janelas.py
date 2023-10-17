import tkinter as tk

__all__ = ['JanelaInicio', 'JanelaJogo']

EVENTO_CLICK = "<Button-1>"

BACKGROUND_PADRAO = "#c5cbe3"

FONTE_PADRAO = ("Helvetica", 16, "bold")

LABEL_PADRAO = {
  "font": FONTE_PADRAO, 
  "anchor": "center",
  "bg": BACKGROUND_PADRAO
}

CAMPO_PADRAO = {
  "bg": "#EDEDED", 
  "font": ("Helvetica", 18, "normal"), 
  "justify": "center"
}

BOTAO_PADRAO = {
  "font": FONTE_PADRAO,
  "width": 200,
  "height": 70,
  "fg": "white",
  "compound": "right",
  "activeforeground": "white",
  "activebackground": "#262d4a",
  "background": "#445496",
  "relief": tk.RIDGE,
}

class Janela:
  def __init__(self, size) -> None:
    self.janela = tk.Tk()
    self.janela.geometry(size)
    self.janela.configure(bg = BACKGROUND_PADRAO)
    self.janela.title('Campo Minado')

  @staticmethod
  def label(opcoes):
    opcoes = { **LABEL_PADRAO, **opcoes}
    return tk.Label(**opcoes)

  @staticmethod
  def campo(opcoes):
    opcoes = { **CAMPO_PADRAO, **opcoes}
    return tk.Entry(**opcoes)

  @staticmethod
  def botao(opcoes) -> tk.Button:
    opcoes = { **BOTAO_PADRAO, **opcoes}
    return tk.Button(**opcoes)

  def esconder(self):
    self.janela.withdraw()

  def mostrar(self):
    self.janela.deiconify()

  def fechar(self):
    self.janela.quit()


class JanelaInicio(Janela):
  def __init__(self) -> None:
    super().__init__("600x200")
    frame = tk.Frame(master=self.janela, 
                    bg=BACKGROUND_PADRAO)
    self.janela.configure(bg = BACKGROUND_PADRAO)
    self.__criar_campo_nivel__(frame)
    self.__criar_botao_iniciar__(frame)
    frame.pack()

  def __criar_campo_nivel__(self, frame):
    self.label({ 
      "text": "Qual o nível de dificuldade desejado?", 
      "master": frame 
    }).grid(row=1,column=1, pady=15)
    self.campo_nivel = self.campo({ 
      "width": 8, 
      "master": frame 
    })
    self.campo_nivel.grid(row=2,column=1)
  
  def __criar_botao_iniciar__(self, frame):
    icone = tk.PhotoImage(file=r'imagens/iniciar.png')
    frame.icone = icone
    self.botao_iniciar = self.botao({ 
      "text": "Começar", 
      "image": icone, 
      "master": frame 
    })
    self.botao_iniciar.grid(row=3,column=1,pady=20)

class JanelaJogo(Janela):
  def __init__(self, nivel) -> None:
    self.janela = tk.Toplevel()
    self.janela.title('Campo Minado')
    self.janela.configure(bg = BACKGROUND_PADRAO)
    self.tamanho_grid = 65*nivel
    self.__criar_grid_mapa__(nivel)
    self.__criar_botoes__()
    self.janela.protocol("WM_DELETE_WINDOW", self.fechar)

  def __criar_grid_mapa__(self, nivel):
    frame_principal = tk.Frame(master=self.janela, 
                              width= self.tamanho_grid + 50, 
                              height=self.tamanho_grid + 40, 
                              bg=BACKGROUND_PADRAO)
    frame_principal.pack()

    frame_esquerdo = tk.Frame(master=frame_principal, 
                              height=self.tamanho_grid, 
                              bg=BACKGROUND_PADRAO)
    frame_esquerdo.pack(side=tk.LEFT, fill=tk.Y)
    self.__criar_campo_contador__(frame_esquerdo, nivel)

    frame_direito = tk.Frame(master=frame_principal, 
                            width= self.tamanho_grid, 
                            height=self.tamanho_grid + 2, 
                            # padx=20, 
                            bg=BACKGROUND_PADRAO)
    frame_direito.pack(side=tk.RIGHT)
    
    self.label({ 
      "text": "Selecione uma coordenada", 
      "master": frame_direito, 
      "height": 2 
      }).pack(fill=tk.X)
    self.frame_grid = tk.Frame(master=frame_direito, 
                              width= self.tamanho_grid, 
                              height=self.tamanho_grid, 
                              bg=BACKGROUND_PADRAO)
    self.frame_grid.pack(side=tk.BOTTOM)


  def __criar_campo_contador__(self, frame, nivel):
    self.label({ 
      "text": "Quantidade de Bombas:", 
      "master": frame, 
      "height": 2 
    }).pack(side=tk.TOP)
    self.campo_contador = self.campo({ 
      "width": 8, 
      "master": frame
    })
    self.campo_contador.pack(side=tk.TOP)
    self.campo_contador.insert(0, nivel)
    self.campo_contador.configure(state=tk.DISABLED)
  
  def __criar_botoes__(self):
    frame_secundario = tk.Frame(master=self.janela, 
                                width= self.tamanho_grid + 100, 
                                height=50, 
                                bg=BACKGROUND_PADRAO)
    frame_secundario.pack()
    frame_botoes = tk.Frame(master=frame_secundario, 
                            width= self.tamanho_grid + 100, 
                            height=50, 
                            bg=BACKGROUND_PADRAO)
    frame_botoes.pack(side=tk.BOTTOM)
    self.__criar_botao_reiniciar__(frame_botoes)
    self.__criar_botao_recomecar__(frame_botoes)
    self.__criar_botao_dica__(frame_botoes)
    self.__criar_botao_sair__(frame_botoes)

  def __criar_botao_reiniciar__(self, frame):
    icone = tk.PhotoImage(file=r'imagens/reiniciar.png')
    frame.icone_reiniciar = icone
    self.botao_reiniciar = self.botao({ 
      "text": "Reiniciar", 
      "image": icone, 
      "master": frame
    })
    self.botao_reiniciar.grid(row=1,column=1,pady=20, padx=5)

  def __criar_botao_recomecar__(self, frame):
    icone = tk.PhotoImage(file=r'imagens/recomecar.png')
    frame.icone_recomecar = icone
    self.botao_recomecar = self.botao({ 
      "text": "Novo Jogo", 
      "image": icone, 
      "master": frame
    })
    self.botao_recomecar.grid(row=1,column=2,pady=20, padx=5)

  def __criar_botao_dica__(self, frame):
    icone = tk.PhotoImage(file=r'imagens/dica.png')
    frame.icone_dica = icone
    self.botao_dica = self.botao({ 
      "text": "Dica", 
      "image": icone, 
      "master": frame
    })
    self.botao_dica.grid(row=1,column=3,pady=20, padx=5)

  def __criar_botao_sair__(self, frame):
    icone = tk.PhotoImage(file=r'imagens/sair.png')
    frame.icone_sair = icone
    self.botao_sair = self.botao({ 
      "text": "Sair", 
      "image": icone, 
      "master": frame 
    })
    self.botao_sair.grid(row=1,column=4,pady=20, padx=5)
    self.botao_sair.bind(EVENTO_CLICK, lambda _evento: self.janela.quit())
