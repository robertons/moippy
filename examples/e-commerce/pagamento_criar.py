# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ',
                'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    pagamento = moippy.Payment(
        installmentCount=1,
        statementDescriptor="Minha Loja",
        device={
            "ip": "127.0.0.1",
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
        },
        fundingInstrument=moippy.FundingInstrument(
            method="CREDIT_CARD",
            creditCard={
                "hash": "cZKZVqDYdw+l0vVWoO/qpafor7mHws7LmX/vjmxYYjb/a8HTOVcj8Zgs65Kb6rRyyT2vajvRfW9u8ugkWmzjOqNz4ceJv4bdS65iCKisFmU8TKVH7W0Pm+JsUPyBPYGlM2ncZf/AEGjmA8tMu/EkQWRgolLL3x9jDrVv/ufsDqUiA7sV5ko00TFTcz0/OOrn04xK5V0rrXvCswClTnU21lgrCj5sBntNszfO1JoyI9tNR5I30I9OsQmq+l2oBWu//uA/qcTq7DZpdn43h0t8fFz+5y9UednJZcWvGpayt/28CquESnHa6JXj/rssw3JgMV35iQ6gsRzX68zF76pV9A==",
                "store": True,
                "holder": {
                    "fullname": "Jose Portador da Silva",
                    "birthdate": "1988-12-30",
                    "taxDocument": {
                        "type": "CPF",
                        "number": "33333333333"
                    },
                    "phone": {
                        "countryCode": "55",
                        "areaCode": "11",
                        "number": "66778899"
                    }
                }
            }
        )
    )

    pagamento.Create("ORD-CMLLMEJ61QAZ")

    print(pagamento.toJSON())


if __name__ == "__main__":
    main(sys.argv)
