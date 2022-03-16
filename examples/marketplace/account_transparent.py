# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', 'e0dc7c54ce4e4b53988525f32168ad79_v2', sandbox=True, debug=True)

    # CRIAR
    account = moippy.MoipAccount(
        email = {
            "address": "robertonsilva@gmail.com"
        },
        person = {
            "name": "Roberto",
            "lastName": "Neves",
            "taxDocument": {
                "type": "CPF",
                "number": "000.000.000-00"
            },
              "identityDocument": {
              "type" : "RG",
              "number": "11122233",
              "issuer": "ES",
              "issueDate": "2000-12-12"
              },
            "birthDate": "1982-02-02",
            "phone": {
                "countryCode": "55",
                "areaCode": "27",
                "number": "965213244"
            },
            "address": {
                "street": "Av. Brigadeiro Faria Lima",
                "streetNumber": "2927",
                "district": "Itaim",
                "zipCode": "01234000",
                "city": "São Paulo",
                "state": "SP",
                "country": "BRA"
            }
        },
        type ="MERCHANT",
        transparentAccount = True)

    account.Create()
    print(account.toJSON())


if __name__ == "__main__":
    main(sys.argv)
