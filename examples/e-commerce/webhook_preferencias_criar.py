# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ',
                'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    webhook = moippy.WebhookPreference()
    webhook.events = ["ORDER.*"]
    webhook.target = "https://189.14.192.4/webhook"
    webhook.media = 'WEBHOOK'
    webhook.Create()
    print(webhook.toJSON())


if __name__ == "__main__":
    main(sys.argv)
