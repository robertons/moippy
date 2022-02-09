# -*- coding: utf-8 -*-
import json
import moippy
import sys


def main(arg):

    moippy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # CRIAÇÃO DE COBRANÇA
    cobranca = moippy.charges.Create(
        moippy.Charge(
            description='Produto Exemplo',
            amount=340.0,
            paymentTypes=['CREDIT_CARD']
        ),
        moippy.Billing(
            name='Usuario Teste',
            document='cpf',
            email='usuario@email.com.br',
            address=moippy.Address(
                street='Endereco',
                number='Numero',
                complement='Complemento',
                neighborhood='Bairro',
                city='Cidade',
                state='UF',
                postCode='99999999'),
            phone='99999999999',
            notify=False
        )
    )

    # PROCESSAMENTO DE PAGAMENTO
    if len(cobranca) > 0:
        pagamento = moippy.payment.Create(
            chargeId=cobranca[0].id,
            creditcard=moippy.CreditCard(
                creditCardId='9a453d71-3ec1-44a5-b2f3-0596ced42a35'
            ),
            billing=moippy.Billing(
                name='Usuario Teste',
                email='usuario@email.com.br',
                address=moippy.Address(
                    street='Endereco',
                    number='Numero',
                    complement='Complemento',
                    neighborhood='Bairro',
                    city='Cidade',
                    state='UF',
                    postCode='99999999'),
                delayed=False
            )
        )


if __name__ == "__main__":
    main(sys.argv)
