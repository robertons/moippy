# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):

    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', '348d2089063e4126b067b8907a2f49d5_v2', sandbox=True, debug=True)

    banco = moippy.BankAccount(
        id="BKA-YDZA6XBNCOOW",
        bankNumber = "237",
        agencyNumber = "12345",
        agencyCheckNumber =  "0",
        accountNumber = "12345678",
        accountCheckNumber = "7",
        type = "SAVING",
        holder= {
            "taxDocument": {
                "type": "CPF",
                "number": "622.134.533-22"
            },
            "fullname": "Demo Moip"}
        )

    banco.Update()

    print(banco.toJSON())



if __name__ == "__main__":
    main(sys.argv)
