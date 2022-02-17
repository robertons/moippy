# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', 'e0dc7c54ce4e4b53988525f32168ad79_v2', sandbox=True, debug=True)

    extrato_detalhe = moippy.DetailStatement('43','2022-02-14')

    print(extrato_detalhe.toJSON())


if __name__ == "__main__":
    main(sys.argv)
