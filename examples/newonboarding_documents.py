# -*- coding: utf-8 -*-
import json
import sys
import moipy


def main(arg):

    moipy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    onboarding = moipy.onboarding.Documents(
        returnUrl="https://www.website.com.br/documents",
        refreshUrl="https://www.website.com.br/invalid"
    )
    print(onboarding.toJSON())


if __name__ == "__main__":
    main(sys.argv)
