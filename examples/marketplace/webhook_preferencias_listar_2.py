# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ',
                'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    webhook = moippy.WebhooksPreferences()
    print(webhook.toJSON())


if __name__ == "__main__":
    main(sys.argv)


access_token = '0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ'
secret =  'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF'
resource_token = 'e0dc7c54ce4e4b53988525f32168ad79_v2'
app_secret = 'b769e7ec74b7417281463ca162060b0d'
sandbox = True
