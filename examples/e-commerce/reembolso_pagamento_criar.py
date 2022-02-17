# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ',
                'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    reembolso = moippy.Refund()

    reembolso.Create("PAY-IFJM9NH4ZHJ3", 100)

    print(reembolso.toJSON())


if __name__ == "__main__":
    main(sys.argv)
