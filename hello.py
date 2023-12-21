#!/usr/bin/env python3
"""Hello world multi linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:
	export LANG=pt_BR

Execução
	pyhthon3 hello.py
	ou
	./hello.py
"""
__version__ = "0.0.1"
__author__ = "Felipe Costa"
__license__ = "unlicense"


import os

current_language = os.getenv("LANG","en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "es_SP":
	msg = "Hola, Mundo!"
elif current_language == "fe_FR":
	msg = "Bonjour, Monde!"
	
print(msg)
