# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sinteseVoz2.py
#  Copyright 2017-08-22 tavares <tavares arroba cadernodelaboratorio.com.br>
#  0.1
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#
import os
import num2words


def main(args):
    inicio_cmd = 'espeak -vpt --stdout  '
    fim_cmd = ' | aplay'
    inicio_contagem = 10

    os.system("espeak -vpt --stdout 'Iniciando contagem regresssiva' | aplay")

    for nIndice in range(inicio_contagem, -1, -1):
        valor_atual = num2words.num2words(nIndice, lang='pt_BR')
        os.system(inicio_cmd + valor_atual + fim_cmd)

    os.system("espeak -vpt+whisper --stdout 'Funcionou' | aplay")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))