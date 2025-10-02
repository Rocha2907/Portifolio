import tkinter as tk   
from tkinter import font
import winsound
import pygame
import requests
import os



tempo_estudo = 25*60
tempo_pausa_curta= 5*60
tempo_pausa_longa= 15*60
ciclos_pausa_longa = 4

ciclos_concluidos = 0

def iniciar_janela():
    global janela,label
    janela = tk.Tk()
    janela.title("Pomodoro")
    minha_fonte = ("Arial", 15, "bold")

    label = tk.Label(janela, text="Inicie o seu estudo!\n", font=minha_fonte)
    label.pack()

    botao = tk.Button(janela,text='Iniciar', command=lambda: iniciar_timer(tempo_estudo,'Hora de estudar'),font=("Arial", 10, "bold"))
    botao.pack()

    centralizar_janela(janela,300,100)
    janela.mainloop() 
    

def iniciar_timer(duracao,tipo):

    def timer(segundos):
        if segundos >= 0:
            atualizar_display(segundos, tipo)
            janela.after(1000,timer,segundos -1)
            
        else:
            proxima_sessao(tipo)

    timer(duracao)


def atualizar_display(tempo_restante,tipo):         
            minutos = tempo_restante // 60
            seg = tempo_restante % 60
            tempo_formatado = f'{minutos:02d}:{seg:02d}'
            label.config(text=f'{tipo}: {tempo_formatado}')

def proxima_sessao(tipo):
    global ciclos_concluidos
    if 'Hora de estudar' in tipo: 
        ciclos_concluidos += 1
        if ciclos_concluidos % ciclos_pausa_longa == 0:
            iniciar_timer(tempo_pausa_longa,"Pausa Longa" + "\nAproveite seu tempo")
            janela.attributes('-topmost', True)
            tocar_som_pausa_15_minitos()
        else:
            iniciar_timer(tempo_pausa_curta,"Pausa Curta" + "\nAproveite para respirar")
            janela.attributes('-topmost', True)
            tocar_bip()
            tocar_som_pausa_5_minitos()
    else:
        janela.lower()
        iniciar_timer(tempo_estudo,"Hora de estudar")
        tocar_som_estudar()

def tocar_bip():
    frequencia = 1000
    duracao = 500
    winsound.Beep(frequencia,duracao)

def tocar_som_estudar():

    # Caminho para salvar o arquivo na pasta "audio" dentro do diretório do script
    pasta_audio = os.path.join(os.getcwd(), "audio")
    if not os.path.exists(pasta_audio):
        os.makedirs(pasta_audio)

    arquivo_local = os.path.join(pasta_audio, "estudo.mp3")
    url = "https://drive.google.com/uc?export=download&id=1qA4dBruXlWETiCo5v8_5KqzsM5c6sXSo"

    # Baixar apenas se o arquivo não existir
    if not os.path.exists(arquivo_local):
        print("Baixando áudio do Google Drive...")
        r = requests.get(url)
        with open(arquivo_local, "wb") as f:
            f.write(r.content)
    else:
        print("Usando arquivo local...")

    # Inicializar mixer (apenas se não estiver inicializado)
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Carregar e tocar o áudio
    pygame.mixer.music.load(arquivo_local)
    pygame.mixer.music.play()

def tocar_som_pausa_5_minitos():
    
    # Caminho para salvar o arquivo na pasta "audio" dentro do diretório do script
    pasta_audio = os.path.join(os.getcwd(), "audio")
    if not os.path.exists(pasta_audio):
        os.makedirs(pasta_audio)

    arquivo_local = os.path.join(pasta_audio, "pausa5.mp3")
    url = "https://drive.google.com/uc?export=download&id=1FpHXSfW4ghCagRseKJdX-r4ofk4StMGh"

    # Baixar apenas se o arquivo não existir
    if not os.path.exists(arquivo_local):
        print("Baixando áudio do Google Drive...")
        r = requests.get(url)
        with open(arquivo_local, "wb") as f:
            f.write(r.content)
    else:
        print("Usando arquivo local...")

    # Inicializar mixer (apenas se não estiver inicializado)
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Carregar e tocar o áudio
    pygame.mixer.music.load(arquivo_local)
    pygame.mixer.music.play()

def tocar_som_pausa_15_minitos():

    # Caminho para salvar o arquivo na pasta "audio" dentro do diretório do script
    pasta_audio = os.path.join(os.getcwd(), "audio")
    if not os.path.exists(pasta_audio):
        os.makedirs(pasta_audio)

    arquivo_local = os.path.join(pasta_audio, "pausa15.mp3")
    url = "https://drive.google.com/uc?export=download&id=1xrVZCkPwhClKkNstoHu4FuW-VAuHaQG8"

    # Baixar apenas se o arquivo não existir
    if not os.path.exists(arquivo_local):
        print("Baixando áudio do Google Drive...")
        r = requests.get(url)
        with open(arquivo_local, "wb") as f:
            f.write(r.content)
    else:
        print("Usando arquivo local...")

    # Inicializar mixer (apenas se não estiver inicializado)
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Carregar e tocar o áudio
    pygame.mixer.music.load(arquivo_local)
    pygame.mixer.music.play()

def centralizar_janela(janela, largura=400, altura=300):
    # Tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcular posição x e y
    x = (largura_tela // 2) - (largura // 2) 
    y = (altura_tela // 2) - (altura // 2)
    # Configurar tamanho e posição
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


iniciar_janela()