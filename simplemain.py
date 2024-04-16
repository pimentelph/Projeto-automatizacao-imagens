import os
import tkinter as tk
from tkinter import simpledialog
from PIL import Image

def pegar_caminho_pasta():
    terminar = bool


def alterar_extensao(caminho_pasta):
    lista_arquivos = os.listdir(caminho_pasta)

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(('.png')):
            imagem = Image.open(os.path.join(caminho_pasta, arquivo))
            
            imagem_convertida = imagem.convert('RGB')
            
            if imagem.format.lower() != "jpg":
                novo_nome = os.path.splitext(arquivo)[0] + ".jpg"
                imagem_convertida.save(os.path.join(caminho_pasta, novo_nome))


caminho_pasta = input("Coloque aqui o caminho da pasta que será usada(Se estiver com "" tire elas): ")
alterar_extensao(caminho_pasta)


if __name__ == '__main__':
    py = 1