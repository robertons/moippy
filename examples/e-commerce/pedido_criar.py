# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ', 'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    pedido = moippy.Order(
        ownId = "1000",
        amount = moippy.Amount(
            currency = "BRL",
             subtotals = {
             "shipping":1500
             }
        ),
        items = [
          {
             "product":"Descrição do pedido",
             "category":"CLOTHING",
             "quantity":1,
             "detail":"Camiseta estampada branca",
             "price":9500
          }
       ],
        customer = {
          "id":"CUS-TBU823CK73TG"
       }
    )
    pedido.Create()
    print(pedido.toJSON())


if __name__ == "__main__":
    main(sys.argv)
