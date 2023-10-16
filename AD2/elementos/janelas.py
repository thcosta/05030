import tkinter as tk
import tkinter.messagebox as messagebox

__all__ = ['JanelaInicio', 'JanelaJogo']

EVENTO_CLICK = "<Button-1>"

FONTE_PADRAO = ("Helvetica", 16, "bold")

LABEL_PADRAO = {
  "font": FONTE_PADRAO, 
  "anchor": "center",
  "bg": "#c5cbe3"
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
    self.janela.configure(bg = "#c5cbe3")
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
    frame = tk.Frame(master=self.janela, bg="#c5cbe3")
    self.janela.configure(bg = "#c5cbe3")
    self.criarCampoNivel(frame)
    self.criarBotaoIniciar(frame)
    frame.pack()

  def criarCampoNivel(self, frame):
    self.label({ "text": "Qual o nível de dificuldade desejado?", "master": frame }).grid(row=1,column=1, pady=15)
    self.campo_nivel = self.campo({ "width": 8, "master": frame })
    self.campo_nivel.grid(row=2,column=1)
  
  def criarBotaoIniciar(self, frame):
    icone = tk.PhotoImage(file=r'imagens/iniciar.png')
    frame.icone = icone
    self.botao_iniciar = self.botao({ "text": "Começar", 
                        "image": icone, 
                        "master": frame })
    self.botao_iniciar.grid(row=3,column=1,pady=20)

class JanelaJogo(Janela):
  def __init__(self, nivel) -> None:
    self.janela = tk.Toplevel()
    self.janela.title('Campo Minado')
    self.janela.configure(bg = "#c5cbe3")
    self.tamanho_grid = 65*nivel
    self.criarGridMapa(nivel)
    self.criarBotoes()

  def criarGridMapa(self, nivel):
    frame_principal = tk.Frame(master=self.janela, width= self.tamanho_grid + 100, height=self.tamanho_grid + 20, bg="#c5cbe3")
    frame_principal.pack()
    self.frame_grid = tk.Frame(master=frame_principal, width= self.tamanho_grid, height=self.tamanho_grid, bg="#c5cbe3")
    self.frame_grid.pack(side=tk.LEFT)
    frame_contador = tk.Frame(master=frame_principal, width= 100, height=self.tamanho_grid, background="red", padx=20, bg="#c5cbe3")
    frame_contador.pack(side=tk.RIGHT)
    self.criarCampoContador(frame_contador, nivel)

  def criarCampoContador(self, frame, nivel):
    self.label({ "text": "Quantidade de Bombas", "master": frame }).grid(row=1,column=1, pady=15, padx=10)
    self.campo_contador = self.campo({ "width": 8, "master": frame, "state": tk.DISABLED })
    self.campo_contador.grid(row=2, column=1, padx=10)
    self.campo_contador.insert(0, nivel)
  
  def criarBotoes(self):
    frame_secundario = tk.Frame(master=self.janela, width= self.tamanho_grid + 100, height=50, bg="#c5cbe3")
    frame_secundario.pack()
    frame_botoes = tk.Frame(master=frame_secundario, width= self.tamanho_grid + 100, height=50, bg="#c5cbe3")
    frame_botoes.pack(side=tk.BOTTOM)
    self.criarBotaoReiniciar(frame_botoes)
    self.criarBotaoRecomecar(frame_botoes)
    self.criarBotaoDica(frame_botoes)
    self.criarBotaoSair(frame_botoes)

  def criarBotaoReiniciar(self, frame):
    icone = tk.PhotoImage(file=r'imagens/reiniciar.png')
    frame.icone_reiniciar = icone
    self.botao_reiniciar = self.botao({ "text": "Reiniciar", 
                        "image": icone, 
                        "master": frame})
    self.botao_reiniciar.grid(row=1,column=1,pady=20, padx=5)
    # botao_iniciar.bind(EVENTO_CLICK, self.eventoIniciar)

  def criarBotaoRecomecar(self, frame):
    icone = tk.PhotoImage(file=r'imagens/recomecar.png')
    frame.icone_recomecar = icone
    self.botao_recomecar = self.botao({ "text": "Novo Jogo", 
                        "image": icone, 
                        "master": frame})
    self.botao_recomecar.grid(row=1,column=2,pady=20, padx=5)

  def criarBotaoDica(self, frame):
    icone = tk.PhotoImage(file=r'imagens/dica.png')
    frame.icone_dica = icone
    self.botao_dica = self.botao({ "text": "Dica", 
                        "image": icone, 
                        "master": frame})
    self.botao_dica.grid(row=1,column=3,pady=20, padx=5)
    # botao_iniciar.bind(EVENTO_CLICK, self.eventoIniciar)

  def criarBotaoSair(self, frame):
    icone = tk.PhotoImage(file=r'imagens/sair.png')
    frame.icone_sair = icone
    self.botao_sair = self.botao({ "text": "Sair", 
                        "image": icone, 
                        "master": frame })
    self.botao_sair.grid(row=1,column=4,pady=20, padx=5)
    self.botao_sair.bind(EVENTO_CLICK, lambda _evento: self.janela.quit())
