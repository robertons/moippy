# -*- coding: utf-8 -*-
import moipy
import json
import sys


def main(arg):

    moipy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # PLANO
    plano = moipy.Plan(name="Plano Teste", amount=100.00).Create()


if __name__ == "__main__":
    main(sys.argv)