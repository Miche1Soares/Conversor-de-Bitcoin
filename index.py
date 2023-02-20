from flask import Flask, render_template, request

import requests

from config import chave

from datapackage import Package


app = Flask(__name__)

conteudo = []
resultado = []

@app.route('/', methods=['GET','POST'])
def initPage():

    cripto = 'BTC'
    fiat1 = 'USD'
    fiat2 = 'BRL'
    fiat3 = 'EUR'

    if request.method == 'POST':
        
        if not (request.form.get('quant_fiat')) and request.form.get('quant_btc'):
            fiat_esco = request.form.get('moeda_fiat').upper()

            urlCalc = f'https://rest.coinapi.io/v1/exchangerate/BTC/{fiat_esco}'
            headers = {'X-CoinAPI-Key' : chave}
            
            valor = requests.get(urlCalc, headers=headers).json()

            quant_BTC = request.form.get('quant_btc')
            resCalc = float(quant_BTC) * float(valor['rate'])

            texto = f'{quant_BTC} BTC = {round(resCalc,2)} {fiat_esco}'

            resultado.insert(0,texto)

            if len(resultado) > 1:
                resultado.pop()

        if request.form.get('quant_fiat') and not (request.form.get('quant_btc')):
            fiat_esco = request.form.get('moeda_fiat').upper()

            urlCalc = f'https://rest.coinapi.io/v1/exchangerate/BTC/{fiat_esco}'
            headers = {'X-CoinAPI-Key' : chave}
            valor2 = requests.get(urlCalc, headers=headers).json()

            quant_fiat = request.form.get('quant_fiat')
            resCalc = float(quant_fiat) / float(valor2['rate'])

            texto = f'{quant_fiat} {fiat_esco} = {round(resCalc,8)} BTC'

            resultado.insert(0,texto)

            if len(resultado) > 1:
                resultado.pop()


    url = f'https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat1}'
    url2 = f'https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat2}'
    url3 = f'https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat3}'

    headers = {'X-CoinAPI-Key' : chave}

    response = requests.get(url, headers=headers).json()
    response2 = requests.get(url2, headers=headers).json()
    response3 = requests.get(url3, headers=headers).json()


    preco_usd = round(response['rate'],2)
    preco_brl = round(response2['rate'],2)
    preco_eur = round(response3['rate'],2)

    return render_template("index.html", conteudo=[preco_usd, preco_eur, preco_brl, resultado])