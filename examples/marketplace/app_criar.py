# -*- coding: utf-8 -*-
import json
import sys
sys.path.append("/Users/robertoneves/Projetos/moippy")
import moippy


def main(arg):

    moippy.Moip('0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ',
                'VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF', sandbox=True, debug=True)

    # CONSULTAR
    app = moippy.App()
    app.name = "App Name"
    app.description = "App dedicado aos fans!"
    app.site = "http://www.appname.com.br"
    app.redirectUri = "https://api.appname.com.br/gateway"
    app.Create()
    print(app.toJSON())


if __name__ == "__main__":
    main(sys.argv)
