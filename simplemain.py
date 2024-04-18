import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

def abrir_janela_escolher_pasta():
    janela2 = Tk()
    janela2.withdraw() # Esconde a janela principal

    pasta_escolhida = filedialog.askdirectory()
    print("Pasta escolhida:", pasta_escolhida)

def alterar_extensao(caminho_pasta):
    lista_arquivos = os.listdir(caminho_pasta)

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(('.png')):
            imagem = Image.open(os.path.join(caminho_pasta, arquivo))
            
            imagem_convertida = imagem.convert('RGB')
            
            if imagem.format.lower() != "jpg":
                novo_nome = os.path.splitext(arquivo)[0] + ".jpg"
                imagem_convertida.save(os.path.join(caminho_pasta, novo_nome))

def main():
    janela2 = Tk()
    janela2.withdraw() # Esconde a janela principal

    pasta_escolhida = filedialog.askdirectory()
    print("Pasta escolhida:", pasta_escolhida)
    alterar_extensao(pasta_escolhida)

    texto_final["text"] = "Código finalizado, pode fechar a janela! Obrigado por usar!"

janela = Tk() # Cria a janela e chama ela de "Janela"

janela.title("Escolha a sua pasta")

texto_explicacao = Label(janela, text="Clique no botão para ")
texto_explicacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Clique aqui para escolher a pasta", command=main)
botao.grid(column=0, row=1, padx=15, pady=5)

texto_final = Label(janela, text="")
texto_final.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop() # Mantém a janela aberta até o final do uso