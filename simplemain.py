import os
from tkinter import *
from tkinter import filedialog
from PIL import Image


def criar_pasta():
    diretorio_area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')

    nova_pasta = os.path.join(diretorio_area_de_trabalho, "Imagens Redimensionadas")

    if not os.path.exists(nova_pasta):
        os.mkdir(nova_pasta)
        texto_aviso['text'] = "Pasta criada!"
    else:
        texto_aviso['text'] = "A pasta já existe na sua área de trabalho e está tudo lá!"
    
    return nova_pasta

def alterar_extensao(caminho_pasta, nova_pasta):
    lista_arquivos = os.listdir(caminho_pasta)

    for arquivo in lista_arquivos:
        imagem = Image.open(os.path.join(caminho_pasta, arquivo))

        if arquivo.lower().endswith(('.png')):
            imagem_convertida = imagem.convert('RGB')
            novo_nome = os.path.splitext(arquivo)[0] + ".jpg"
            imagem_convertida.save(os.path.join(nova_pasta, novo_nome))

        else:
            novo_nome = os.path.splitext(arquivo)[0] + ".jpg"
            imagem.save(os.path.join(nova_pasta, novo_nome))


def redimensionar_imagem(caminho_pasta, nova_pasta):
    lista_arquivos = os.listdir(nova_pasta)
    for arquivo in lista_arquivos:
        imagem = Image.open(os.path.join(nova_pasta, arquivo))
        largura, altura = imagem.size

        if (largura, altura) != (356, 475):
            new_largura = 356 #|(largura / altura) * 356|
            new_altura = 475 #|(altura / largura) * 475| Com esses valores estava aumentando em PROPORÇÃO, por isso ficavam fora do padrão

            imagem_redimensionada = imagem.resize((round(new_largura), round(new_altura)), Image.LANCZOS)
            imagem_redimensionada.save(os.path.join(nova_pasta, arquivo), dpi = (72,72))



def main():
    janela2 = Tk()
    janela2.withdraw() # Esconde a janela principal

    pasta_escolhida = filedialog.askdirectory()
    nova_pasta = criar_pasta()
    alterar_extensao(pasta_escolhida, nova_pasta)
    redimensionar_imagem(pasta_escolhida, nova_pasta)

    texto_final["text"] = "Código finalizado, pode fechar a janela! Obrigado por usar!"

janela = Tk() # Cria a janela e chama ela de "Janela"
janela.title("Escolha a sua pasta")
janela.resizable(width = True, height = False)

texto_explicacao = Label(janela, text="Clique no botão para ")
texto_explicacao.grid(column = 0, row = 0, padx = 0, pady = 10)

botao = Button(janela, text="Clique aqui para escolher a pasta", command=main)
botao.grid(column = 0, row = 1, padx = 10, pady = 15)

texto_aviso = Label(janela, text='')
texto_aviso.grid(column = 0, row = 2, padx = 15, pady = 5)

texto_final = Label(janela, text="")
texto_final.grid(column = 0, row = 3, padx = 10, pady = 10)

janela.mainloop() # Mantém a janela aberta até o final do uso