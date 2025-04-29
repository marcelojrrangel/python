# -*- coding: utf-8 -*-

import pyautogui
import os
import shutil
import fnmatch
import chardet
import pyperclip
import re

import win32con
import win32gui
import keyboard


class LibClass:

    def __init__(self, p_titulo_janela):
        self.retry = 10
        self.titulo_janela = p_titulo_janela

    def enum_window_callback(self, hwnd, results):
        results.append((hwnd, win32gui.GetWindowText(hwnd)))
    def obter_janela(self, sub_string):
        results = []
        win32gui.EnumWindows(self.enum_window_callback, results)
        for hwnd, title in results:
            if sub_string.lower() in title.lower():
                return hwnd
        return None


    def focus_window(self, hwnd):
        try:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Para restaurar a janela se estiver minimizada
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f"Erro ao tentar focar a janela: {e}")

    def envia_comando(self, comando=None, texto=None, press=None, hotkey=None):
        window = None
        sair = False

        while window is None or sair:
            window = self.obter_janela(self.titulo_janela)

        if window is not None:
            # Garantir que a janela está focada
            self.focus_window(window)
            if comando is not None:
                pyautogui.hotkey(comando)
            elif texto is not None:
                # if self.contem_caracteres_acentuados(texto):
                #     #self.type_with_accented_characters(texto)
                #     keyboard.write(text=texto,delay=0.2)
                # else:
                #     pyautogui.typewrite(message=texto,interval=0.2)
                keyboard.write(text=texto, delay=0.1)
            elif press is not None:
                pyautogui.press(press)
            elif hotkey is not None:
                pyautogui.hotkey(hotkey)
            else:
                print("Nenhum parâmetro passado!")
                raise print('Nenhum parâmetro passado!')
        else:
            print("Janela não encontrada!!")

    def type_with_accented_characters(self, text):
        # Copia o texto para a área de transferência
        pyperclip.copy(text)
        # Cola o texto no local desejado
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('')
    def contem_caracteres_acentuados(self, texto):
        # Expressão regular para caracteres acentuados
        padrao = r'[áéíóúàèìòùâêîôûãõçÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ]'

        # Verifica se a string contém algum desses caracteres
        return re.search(padrao, texto) is not None

    def save_as(self, p_titulo_janela=None, texto=None, press=None):
        window = self.obter_janela(p_titulo_janela)
        if window is not None:
            # Garantir que a janela está focada
            self.focus_window(window)
            if texto is not None:
                pyautogui.typewrite(texto)
            elif press is not None:
                pyautogui.press(press)
            else:
                raise print('Nunum parâmetro passado!')

    def clear_folder(self, folder_path):
        # Verifica se o caminho da pasta existe
        if not os.path.exists(folder_path):
            print(f"A pasta {folder_path} não existe.")
            return
        # Itera sobre todos os arquivos e subpastas na pasta especificada
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                # Se for um arquivo, remove
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print(f"Arquivo {file_path} removido.")
                # Se for uma pasta, remove recursivamente
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Pasta {file_path} removida.")
            except Exception as e:
                print(f"Falha ao apagar {file_path}. Motivo: {e}")

    def obter_leitura_arquivo(self,  file_path):
        try:
            encode = self.obter_encode_arquivo(file_path)
            return open(file_path, 'r', encoding=encode)
        except FileNotFoundError:
            print(f"O arquivo {file_path} não foi encontrado.")
            return None

    def obter_encode_arquivo(self, file_path):
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            return result['encoding']

    def encontar_arquivos(self, pasta_inicial, padrao):
        # Garantir que a pasta de destino exista
        #os.makedirs(pasta_destino, exist_ok=True)

        arquivos_encontrados = []

        for raiz, diretorios, arquivos in os.walk(pasta_inicial):
            for nome in arquivos:
                if fnmatch.fnmatch(nome, padrao):
                    caminho_completo_arquivo = os.path.join(raiz, nome)
                    arquivos_encontrados.append(caminho_completo_arquivo)

                    # Copiar arquivo para a pasta de destino
                    #shutil.copy(caminho_completo_arquivo, pasta_destino)

        return arquivos_encontrados

    def verificar_string_no_arquivo(self, caminho_do_arquivo, string_a_procurar):
        try:
            encode = self.obter_encode_arquivo(caminho_do_arquivo)
            with open(caminho_do_arquivo, 'r', encoding=encode) as arquivo:
                #string_a_procurar = string_a_procurar.lower()
                for linha in arquivo:
                    for procura in string_a_procurar:
                        if procura.lower() in linha.lower():
                            arquivo.close()
                            return True
            return False
        except FileNotFoundError:
            print(f"O arquivo {caminho_do_arquivo} não foi encontrado.")
            return False
