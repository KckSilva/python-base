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
__License__ = "Unlicense"

#Biblioteca python importada para interagir com as variaveis de ambiente do Sistema Operacional.
import os 

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello,Word!"

if current_language == "pt_BR":
                msg = "Olá, Mundo!"
elif current_language == "it_IT":     
                msg = "Ciao,Mondo!"    
elif current_language == "es_SP":                 
            msg = "Hola,Mundo!" 
                
print(msg)
 
