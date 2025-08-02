#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Hello Word Multi Linguas

Dependendo da linguagem configurada no ambiente o 
programa exibe a mensagem
correspondente.

Como usar:
Tenha a variavel LANG devidamente configurada ex

                export LANG=pt_BR
Execução:
                python3 hello.py
                ou
                ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Rafael Pereira"
__license__ = "Unlicense"

# Biblioteca python importada para interagir com as variaveis de ambiente do Sistema Operacional.
import os 

# Obtém o idioma do sistema, removendo possíveis .UTF-8 e convertendo para minúsculas
lang = os.getenv("LANG", "en_US").split('.')[0][:5].lower()

# Define a mensagem padrão em inglês
msg = "Hello, World!"  # Corrigido a vírgula (adicionado espaço)

# Verifica o idioma e altera a mensagem (comparando em minúsculas)
if lang == "pt_br":
    msg = "Olá, Mundo!"
elif lang == "it_it":     
    msg = "Ciao, Mondo!"  # Adicionado espaço após a vírgula   
elif lang == "es_es":                 
    msg = "Hola, Mundo!"  # Corrigido "es_SP" para "es_ES" (padrão espanhol)
                
print(msg)