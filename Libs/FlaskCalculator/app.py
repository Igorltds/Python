from flask import Flask, request, render_template
from calculos import *


def create_app(config):
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')

    config.APP = app

    @app.route('/')
    def index():
        return render_template('html.html')

    @app.route('/calculaform', methods=['POST', 'GET'])
    def calculaform():
        v1 = request.form['v1']
        v2 = request.form['v2']
        operacao = request.form['operacao']

        try:
            v1 = float(v1)
        except ValueError:
            return "Valores errados"

        try:
            v2 = float(v2)
        except ValueError:
            return "Valores errados"


        match operacao:
            case "soma": return str(Soma.soma(v1, v2))
            case "+": return str(Soma.soma(v1, v2))

            case "subtracao": return str(Subtração.Subtrai(v1, v2))
            case "-": return str(Subtração.Subtrai(v1, v2))

            case "divisao": return str(Divisão.divide(v1, v2))
            case "/": return str(Divisão.divide(v1, v2))

            case "multiplicacao": return str(Multiplicação.multiplica(v1, v2))
            case "*": return str(Multiplicação.multiplica(v1, v2))
            
            case "potencia": return str(Potenciação.potencia(v1, v2))
            case "^": return str(Potenciação.potencia(v1, v2))

            case "raiz": return str(Raiz.raiz(v1, v2))
            case "/*": return str(Raiz.raiz(v1, v2))

            case "logaritimo": return str(Logaritimo.logaritimo(v1, v2))
            case "*/": return str(Logaritimo.logaritimo(v1, v2))
        return str("algo deu errado")
