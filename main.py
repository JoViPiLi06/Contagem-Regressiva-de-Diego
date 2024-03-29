import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from datetime import datetime, timedelta, time
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
    primeiro_dia_ano = datetime(data.year, 1, 1)
    return (data - primeiro_dia_ano).days + 1

# Função para calcular a data do último dia letivo
def calcular_ultimo_dia_letivo():
    hoje = datetime.now()
    dias_letivos_totais = sum(len(dias) for dias in dias_letivos.values())
    primeiro_dia_ano = hoje.replace(month=2, day=27)  # Primeiro dia letivo
    ultimo_dia_letivo = primeiro_dia_ano + timedelta(days=dias_letivos_totais - 1)
    return ultimo_dia_letivo

# Função para calcular o tempo restante até o final do ano letivo
def calcular_tempo_restante():
    hoje = datetime.now()
    ultimo_dia_letivo = calcular_ultimo_dia_letivo()
    tempo_restante = ultimo_dia_letivo - hoje
    return tempo_restante

# Verifica se é hora de tocar o vídeo
def verificar_video():
    agora = datetime.now()
    if agora.time() >= time(6, 45) and agora.time() <= time(6, 46):
        webbrowser.open("https://www.youtube.com/watch?v=WPzMxiGd0io")

# Exibe a contagem regressiva
def exibir_contagem_regressiva(*args):
    tempo_restante = calcular_tempo_restante()
    dias_restantes = tempo_restante.days
    horas, segundos = divmod(tempo_restante.seconds, 3600)
    minutos, segundos = divmod(segundos, 60)
    popup = Popup(title='Contagem regressiva',
                  content=Label(text=f"Contagem regressiva para o fim de ano letivo de Diego interdimensional!\n\n"
                                     f"Tempo restante até o fim do ano letivo:\n"
                                     f"Dias: {dias_restantes}\n"
                                     f"Horas: {horas}\n"
                                     f"Minutos: {minutos}\n"
                                     f"Segundos: {segundos}"),
                  size_hint=(None, None), size=(500, 500))
    popup.open()

# Função para atualizar a contagem regressiva
def atualizar_contagem():
    verificar_video()
    exibir_contagem_regressiva()

class ContagemRegressivaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Contagem regressiva para o fim de ano"))
        btn_contagem = Button(text="Exibir Contagem Regressiva", on_press=exibir_contagem_regressiva)
        btn_atualizar = Button(text="Atualizar Contagem Regressiva", on_press=atualizar_contagem)
        layout.add_widget(btn_contagem)
        layout.add_widget(btn_atualizar)
        return layout

if __name__ == "__main__":
    ContagemRegressivaApp().run()