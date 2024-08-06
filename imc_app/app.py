from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 16.9:
        return 'muito abaixo do peso'
    elif 17.0 <= imc <= 18.4:
        return 'abaixo do peso'
    elif  18.5 <= imc <= 24.9:
        return 'peso normal'
    elif 25 <= imc <= 29.9:
        return 'acima do peso'
    elif 30 <= imc <= 34.9:
        return 'obesidade grau 1'
    elif 35 <= imc <= 40:
        return 'obesidade grau 2'
    else:
        'obesidade grau 3'
        
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            
            return render_template('index.htm', imc=imc, classificacao=classificacao)
        except ValueError:
            return render_template('index.html', error='por favor, insira valores validos para peso e altura')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)