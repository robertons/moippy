# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")

import moippy
import json



def main(arg):


    moippy.Moip('e0dc7c54ce4e4b53988525f32168ad79_v2', 'b769e7ec74b7417281463ca162060b0d', 'e0dc7c54ce4e4b53988525f32168ad79_v2', sandbox=True, debug=True)

    # CONSULTAR
    pedido = moippy.Order(
        ownId = "1100",
        amount = moippy.Amount(
            currency = "BRL",
             subtotals = {
             "shipping":5000
             }
        ),
        items = [
          {
             "product":"Teste Split",
             "category":"CLOTHING",
             "quantity":1,
             "detail":"Compra dividida",
             "price":95000
          }
       ],
       customer = {
          "id":"CUS-TBU823CK73TG"
       },
       receivers = [{
                "type": "SECONDARY",
                "feePayor":False,
                "moipAccount":{
                    "login": "MPA-04D5B4AB865C",
                    "fullname": "Roberto Neves",
                    "id":  "MPA-04D5B4AB865C",
                    },
                "amount": {
                    "refunds":0,
                    "fees": 0,
                    "fixed": 50,
                }

            }]
    )
    pedido.Create()
    print(pedido.toJSON())


    #{'ownId': '1100', 'amount': {'paid': 0, 'total': 100000, 'fees': 0, 'refunds': 0, 'liquid': 0, 'otherReceivers': 0, 'currency': 'BRL', 'subtotals': {'shipping': 5000, 'addition': 0, 'discount': 0, 'items': 95000}}, 'id': 'ORD-HIVUPPM7RSBD', 'status': 'CREATED', 'platform': 'V2', 'createdAt': '2022-02-15T16:54:47.894-03', 'updatedAt': '2022-02-15T16:54:47.894-03', '_links': {'self': {'href': 'https://sandbox.moip.com.br/v2/orders/ORD-HIVUPPM7RSBD'}, 'checkout': {'payCheckout': {'redirectHref': 'https://checkout-new-sandbox.moip.com.br?token=b4f1aef7-d41e-41fe-a0a3-1b358dc8f0b4&id=ORD-HIVUPPM7RSBD'}, 'payCreditCard': {'redirectHref': 'https://checkout-new-sandbox.moip.com.br?token=b4f1aef7-d41e-41fe-a0a3-1b358dc8f0b4&id=ORD-HIVUPPM7RSBD&payment-method=credit-card'}, 'payBoleto': {'redirectHref': 'https://checkout-new-sandbox.moip.com.br?token=b4f1aef7-d41e-41fe-a0a3-1b358dc8f0b4&id=ORD-HIVUPPM7RSBD&payment-method=boleto'}, 'payOnlineBankDebitItau': {'redirectHref': 'https://checkout-sandbox.moip.com.br/debit/itau/ORD-HIVUPPM7RSBD'}}}, 'items': [{'product': 'Teste Split', 'category': 'CLOTHING', 'quantity': 1, 'detail': 'Compra dividida', 'price': 95000}, {'product': 'Teste Split', 'detail': 'Compra dividida', 'quantity': 1, 'price': 95000, 'category': 'CLOTHING'}], 'receivers': [{'type': 'SECONDARY', 'feePayor': False, 'moipAccount': {'login': 'MPA-04D5B4AB865C', 'fullname': 'Roberto Neves', 'id': 'MPA-04D5B4AB865C'}, 'amount': {'refunds': 0, 'fees': 0, 'fixed': 50}}, {'moipAccount': {'id': 'MPA-NBK0TJRSKBEX', 'login': 'contato@ilhadoprazer.com.br', 'fullname': 'Edson  Santos de Roma Jr'}, 'type': 'PRIMARY', 'amount': {'total': 99950, 'currency': 'BRL', 'fees': 0, 'refunds': 0}, 'feePayor': True}, {'moipAccount': {'id': 'MPA-04D5B4AB865C', 'login': 'MPA-04D5B4AB865C', 'fullname': 'Roberto Neves'}, 'type': 'SECONDARY', 'amount': {'total': 50, 'currency': 'BRL', 'fees': 0, 'refunds': 0}, 'feePayor': False}], 'customer': {'id': 'CUS-TBU823CK73TG', 'ownId': '5', 'fullname': 'Roberto Neves', 'createdAt': '2022-02-10T10:52:58.000-03', 'updatedAt': '2022-02-15T16:54:47.897-03', 'email': 'robertonsilva@gmail.com', 'fundingInstrument': {'creditCard': {'id': 'CRC-X46EN5JBRN5L', 'brand': 'MASTERCARD', 'first6': '555566', 'last4': '8884', 'store': True}, 'method': 'CREDIT_CARD'}, 'moipAccount': {'id': 'MPA-QYFS6S2EWZ0H'}, '_links': {'self': {'href': 'https://sandbox.moip.com.br/v2/customers/CUS-TBU823CK73TG'}, 'hostedAccount': {'redirectHref': 'https://hostedaccount-sandbox.moip.com.br?token=ba947f9e-de59-4118-b740-6face7ac2909&id=CUS-TBU823CK73TG&mpa=MPA-NBK0TJRSKBEX'}}, 'fundingInstruments': [{'creditCard': {'id': 'CRC-X46EN5JBRN5L', 'brand': 'MASTERCARD', 'first6': '555566', 'last4': '8884', 'store': True}, 'method': 'CREDIT_CARD'}]}, 'events': [{'type': 'ORDER.CREATED', 'createdAt': '2022-02-15T16:54:47.894-03', 'description': ''}]}

if __name__ == "__main__":
    main(sys.argv)
