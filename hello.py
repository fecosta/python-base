#!/usr/bin/env python3
"""Hello world multi linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Ou ifnorme atraves do CLI argument --lang

Ou o usuario precisa digitar

Execução
    pyhthon3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Felipe Costa"
__license__ = "unlicense"


import os
import sys

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValeuError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
    # print(key, value)

current_language = arguments["lang"]

if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjuor, Monde!"
}

print(msg[current_language] * int(arguments["count"]))
