# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', 'e0dc7c54ce4e4b53988525f32168ad79_v2', sandbox=True, debug=True)

    cliente = moippy.Customer(
        ownId = "12",
        fullname = "João da Silva",
        email = "nome@gemail.com"
    )

    try:
        cliente.Create()
    except Exception as e:
        print(e)

    print(cliente.toJSON())


if __name__ == "__main__":
    main(sys.argv)
