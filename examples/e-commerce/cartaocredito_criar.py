# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ', 'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    cartao_credito = moippy.CreditCard(
        expirationMonth = "12",
        expirationYear = "22",
        number = "4012001037141112",
        holder = {
          "fullname": "João Silva",
          "birthdate": "1990-10-22",
          "taxDocument": {
            "type": "CPF",
            "number": "22288866644"
          },
          "phone" : {
            "countryCode": "55",
            "areaCode": "11",
            "number": "55552266"
          }
         }
    )

    try:
        moippy.AddCreditCard('CUS-TBU823CK73TG', cartao_credito)
    except Exception as e:
        print(e)

    print(cartao_credito.toJSON())


if __name__ == "__main__":
    main(sys.argv)
