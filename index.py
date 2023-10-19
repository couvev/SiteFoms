from flask import Flask, render_template, request, redirect, url_for
import send_email as se

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    global nome
    global idade
    
    if request.method == 'POST' and 'enviar' in request.form:
        nome = request.form['nome']
        idade = request.form['idade']
        
        return redirect(url_for('opcoes', nome=nome, idade=idade))

    return render_template('index.html')

@app.route('/opcoes', methods=['GET', 'POST'])
def opcoes():
    if request.method == 'POST' and 'enviar' in request.form:
        opcoes_selecionadas = request.form.getlist('opcoes')
        
        se.send(nome, idade, opcoes_selecionadas)
        
        return redirect(url_for('fim'))

    return render_template('opcoes.html')

@app.route('/fim')
def fim():
    
    return render_template('fim.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
