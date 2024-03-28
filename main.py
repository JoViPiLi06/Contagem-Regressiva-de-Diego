import tkinter as tk
from tkinter import messagebox
import datetime
import webbrowser

# Lista de dias letivos
dias_letivos = {
    "Fevereiro": [6, 7, 8, 9, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29],
    "Março": [1, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 25, 26, 27],
    "Abril": [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30],
    "Maio": [2, 3, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 27, 28, 29],
    "Junho": [3, 4, 5, 6, 7, 8, 10, 11, 12, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28],
    "Julho": [1, 2, 3, 4, 5, 8, 9, 10, 11, 12],
    "Agosto": [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 26, 27, 28, 29, 30],
    "Setembro": [2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 30],
    "Outubro": [1, 2, 3, 4, 7, 8, 9, 10, 11, 21, 22, 23, 24, 25, 28, 29, 30, 31],
    "Novembro": [1, 4, 5, 6, 7, 8, 11, 12, 13, 14, 18, 19, 20, 21, 22, 25, 26, 27, 28, 29],
    "Dezembro": [2, 3, 4, 5, 6, 9, 10, 11]
}

# Função para calcular o dia do ano
def calcular_dia_ano(data):
    primeiro_dia_ano = datetime.datetime(data.year, 1, 1)
    return (data - primeiro_dia_ano).days + 1

# Função para calcular a data do último dia letivo
def calcular_ultimo_dia_letivo():
    hoje = datetime.datetime.now()
    dias_letivos_totais = sum(len(dias) for dias in dias_letivos.values())
    primeiro_dia_ano = hoje.replace(month=2, day=27)  # Primeiro dia letivo
    ultimo_dia_letivo = primeiro_dia_ano + datetime.timedelta(days=dias_letivos_totais - 1)
    return ultimo_dia_letivo

# Função para calcular o tempo restante até o final do ano letivo
def calcular_tempo_restante():
    hoje = datetime.datetime.now()
    ultimo_dia_letivo = calcular_ultimo_dia_letivo()
    tempo_restante = ultimo_dia_letivo - hoje
    return tempo_restante

# Verifica se é hora de tocar o vídeo
def verificar_video():
    agora = datetime.datetime.now()
    if agora.time() >= datetime.time(6, 45) and agora.time() <= datetime.time(6, 46):
        webbrowser.open("https://www.youtube.com/watch?v=WPzMxiGd0io")

# Exibe a contagem regressiva
def exibir_contagem_regressiva():
    tempo_restante = calcular_tempo_restante()
    dias_restantes = tempo_restante.days
    horas, segundos = divmod(tempo_restante.seconds, 3600)
    minutos, segundos = divmod(segundos, 60)
    messagebox.showinfo("Contagem regressiva",
                        f"Contagem regressiva para o fim de ano letivo de Diego interdimensional!\n\n"
                        f"Tempo restante até o fim do ano letivo:\n"
                        f"Dias: {dias_restantes}\n"
                        f"Horas: {horas}\n"
                        f"Minutos: {minutos}\n"
                        f"Segundos: {segundos}")

# Função para atualizar a contagem regressiva
def atualizar_contagem():
    verificar_video()
    exibir_contagem_regressiva()

# Interface Gráfica
root = tk.Tk()
root.title("Contagem Regressiva")
root.configure(background='white')  # Define o fundo da janela como branco

# Adicione estas linhas para definir a janela para a orientação horizontal
largura = 600
altura = 400
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = largura_tela // 2 - largura // 2
posicao_y = altura_tela // 2 - altura // 2
root.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

# Label para o título
titulo = tk.Label(root, text="Contagem regressiva para o fim de ano letivo de Diego interdimensional!", bg='white', fg='black')
titulo.pack(pady=10)

# Botão para exibir a contagem regressiva
btn_contagem = tk.Button(root, text="Exibir Contagem Regressiva", command=exibir_contagem_regressiva, bg='blue', fg='white')
btn_contagem.pack(pady=10)

# Botão para atualizar a contagem regressiva
btn_atualizar = tk.Button(root, text="Atualizar Contagem Regressiva", command=atualizar_contagem, bg='green', fg='white')
btn_atualizar.pack(pady=10)

root.mainloop()