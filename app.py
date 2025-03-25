from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

# Função para verificar se o usuário é calouro
def verificar_calouro(resposta):
    resposta = resposta.strip().capitalize()
    if resposta == 'S':
        return "HAHAHAHAHAH BIXO!"
    elif resposta == 'N':
        return "ata, vc é normal"
    else:
        return "Por favor, responda com 'S' ou 'N'."

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = ''
    if request.method == 'POST':
        # Recupera a resposta do usuário do formulário
        resposta = request.form.get('resposta')
        resultado = verificar_calouro(resposta)
        return render_template('index.html', resultado=resultado)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
