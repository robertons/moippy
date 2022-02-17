# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', '348d2089063e4126b067b8907a2f49d5_v2', sandbox=True, debug=True)

    saldo = moippy.Balance()

    print(saldo)

    transferencia = moippy.Transfer(
        amount = 5,
        transferInstrument = {
            "method": "BANK_ACCOUNT",
            "bankAccount": {
                "type": "CHECKING",
                "bankNumber": "001",
                "agencyNumber": "1111",
                "agencyCheckNumber": "2",
                "accountNumber": "9999",
                "accountCheckNumber": "8",
                "holder": {
                    "fullname": "Roberto Neves",
                    "taxDocument": {
                        "type": "CPF",
                        "number": "09292800752"
                    }
                }
            }
        })

    transferencia.Create()

    print(transferencia.toJSON())


if __name__ == "__main__":
    main(sys.argv)
