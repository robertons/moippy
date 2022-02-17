# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ', 'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    clientes = moippy.Customers()
    print(clientes.toJSON())


if __name__ == "__main__":
    main(sys.argv)
