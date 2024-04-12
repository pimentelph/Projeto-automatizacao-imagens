import os
import re # Expressões regulares
from PIL import Image

def verificar_extensao(extensao):
    extensao_lower = extensao.lower() # Faz com que a extensão dos arquivos fiquem em letras minúsculas, usando a função lower().
    return bool(re.search(r'^\.(jpg)$', extensao_lower)) # Uso expressão regular para achar a ocorrência de .jpg(talvez possa fazer isso de outra forma mais fácil)


def checagem_de_arquivos(raiz, arquivo):
    nome_arquivo, extensao = os.path.splitext(arquivo)  # O 'os.path' é um módulo na biblioteca 'os' que fornece funções para manipulações de caminhos de arquivos e diretórios.
                                                        # E o 'os.path.splittext' divide um caminho em duas partes (nome do arquivo e extensão) e retorna uma tupla.
    caminho_completo = os.path.join(raiz, arquivo)  # Construindo o caminho completo para a imagem, assim me permitindo usar algumas funções do Image

    if verificar_extensao(extensao):
        return
    else:
        imagem = Image.open(caminho_completo).convert("RGB") # Abre a imagem e converte a imagem do formato RGBA(Formato padrão do PNG, onde o 'A' [Canal Alfa] define a transparência da imagem) para o RGB.
        novo_caminho = os.path.join(raiz, nome_arquivo + '.jpg')
        imagem.save(novo_caminho)
        
def loop_de_arquivos(raiz, arquivos):
    for arquivo in arquivos:
        checagem_de_arquivos(raiz, arquivo)

def main(diretorio_raiz):
    for raiz,  diretorios, arquivos in os.walk(diretorio_raiz): # O os.walk é uma função em Python que permite percorrer recursivamente uma árvore de diretórios.
        loop_de_arquivos(raiz, arquivos)


if __name__ == '__main__':
    diretorio_raiz =  r'C:\Users\ph024\Desktop\_fotos_projeto'  # Precisa colocar o 'r' para indicar que é uma string "crua"(raw) e não ler os caracteres de 'escape'.
                                                                # Ou colocar \\ no caminho ao invés de somente uma \ (Aparentemente isso é somente no Windowns).
    main(diretorio_raiz)