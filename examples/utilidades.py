# -*- coding: utf-8 -*-
import json
import sys
import moipy

import uuid


def main(arg):

    moipy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # BANCOS
    bancos = moipy.util.Banks()
    print(bancos)

    # TIPOS EMPRESAS
    tipos_empresas = moipy.util.CompanyTypes()
    print(tipos_empresas)

    # AREAS NEGOCIO
    areas_de_negocio = moipy.util.BusinessAreas()
    print(areas_de_negocio)

    # CHAVE PUBLICA
    chave_publica = moipy.util.PublicKey()
    print(chave_publica)


if __name__ == "__main__":
    main(sys.argv)
