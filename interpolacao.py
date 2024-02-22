#!/usr/bin/env python3

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1] 

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(",")
    
    # TODO: substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(templatepath.read()
        % {
            "nome": name,
            "produto": "caneta azul",
            "texto": "Escrever muito bem",
            "link": "felipecosta.net",
            "quantidade": 1,
            "preco": 50.5,
            # "email": email,
	}
)
print("-" * 50)